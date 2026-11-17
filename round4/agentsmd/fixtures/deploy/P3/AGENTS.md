<!-- faf:start -->
<!-- faf: inventory-api | Python | backend | Inventory API for a small shop -->
<!-- faf: claim=project.faf | family=FAF -->

# AGENTS.md — inventory-api

Inventory API for a small shop — Python · type: backend

> Authored by faf — do not edit the managed block; refresh with `faf export --agents`. Hand-written content outside the managed block is preserved.

## Run the tests

```bash
pytest
```

## Where things live

- `pyproject.toml`

## Guardrails

- **Always OK:** read the tree · run the tests (`pytest`).
- **Ask first:** dependency installs, deletions, migrations, schema changes, publish/release.
- **Never:** force-push · push straight to `main` (branch and open a PR) · commit secrets.

## Definition of Done

Done when: `pytest` passes · changes committed with a conventional message.

## When stuck

Ask a clarifying question, propose a short plan, or open a draft PR with notes — do not push large speculative changes to `main`.

## Commit & PR

- Conventional Commits preferred (`feat:`, `fix:`, `chore:`, …).
- Branch off `main` and open a PR — never commit to `main` directly.
- If build/test scripts or layout change, refresh this file in the **same PR** (`faf export --agents`).

## Stack

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
<!-- faf:end -->
