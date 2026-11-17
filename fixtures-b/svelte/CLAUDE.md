<!-- faf:start -->
<!-- faf: notes-app | TypeScript | svelte | A notes app: users write, list and share short posts -->
<!-- faf: claim=project.faf | family=FAF -->

# CLAUDE.md — notes-app

## What This Is

A notes app: users write, list and share short posts

## Stack

- **Language:** TypeScript
- **Framework:** SvelteKit
- **CSS:** None (plain CSS)
- **UI Library:** Own Svelte components
- **State:** Runes
- **Backend:** SvelteKit
- **API:** Server Routes
- **Runtime:** Node.js
- **Database:** PostgreSQL
- **Connection:** Drizzle ORM 0.40 (postgres.js)
- **Hosting:** Node
- **Build:** Vite 6
- **CI/CD:** GitHub Actions

## Context

- **Who:** Small team of SvelteKit developers
- **What:** A SvelteKit 2 app with server routes over PostgreSQL
- **Why:** A simple self-hosted notes tool the team controls
- **Where:** Node server (adapter-node) on a VPS
- **When:** MVP: posts now, user sign-up next
- **How:** Svelte 5 runes ($props, $state, $derived) in components; form actions in +page.server.ts; Drizzle schema in src/lib/server/db/schema.ts

---

*STATUS: SYNC ACTIVE — 2026-11-17T00:03:56.955Z*
<!-- faf:end -->
