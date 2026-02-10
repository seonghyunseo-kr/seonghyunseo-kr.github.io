---
layout: post
title: "GitLab Workflow and ML Repo Structure"
date: 2026-02-04
tags: [etc, tooling]
style: border
color: primary
comments: false
description: "Practical notes for GitLab/Github to improve communication, reproducibility, and review workflow."
toc: true
---

## 1) Git + GitHub/GitLab: how I actually work

### 1.1 What is GitLab?
GitLab is a DevOps platform that bundles:

- Git repository hosting (source control)
- Issue tracking (planning & coordination)
- Merge Requests (MR) (code review + merge workflow)
- CI/CD pipelines (build/test/deploy automation)
- Wiki/Docs (team knowledge base)

In practice, GitHub and GitLab feel similar at the surface (repos + PR/MR), but GitLab tends to be more “all-in-one” for teams because issues, CI, and permissions are tightly integrated.

### 1.2 My default workflow
> **Plan in Issues/Epics → Implement on branches → Review via MR → Verify with CI → Merge & close issues.**

- **Issues/Epics**: define scope, acceptance criteria, references, and ownership
- **Branches**: isolate changes per issue
- **MR (Merge Request)**: code review + discussion + approvals
- **CI**: sanity check (lint/test/build) before merge
- **Merge**: squash/merge strategy depending on team convention

### 1.3 Key GitLab features (minimal but important)

#### (1) Issues
An issue is a single trackable unit of work:
- feature, bug, refactor, documentation, experiment, etc.

What I try to include:
- background / why
- task list
- definition of done
- links (docs, tickets, papers)

#### (2) Merge Requests (MR) & review
Typical flow:
- branch → commit/push → create MR → assign reviewers → resolve comments → CI passes → merge

Good MR hygiene:
- small scope (reviewable)
- clear description + screenshots/logs if relevant
- link the issue (so planning and code are connected)

#### (3) Wiki / Docs
Use this to avoid tribal knowledge:
- onboarding steps
- environment setup
- runbooks (debugging, deployment, incident notes)

### 1.4 Git essentials (commands I actually use)
```bash
git status
git add .
git commit -m "message"
git push
git pull

git branch
git checkout -b feature/my-change
git log --oneline --decorate --graph --all
git diff

git clone <repo-url>
```

## 2) Why repository structure matters (for ML work especially)

For ML/DL projects, a repo isn’t just “where code lives”—it’s the unit of:

- **Collaboration**: reviewable changes, consistent conventions, shared ownership
- **Reproducibility**: the ability to rerun the same experiment with the same code/config
- **Experiment tracking**: understanding what changed and why results changed
- **Future reuse**: turning one-off study code into reusable building blocks

### 2.1 A practical structure that scales

I like to split a repo into three roles:

#### 1) `src/` = reusable library code
- “importable” modules used across experiments
- less duplication
- easier refactoring and maintenance
- easier to test

#### 2) `experiments/` = runnable scripts
- thin entrypoints (small, runnable scripts)
- parse args, load config, and **call modules in `src/`**
- easier to reproduce runs and keep a stable CLI interface

#### 3) Notes/docs folders
- concept notes, references, interview notes
- link to code/experiments where applicable

A simple mental model:

- `experiments/` = steering wheel (you drive experiments from here)
- `src/` = engine parts (reusable components)
- notes = driving manual (the knowledge base)


### 2.2 Common files you’ll see in real repos (and why)

- `.gitignore`: prevent committing artifacts, local data, checkpoints, secrets
- `pyproject.toml` (or `requirements.txt`): dependencies & packaging metadata
- `README.md`: entry point for humans (how to run / what it is)
- `tests/`: basic automated checks (unit tests for reusable code)
- `Makefile` (optional): shortcuts for lint/test/run tasks
- CI config (`.gitlab-ci.yml` / GitHub Actions): automated checks on merge requests / pull requests

