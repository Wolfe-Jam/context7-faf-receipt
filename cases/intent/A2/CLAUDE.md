# inventory-api

Inventory API for a small shop: items, then orders. It replaces a spreadsheet. One Python developer works on it.

## Stack
- FastAPI, REST, Python 3.12 (uvicorn)
- SQLModel; PostgreSQL in production, SQLite in tests
- uv for dependencies; GitHub Actions CI; Docker on Render

## Conventions
- FastAPI with SQLModel table models and Annotated Depends sessions.

## Roadmap
- Items: done.
- Next: orders. An order has a customer email and line items (item id, quantity), and its total comes from item prices.
