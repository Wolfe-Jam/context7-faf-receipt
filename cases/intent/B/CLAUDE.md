<!-- faf:start -->
<!-- faf: inventory-api | Python | backend | Inventory API for a small shop: items, then orders -->
<!-- faf: claim=project.faf | family=FAF -->

# CLAUDE.md — inventory-api

## What This Is

Inventory API for a small shop: items, then orders

## Stack

- **Language:** Python
- **Backend:** FastAPI
- **API:** REST
- **Runtime:** Python 3.12 (uvicorn)
- **Database:** PostgreSQL (SQLite in tests)
- **Connection:** SQLModel
- **Hosting:** Docker on Render
- **Build:** uv
- **CI/CD:** GitHub Actions

## Context

- **Who:** One Python developer
- **What:** A JSON API over items
- **Why:** Replace a spreadsheet
- **Where:** Docker on Render
- **When:** Items done. Next: orders, where an order has a customer email and line items (item id, quantity), and its total comes from item prices
- **How:** FastAPI with SQLModel table models and Annotated Depends sessions

---

*STATUS: SYNC ACTIVE — 2026-11-17T01:23:43.340Z*
<!-- faf:end -->
