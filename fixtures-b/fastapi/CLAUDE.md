<!-- faf:start -->
<!-- faf: inventory-api | Python | backend | Inventory API for a small shop: create, list and price stock items -->
<!-- faf: claim=project.faf | family=FAF -->

# CLAUDE.md — inventory-api

## What This Is

Inventory API for a small shop: create, list and price stock items

## Stack

- **Language:** Python
- **Backend:** FastAPI
- **API:** REST
- **Runtime:** Python 3.12 (uvicorn)
- **Database:** PostgreSQL (SQLite in tests)
- **Connection:** SQLModel 0.0.24 (Pydantic v2, SQLAlchemy 2)
- **Hosting:** Docker on Render
- **Build:** uv
- **CI/CD:** GitHub Actions

## Context

- **Who:** One Python developer and the shop's front-end contractor
- **What:** A JSON API over an items table, migrated with Alembic
- **Why:** Replace a spreadsheet the shop updates by hand
- **Where:** Docker on Render, managed PostgreSQL
- **When:** MVP this month: items CRUD, then orders
- **How:** FastAPI with SQLModel table models and Annotated Depends sessions; Pydantic v2 APIs (model_validate, model_dump)

---

*STATUS: SYNC ACTIVE — 2026-11-17T00:03:57.343Z*
<!-- faf:end -->
