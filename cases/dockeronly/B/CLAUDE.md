<!-- faf:start -->
<!-- faf: ops-tools | Python | cli | Ops command-line tools for the status page -->
<!-- faf: claim=project.faf | family=FAF -->

# CLAUDE.md — ops-tools

## What This Is

Ops command-line tools for the status page

## Stack

- **Language:** Python
- **Hosting:** Docker image in the ops registry
- **Build:** docker build
- **CI/CD:** GitHub Actions

## Context

- **Who:** The on-call engineer
- **What:** A Typer CLI shipped as a Docker image
- **Why:** Quick checks during incidents
- **Where:** Docker image, deps pinned in the Dockerfile
- **When:** URL checks next
- **How:** Typer 0.12 commands; HTTP with httpx 0.27 (not requests); output with rich

---

*STATUS: SYNC ACTIVE — 2026-11-17T01:23:42.410Z*
<!-- faf:end -->
