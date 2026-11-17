<!-- faf:start -->
<!-- faf: acme | TypeScript | monorepo-root | Acme shop: storefront web app and its API -->
<!-- faf: claim=project.faf | family=FAF -->

# CLAUDE.md — acme

## What This Is

Acme shop: storefront web app and its API

## Stack

- **Language:** TypeScript
- **Monorepo:** Bun workspaces
- **Package Manager:** bun
- **Workspaces:** apps/*, packages/*
- **Admin:** Cloudflare dashboard
- **Cache:** Cloudflare KV
- **Search:** Postgres full-text (planned with checkout)
- **Storage:** Cloudflare R2

## Context

- **Who:** Full-stack team of four
- **What:** Bun workspaces: apps/api (Hono), apps/web, packages/shared
- **Why:** One repo, shared types
- **Where:** Cloudflare Workers (api) and Pages (web)
- **When:** Checkout next
- **How:** HTTP endpoints only in apps/api (Hono); shared constants and types only from @acme/shared, never duplicated

---

*STATUS: SYNC ACTIVE — 2026-11-17T01:23:43.961Z*
<!-- faf:end -->
