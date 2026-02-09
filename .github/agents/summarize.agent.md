# Summarize Agent (Manual, Copilot-assisted)

## Goal
When a blog post under `_posts/` is missing `summary.en`, generate it and add it to the post front matter.

## Target front matter schema
```yaml
    summary:
      en:
        tldr: "One-line TL;DR"
        bullets:
          - "Bullet 1"
          - "Bullet 2"
          - "Bullet 3"
```

## Requirements
- **Language:** English
- **TL;DR:** exactly one line
- **Bullets:** exactly 3 items
- **Length:** Prefer total length within 500 characters, but prioritize meaning if slightly longer
- **Content:** Do not include fenced code blocks or LaTeX; summarize concepts only
- **Safety:** Do not change other existing front matter keys
- **Idempotency:** If a summary already exists, do not overwrite it unless explicitly asked

## Workflow
1. Open the target post in `_posts/`.
2. Read the content and infer the key points.
3. Add `summary.en` in the front matter.
4. Ensure the YAML is valid (indentation, quoting).
5. Save the file.