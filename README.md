# esnet-netauto-retreat-2026
Welcome to Asma's NetAuto topic — "AI as an Augmentation Tool (not a replacement)". This repository contains code, exercises, and supporting materials designed to help YOU developers explore practical AI workflows and use AI to augment their work. Enjoy learning and experimenting!
## Table of Contents
- [esnet-netauto-retreat-2026](#esnet-netauto-retreat-2026)
  - [Table of Contents](#table-of-contents)
  - [Summary](#summary)
  - [Prereqs](#prereqs)
  - [Exercises](#exercises)
    - [ipls.json file](#iplsjson-file)
    - [Exercise #1](#exercise-1)
    - [Exercise #2](#exercise-2)
  - [Commit](#commit)
## Summary
You'll use this repository to explore the exercise materials and save your work in the team files folder under your name. The goal is for you to write your own code and then use AI as an assistive tool to improve, refactor, and extend that code. The exercises in this repo use Python as the primary programming language.
## Prereqs
Before you start the exercises, make sure you have the following in place:

- A GitHub account. Create one at https://github.com/ if you don't already have one.
- Git installed and configured locally (set user.name and user.email). Example:

  `git config --global user.name "Your Name"`

  `git config --global user.email "you@example.com"`

- Clone this repository to your machine:

  `git clone <repo-url>`

- Create and switch to a working branch (replace `<your-branch>` with a descriptive name):

  `git checkout -b <your-branch>`

- Under `team_files/` create a directory with your name (for example `team_files/asma`) and add the two exercise files if they are not already present: `range_only.py` and `split.py`. You can copy the templates from `team_files/asma` if needed.
- Create an account on https://claude.ai as will use it as an AI assistant in our retreat.
## Exercises 
### ipls.json file
Examine the ipls.json file in the exercise folder, The overall structure of the JSON file has a single top-level key "ipl" which contains a dictionary/object with 6 entries representing different IP prefix lists. The Top-Level Keys (IP Prefix List Names) where each key in the ipl object represents a different IP prefix list configuration. Value Structure (Array of Objects) where each key maps to an array (list) of objects. Each object in the array represents a single IP prefix configuration with these fields: `ip_prefixes`, `type`, `start` and `end`.
### Exercise #1
Open the `exercise_files/ipls.json` file and inspect its structure (the top-level "ipl" key contains multiple prefix-list entries; each entry is an array of objects with fields such as `ip_prefixes`, `type`, `start`, and `end`).

Create `team_files/<your-name>/split.py` that reads the JSON, iterates all prefix entries, and separates IPv4 prefixes from IPv6 prefixes. Your script should detect the address family (IPv4 vs IPv6) for each prefix (CIDR format), collect them into two lists (or write them to separate output files), and handle common edge cases (empty lists and malformed prefixes) with graceful errors or warnings.
### Exercise #2
Open `exercise_files/ipls.json` and inspect the structure (see the `ipl` top-level key and the list-of-objects value format).

Create `team_files/<your-name>/range_only.py` that reads the JSON and extracts all IP prefixes whose `type` field equals `"range"`.

Suggested behavior:
- Iterate every prefix list entry in `ipl` and collect objects where `type` is `range`.
- Output the matching prefixes to a list or write them to an output file (for example `range_prefixes.txt`).
- Handle edge cases gracefully: missing `type` fields, empty lists, or malformed entries should produce warnings rather than crashing.

This exercise focuses on correct JSON parsing, filtering by the `type` field, and producing a clear, testable output.
## Commit
When you're finished, save your changes, commit them to your branch, and push the branch to GitHub (for example: `git add . && git commit -m "complete exercises" && git push origin <your-branch>`).
