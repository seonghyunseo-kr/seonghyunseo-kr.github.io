import os
import re
import glob
import yaml
import requests

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "").strip()
MODEL = "gpt-4o-mini"

def split_front_matter(text: str):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            body = parts[2].lstrip("\n")
            fm = yaml.safe_load(fm_text) or {}
            return fm, body
    return {}, text

def strip_code_blocks(md: str) -> str:
    # Remove fenced code blocks ```...```
    return re.sub(r"```.*?```", "", md, flags=re.DOTALL)

def compress_whitespace(s: str) -> str:
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()

def has_en_summary(fm: dict) -> bool:
    try:
        en = fm.get("summary", {}).get("en", {})
        return bool(en.get("tldr")) and isinstance(en.get("bullets"), list) and len(en.get("bullets")) == 3
    except Exception:
        return False

def build_prompt(md_body: str) -> str:
    # Basic length guard for long posts
    max_chars = 12000
    md_body = md_body[:max_chars]

    return f"""You are summarizing a technical blog post written in English.

Requirements:
- Output MUST be valid YAML for the following schema only:
  tldr: <string>
  bullets: <list of exactly 3 strings>
- TL;DR: exactly one line.
- bullets: exactly 3 bullets.
- Prefer keeping the TOTAL length (tldr + bullets) within 500 characters, but prioritize preserving key meaning if a bit longer.
- Do NOT include code blocks or LaTeX; summarize concepts only.
- Do NOT add extra keys or commentary.

Blog post (Markdown):
{md_body}
"""

def call_openai(prompt: str) -> dict:
    if not OPENAI_API_KEY:
        raise RuntimeError("OPENAI_API_KEY is not set")

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.2,
    }

    r = requests.post(url, headers=headers, json=payload, timeout=60)
    r.raise_for_status()

    content = r.json()["choices"][0]["message"]["content"].strip()
    data = yaml.safe_load(content)

    if not isinstance(data, dict):
        raise ValueError("Model output is not a YAML mapping")
    if "tldr" not in data or "bullets" not in data:
        raise ValueError("Missing keys in summary YAML")
    if not isinstance(data["bullets"], list) or len(data["bullets"]) != 3:
        raise ValueError("bullets must be a list of exactly 3 strings")

    return data

def ensure_summary(fm: dict, summary_yaml: dict) -> dict:
    fm.setdefault("summary", {})
    fm["summary"].setdefault("en", {})
    fm["summary"]["en"]["tldr"] = str(summary_yaml["tldr"]).strip()
    fm["summary"]["en"]["bullets"] = [str(x).strip() for x in summary_yaml["bullets"]]
    return fm

def dump_front_matter(fm: dict) -> str:
    return "---\n" + yaml.safe_dump(fm, sort_keys=False, allow_unicode=True).strip() + "\n---\n\n"

def main():
    paths = sorted(glob.glob("_posts/*.md"))
    updated = 0

    for path in paths:
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        fm, body = split_front_matter(text)

        # Only generate when missing
        if has_en_summary(fm):
            continue

        cleaned = compress_whitespace(strip_code_blocks(body))
        if len(cleaned) < 200:
            continue

        try:
            prompt = build_prompt(cleaned)
            summary = call_openai(prompt)
            fm = ensure_summary(fm, summary)
        except Exception as e:
            # Fail open: publish without summary
            print(f"[SKIP] {path}: {e}")
            continue

        new_text = dump_front_matter(fm) + body
        if new_text != text:
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_text)
            updated += 1
            print(f"[UPDATED] {path}")

    print(f"Done. Updated {updated} file(s).")

if __name__ == "__main__":
    main()