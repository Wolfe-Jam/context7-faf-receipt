<!-- faf:start -->
<!-- faf: bookmarks | TypeScript | backend | Personal bookmarks service -->
<!-- faf: claim=project.faf | family=FAF -->

# CLAUDE.md — bookmarks

## What This Is

Personal bookmarks service

## Stack

- **Language:** TypeScript
- **Backend:** Node.js (TypeScript)
- **API:** REST
- **Runtime:** Node.js 22
- **Database:** PostgreSQL
- **Connection:** postgres.js (raw SQL, no ORM)
- **Hosting:** Fly.io
- **Build:** tsc
- **CI/CD:** GitHub Actions

## Context

- **Who:** One developer
- **What:** Bookmarks stored in PostgreSQL
- **Why:** Own the data, no SaaS
- **Where:** Fly.io
- **When:** Tags next, then search
- **How:** Raw SQL with postgres.js tagged templates, no ORM or query builder; every schema change is a numbered file in migrations/

---

*STATUS: SYNC ACTIVE — 2026-11-17T01:23:44.906Z*
<!-- faf:end -->
