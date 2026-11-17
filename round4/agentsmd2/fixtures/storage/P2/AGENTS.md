<!-- faf:start -->
<!-- faf: files-api | JavaScript | backend | File metadata API for the docs site -->
<!-- faf: claim=project.faf | family=FAF -->

# AGENTS.md — files-api

File metadata API for the docs site — JavaScript · type: backend

> Authored by faf — do not edit the managed block; refresh with `faf export --agents`. Hand-written content outside the managed block is preserved.

## Setup & build

```bash
bun run start    # start
```

## Run the tests

```bash
bun run test
```

## Where things live

- `package.json`

## Conventions

- ESM modules (`type: module`)

## Guardrails

- **Always OK:** read the tree · run the tests (`bun run test`).
- **Ask first:** dependency installs, deletions, migrations, schema changes, publish/release.
- **Never:** force-push · push straight to `main` (branch and open a PR) · commit secrets.

## Definition of Done

Done when: `bun run test` passes · changes committed with a conventional message.

## When stuck

Ask a clarifying question, propose a short plan, or open a draft PR with notes — do not push large speculative changes to `main`.

## Commit & PR

- Conventional Commits preferred (`feat:`, `fix:`, `chore:`, …).
- Branch off `main` and open a PR — never commit to `main` directly.
- If build/test scripts or layout change, refresh this file in the **same PR** (`faf export --agents`).

## Stack

- **Backend:** Express 5
- **API:** REST
- **Runtime:** Node.js 22
- **Database:** Filesystem (file metadata, no database yet)
- **Connection:** node:fs/promises
- **Hosting:** Docker
- **Build:** None (plain ESM JavaScript)
- **CI/CD:** GitHub Actions
Project facts, including the six W's (who, what, why, where, when, how): see `project.faf`.
<!-- faf:end -->
