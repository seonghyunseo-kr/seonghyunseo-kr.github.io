---
layout: post
title: "[Tooling] GitLab / Hugging Face / arXiv"
date: 2026-02-04
tags: [etc, study, tooling]
style: border
color: primary
comments: false
description: "My practical notes for GitLab, Hugging Face, and arXiv to improve collaboration, reproducibility, and review workflow."
toc: true
---

I use these tools frequently at work, but I realized I don’t have a consistent workflow documented.
This note is meant to be my “default playbook” for reliable reviews and collaboration.

## GitLab
---

#### What is GitLab? 
GitLab is a DevOps platform that bundles:

- Git repository hosting (source control)
- Issue tracking (planning & coordination)
- Merge Requests (MR) (code review + merge workflow)
- CI/CD pipelines (build/test/deploy automation)
- Wiki / Docs (team knowledge base)


**How I use GitLab in Practice:** 
> **Plan in Issues/Epics → Implement on branches → Review via MR → Verify with CI → Merge & close issues.**
 - Issue tracking and planning
 - Code review via Merge Requests (MR)
 - Team documentation (Wiki / README)

\

#### Key functions
1. Issue
A single trackable unit of work: feature, bug, refactor, documentation, experiment, etc.

2. Merge Request & Review
Branch -> push and commit -> merge request -> reviewer assign -> merge

3. Wiki 


#### Key Commands 

---git command
git status
git add
git commit -m "commit message"
git push / pull 
git branch 
git clone
---


#### Repository Structure *In Practice* 
- gitignore
- config.yml
- pyproject.toml
- requrements
- makefile
- venv activation
- src? models? tests? 
- unit test / integration test? 


---

## Hugging Face

---

## Arvix

