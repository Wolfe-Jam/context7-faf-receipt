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

- **Who:** One Node developer
- **What:** An Express 5 JSON API
- **Why:** The docs site needs file listings
- **Where:** Docker
- **When:** MVP this month
- **How:** Express 5 routing (path-to-regexp 8): named wildcards like /files/*path, no bare * or regex strings; async handlers may throw

---

*STATUS: SYNC ACTIVE — 2026-11-17T01:23:42.727Z*
<!-- faf:end -->
