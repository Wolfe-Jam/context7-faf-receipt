<!-- faf:start -->
<!-- faf: people | Go | backend | People directory API -->
<!-- faf: claim=project.faf | family=FAF -->

# CLAUDE.md — people

## What This Is

People directory API

## Stack

- **Language:** Go
- **Backend:** Go net/http (standard library)
- **API:** REST
- **Runtime:** Go 1.23
- **Database:** None (in-memory store)
- **Connection:** In-memory map behind sync.RWMutex
- **Hosting:** Docker
- **Build:** go build
- **CI/CD:** GitHub Actions

## Context

- **Who:** Go developers
- **What:** A JSON API on the standard library
- **Why:** No dependencies to audit
- **Where:** Docker
- **When:** Read endpoints now
- **How:** Standard library only, no router packages; Go 1.22+ ServeMux patterns ("GET /users/{id}") with r.PathValue

---

*STATUS: SYNC ACTIVE — 2026-11-17T01:23:43.039Z*
<!-- faf:end -->
