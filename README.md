# esnet-netauto-retreat-2026

Welcome to Asma's NetAuto mini-retreat — "AI as an Augmentation Tool (not a replacement)". This repository contains code, exercises, and supporting materials to help developers learn how to use AI as an assistive tool for network automation tasks.

---

## Quick links

- Exercises: `exercise_files/ipls.json`
- Team files (your workspace): `team_files/<your-name>/`

## Table of contents

- [esnet-netauto-retreat-2026](#esnet-netauto-retreat-2026)
  - [Quick links](#quick-links)
  - [Table of contents](#table-of-contents)
  - [Summary](#summary)
  - [Prereqs](#prereqs)
  - [Exercises](#exercises)
    - [ipls.json (structure)](#iplsjson-structure)
    - [Exercise 1 — split prefixes (`split.py`)](#exercise-1--split-prefixes-splitpy)
    - [Exercise 2 — range-only (`range_only.py`)](#exercise-2--range-only-range_onlypy)
  - [How to run (examples)](#how-to-run-examples)
  - [Commit \& push](#commit--push)
  - [Contributing](#contributing)

---

## Summary

This repository is a hands-on lab. You'll write Python scripts that parse the provided `ipls.json`, perform simple filters and transformations, and save outputs to your `team_files/<your-name>/` directory. The exercises are meant to be short (about 1–2 hours each) and focused on practical JSON parsing and IP prefix handling.

## Prereqs

Ensure the following before starting:

- Git (configured with `user.name` and `user.email`). Example:

  `git config --global user.name "Your Name"`

  `git config --global user.email "you@example.com"`

- Python 3.8+
- Clone the repo and create a branch:

  `git clone <repo-url>`

  `cd esnet-netauto-retreat-2026`

  `git checkout -b <your-branch>`

- Create your personal folder under `team_files/`, e.g. `team_files/asma/`, and add or copy the two exercise files: `split.py` and `range_only.py`.
- (Optional) Create an account on https://claude.ai if you plan to use it as an AI assistant during the exercises.

## Exercises

### ipls.json (structure)

The file `exercise_files/ipls.json` contains a top-level key `ipl` whose value is an object mapping prefix-list names to arrays of prefix objects. Each prefix object typically has fields like:

- `ip_prefixes` — a list of prefix strings (CIDR)
- `type` — a string such as `range` or other types
- `start`, `end` — optional range endpoints

Inspect the file to familiarize yourself with the shape of the data before coding.

### Exercise 1 — split prefixes (`split.py`)

Goal: write `team_files/<your-name>/split.py` that reads `exercise_files/ipls.json`, iterates all entries, and separates IPv4 and IPv6 prefixes.

Requirements and suggestions:

- Detect address family (IPv4 vs IPv6) using Python's `ipaddress` module.
- Produce two outputs (lists or files): one for IPv4 prefixes and one for IPv6 prefixes (e.g. `ipv4.txt`, `ipv6.txt`).
- Handle empty or malformed prefixes with warnings (do not crash).

Example checklist:

- Read JSON
- For each `ip_prefixes` entry, validate and classify each prefix
- Save or print results

### Exercise 2 — range-only (`range_only.py`)

Goal: write `team_files/<your-name>/range_only.py` that reads `exercise_files/ipls.json` and extracts prefix objects where `type == "range"`.

Suggested behavior:

- Iterate all prefix-list entries under `ipl` and filter objects with `type == "range"`.
- Output matching prefixes to a file (e.g. `range_prefixes.txt`) or return them as a list.
- Handle missing or malformed fields with warnings.

## How to run (examples)

From the repository root you can run your scripts like:

```bash
python3 team_files/<your-name>/split.py
python3 team_files/<your-name>/range_only.py
```

If you write outputs to files, check them under your `team_files/<your-name>/` directory.

## Commit & push

When you're finished, save your changes, commit them to your branch, and push to GitHub. Example:

```bash
git add .
git commit -m "complete exercises"
git push origin <your-branch>
```

## Contributing

If you want to improve the exercises or add tests, please open a pull request with a clear description of changes. Keep commits small and use meaningful commit messages.

---

Happy hacking — ask for help if you want starter templates for `split.py` or `range_only.py`!
