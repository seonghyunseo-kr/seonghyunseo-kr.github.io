# Copilot Instructions (Repo)

This repository is a GitHub Pages site built with Jekyll. Blog posts are stored in `_posts/` as Markdown files.

## Summaries (Manual, Copilot-assisted)
- When asked to summarize a post, follow `.github/agents/summarize.agent.md`.
- Store summaries in the post front matter under `summary.en` (do not insert into the markdown body).
- Do not overwrite an existing `summary.en` unless explicitly requested.
- Summary format must be:
  - One-line `tldr`
  - Exactly 3 `bullets`
  - Prefer total length within 500 characters, but prioritize meaning if slightly longer
  - No fenced code blocks and no LaTeX in the summary (concepts only)

## Safety / Editing rules
- Preserve existing front matter keys (e.g., `layout`, `title`, `date`, `tags`, etc.).
- Keep YAML valid: correct indentation; quote strings with special characters.