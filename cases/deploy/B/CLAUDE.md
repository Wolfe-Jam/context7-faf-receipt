<!-- faf:start -->
<!-- faf: inventory-api | Python | backend | Inventory API for a small shop -->
<!-- faf: claim=project.faf | family=FAF -->

# CLAUDE.md — inventory-api

## What This Is

Inventory API for a small shop

## Stack

- **Language:** Python
- **Backend:** FastAPI
- **API:** REST
- **Runtime:** Python 3.12 (uvicorn)
- **Database:** PostgreSQL on Cloud SQL (SQLite in tests)
- **Connection:** SQLModel
- **Hosting:** Google Cloud Run
- **Build:** uv
- **CI/CD:** GitHub Actions

## Context

- **Who:** One Python developer
- **What:** A JSON API over items
- **Why:** Replace a spreadsheet
- **Where:** Google Cloud Run: a container that listens on $PORT, scales to zero, no local disk
- **When:** First deploy this week
- **How:** FastAPI with SQLModel table models and Annotated Depends sessions

---

*STATUS: SYNC ACTIVE — 2026-11-17T01:56:24.393Z*
<!-- faf:end -->
