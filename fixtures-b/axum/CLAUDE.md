<!-- faf:start -->
<!-- faf: users-api | Rust | backend | REST API for the users of a small SaaS: look up, create and update user records -->
<!-- faf: claim=project.faf | family=FAF -->

# CLAUDE.md — users-api

## What This Is

REST API for the users of a small SaaS: look up, create and update user records

## Stack

- **Language:** Rust
- **Backend:** axum 0.8
- **API:** REST
- **Runtime:** Tokio
- **Database:** PostgreSQL
- **Connection:** sqlx 0.8
- **Hosting:** Docker on Fly.io
- **Build:** cargo
- **CI/CD:** GitHub Actions

## Context

- **Who:** Backend developers on a two-person team
- **What:** A JSON API over a PostgreSQL users table
- **Why:** The web and mobile apps need one source for user records
- **Where:** Docker on Fly.io, PostgreSQL managed by Fly
- **When:** MVP: read endpoints this sprint, writes next
- **How:** axum 0.8 handlers with shared AppState holding a sqlx PgPool; runtime-checked sqlx queries so the build needs no database

---

*STATUS: SYNC ACTIVE — 2026-11-17T00:03:57.139Z*
<!-- faf:end -->
