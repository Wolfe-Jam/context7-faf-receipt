<!-- faf:start -->
<!-- faf: blog-api | TypeScript | backend | Blog backend: posts, authors and comments -->
<!-- faf: claim=project.faf | family=FAF -->

# CLAUDE.md — blog-api

## What This Is

Blog backend: posts, authors and comments

## Stack

- **Language:** TypeScript
- **Backend:** Node.js (TypeScript)
- **API:** REST
- **Runtime:** Node.js 22
- **Database:** PostgreSQL
- **Connection:** Drizzle ORM (Prisma legacy, being removed)
- **Hosting:** Railway
- **Build:** tsc
- **CI/CD:** GitHub Actions

## Context

- **Who:** Two TypeScript developers
- **What:** A blog API moving from Prisma to Drizzle
- **Why:** Prisma client size and cold starts
- **Where:** Railway with managed PostgreSQL
- **When:** Migration in progress: authors done in Drizzle, posts still Prisma
- **How:** All new tables and queries go in Drizzle (src/db/schema.ts, drizzle-kit migrations); never add Prisma models; src/legacy is read-only

---

*STATUS: SYNC ACTIVE — 2026-11-17T01:23:44.265Z*
<!-- faf:end -->
