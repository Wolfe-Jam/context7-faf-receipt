<!-- faf:start -->
<!-- faf: files-api | JavaScript | backend | File metadata API for the docs site -->
<!-- faf: claim=project.faf | family=FAF -->

# CLAUDE.md — files-api

## What This Is

File metadata API for the docs site

## Stack

- **Language:** JavaScript
- **Backend:** Express 5
- **API:** REST
- **Runtime:** Node.js 22
- **Database:** Filesystem (file metadata, no database)
- **Connection:** node:fs/promises
- **Hosting:** Docker
- **Build:** None (plain ESM JavaScript)
- **CI/CD:** GitHub Actions

## Context

- **Who:** One Node developer; ops reads the logs in Grafana Loki
- **What:** An Express 5 JSON API
- **Why:** The docs site needs file listings
- **Where:** Docker; stdout shipped to Loki
- **When:** Logging before launch
- **How:** Logging decided: pino with pino-http, JSON to stdout (Loki parses it); no console.log in app code

---

*STATUS: SYNC ACTIVE — 2026-11-17T01:56:19.923Z*
<!-- faf:end -->
