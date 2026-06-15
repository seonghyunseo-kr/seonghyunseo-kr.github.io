"""Generate KR/EN summary fields for _projects/ and _academic/ front matter.

For each file in _projects/*.md, fills in (if missing/empty):
  - summary_en : 2-3 sentence English summary (from Overview + My Contributions)
  - summary_kr : 2-3 sentence Korean summary
  - name_kr    : Korean translation of the project title

For each file in _academic/*.md, fills in (if missing/empty):
  - title_kr   : Korean translation of the title
  - summary_kr : 1-2 sentence Korean summary (from description + Overview)

Usage:
    ANTHROPIC_API_KEY=sk-... python scripts/summarize_posts.py
"""

import glob
import json
import os
import re

import frontmatter
from anthropic import Anthropic

MODEL = "claude-sonnet-4-6"

_client = None


def get_client() -> Anthropic:
    global _client
    if _client is None:
        api_key = os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise RuntimeError("ANTHROPIC_API_KEY environment variable is not set")
        _client = Anthropic(api_key=api_key)
    return _client


def extract_section(body: str, heading: str) -> str:
    """Return the text under a markdown heading line containing `heading`,
    up to (but not including) the next heading of any level."""
    pattern = rf"^#{{1,6}}\s*{re.escape(heading)}\s*\n(.*?)(?=^#{{1,6}}\s|\Z)"
    match = re.search(pattern, body, re.DOTALL | re.MULTILINE)
    return match.group(1).strip() if match else ""


def call_claude(prompt: str) -> dict:
    response = get_client().messages.create(
        model=MODEL,
        max_tokens=600,
        messages=[{"role": "user", "content": prompt}],
    )
    text = response.content[0].text.strip()

    # Strip markdown code fences if the model wrapped the JSON anyway
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())

    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("Model output is not a JSON object")
    return data


def clean(value) -> str:
    return " ".join(str(value).split())


def yaml_quote(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def update_front_matter(text: str, updates: dict) -> str:
    """Set or insert `key: "value"` fields inside the YAML front matter block,
    leaving the rest of the file (and other front matter fields) untouched."""
    lines = text.split("\n")
    if lines[0].strip() != "---":
        raise ValueError("File does not start with front matter")

    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        raise ValueError("Could not find end of front matter")

    fm_lines = lines[1:end_idx]
    remaining = lines[end_idx:]

    updated_keys = set()
    for i, line in enumerate(fm_lines):
        m = re.match(r"^([A-Za-z0-9_]+):", line)
        if m and m.group(1) in updates:
            key = m.group(1)
            fm_lines[i] = f"{key}: {yaml_quote(updates[key])}"
            updated_keys.add(key)

    for key, value in updates.items():
        if key not in updated_keys:
            fm_lines.append(f"{key}: {yaml_quote(value)}")

    return "\n".join(["---"] + fm_lines + remaining)


PROJECT_PROMPT = """You are localizing a personal portfolio website for an AI/ML researcher.

Project title: {name}

## Overview
{overview}

## My Contributions
{contributions}

Based on the information above, generate:
1. "summary_en": A 2-3 sentence English summary of the project suitable for a project card (third person or neutral tone).
2. "summary_kr": A natural, professional Korean summary of the same project (2-3 sentences). Write naturally in Korean rather than translating summary_en word-for-word.
3. "name_kr": A natural Korean translation of the project title "{name}".

Respond with ONLY a single JSON object, no markdown code fences, no extra commentary:
{{"summary_en": "...", "summary_kr": "...", "name_kr": "..."}}
"""

ACADEMIC_PROMPT = """You are localizing a personal academic portfolio page for an AI/ML researcher.

Title: {title}
Description: {description}

## Overview
{overview}

Based on the information above, generate:
1. "title_kr": A natural Korean translation of the title "{title}".
2. "summary_kr": A natural, professional 1-2 sentence Korean summary of the work, based on the description and overview. Do not translate word-for-word.

If the Overview is "(TBD)" or empty, base the summary mainly on the title and description.

Respond with ONLY a single JSON object, no markdown code fences, no extra commentary:
{{"title_kr": "...", "summary_kr": "..."}}
"""


def process_project(path: str) -> None:
    post = frontmatter.load(path)
    fm = post.metadata

    if fm.get("summary_en") and fm.get("summary_kr") and fm.get("name_kr"):
        print(f"[SKIP] {path} (already filled)")
        return

    name = fm.get("name", "")
    overview = extract_section(post.content, "Overview") or "(none)"
    contributions = extract_section(post.content, "My Contributions") or "(none)"

    prompt = PROJECT_PROMPT.format(name=name, overview=overview, contributions=contributions)

    try:
        data = call_claude(prompt)
        updates = {
            "summary_en": clean(data["summary_en"]),
            "summary_kr": clean(data["summary_kr"]),
            "name_kr": clean(data["name_kr"]),
        }
    except Exception as e:
        print(f"[ERROR] {path}: {e}")
        return

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    new_text = update_front_matter(text, updates)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)

    print(f"[UPDATED] {path}")
    print(f"  summary_en: {updates['summary_en']}")
    print(f"  summary_kr: {updates['summary_kr']}")
    print(f"  name_kr:    {updates['name_kr']}")


def process_academic(path: str) -> None:
    post = frontmatter.load(path)
    fm = post.metadata

    if fm.get("title_kr") and fm.get("summary_kr"):
        print(f"[SKIP] {path} (already filled)")
        return

    title = fm.get("title", "")
    description = fm.get("description", "") or "(none)"
    overview = extract_section(post.content, "Overview") or "(none)"

    prompt = ACADEMIC_PROMPT.format(title=title, description=description, overview=overview)

    try:
        data = call_claude(prompt)
        updates = {
            "title_kr": clean(data["title_kr"]),
            "summary_kr": clean(data["summary_kr"]),
        }
    except Exception as e:
        print(f"[ERROR] {path}: {e}")
        return

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    new_text = update_front_matter(text, updates)
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_text)

    print(f"[UPDATED] {path}")
    print(f"  title_kr:   {updates['title_kr']}")
    print(f"  summary_kr: {updates['summary_kr']}")


def main():
    project_paths = sorted(glob.glob("_projects/*.md"))
    academic_paths = sorted(glob.glob("_academic/*.md"))

    print(f"== Projects ({len(project_paths)}) ==")
    for path in project_paths:
        process_project(path)

    print(f"\n== Academic ({len(academic_paths)}) ==")
    for path in academic_paths:
        process_academic(path)


if __name__ == "__main__":
    main()
