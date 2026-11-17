# inventory-api

Inventory API for a small shop. It replaces a spreadsheet. One Python developer works on it.

## Stack
- FastAPI, REST, Python 3.12 (uvicorn)
- SQLModel; PostgreSQL on Cloud SQL in production, SQLite in tests
- uv for dependencies; GitHub Actions CI

## Hosting
- Google Cloud Run: a container that listens on $PORT, scales to zero, no local disk.
- First deploy this week.

## Conventions
- FastAPI with SQLModel table models and Annotated Depends sessions.
