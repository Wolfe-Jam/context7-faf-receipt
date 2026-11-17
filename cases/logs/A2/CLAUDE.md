# files-api

File metadata API for the docs site. One Node developer works on it.

## Stack
- Express 5, REST, Node.js 22, plain ESM JavaScript (no build)
- Filesystem only (node:fs/promises), no database
- Docker; GitHub Actions CI

## Logging
- Decided: pino with pino-http, JSON to stdout. Ops reads the logs in Grafana Loki, which parses the JSON.
- No console.log in app code.
- Logging is due before launch.
