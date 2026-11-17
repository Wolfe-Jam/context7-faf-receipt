<!-- faf:start -->
<!-- faf: orders-service | Python | backend | Orders service for the shop: customers and their orders -->
<!-- faf: claim=project.faf | family=FAF -->

# CLAUDE.md — orders-service

## What This Is

Orders service for the shop: customers and their orders

## Stack

- **Language:** Python
- **Backend:** FastAPI 0.99
- **API:** REST
- **Runtime:** Python 3.12 (uvicorn)
- **Database:** None (in-memory for now)
- **Connection:** In-memory dict (no database client yet)
- **Hosting:** Docker on ECS
- **Build:** uv
- **CI/CD:** GitHub Actions

## Context

- **Who:** Python developers on the shop team
- **What:** A FastAPI JSON API
- **Why:** Split orders out of the monolith
- **Where:** Docker on ECS
- **When:** Pinned to Pydantic 1.10 until the shared models package moves to v2
- **How:** Pydantic v1 APIs only (class Config, .dict(), parse_obj, orm_mode); FastAPI 0.99 is the last release that supports v1

---

*STATUS: SYNC ACTIVE — 2026-11-17T01:23:44.576Z*
<!-- faf:end -->
