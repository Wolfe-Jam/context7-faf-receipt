import subprocess, sys, shutil, pathlib, json
C = pathlib.Path(__file__).parent/'cases'
FAF = ['npx', '-y', 'faf-cli@8.10.0']
F = {
 'svelte4': {'project.name':'team-directory','project.goal':'Internal team directory: find people and their teams',
   'stack.database':'None (static data from load functions)','stack.connection':'None','stack.css_framework':'Plain CSS','stack.ui_library':'Own Svelte components','stack.cicd':'GitHub Actions','stack.hosting':'Vercel (adapter-auto)',
   'human_context.who':'Two front-end developers','human_context.what':'A SvelteKit 2 app on Svelte 4','human_context.why':'People need to find who owns what',
   'human_context.where':'Vercel','human_context.when':'Svelte 4 until Q3; the Svelte 5 upgrade is planned, not started',
   'human_context.how':'Svelte 4 syntax only (export let, $: reactive statements, on:event); no runes until the upgrade'},
 'pydv1': {'project.name':'orders-service','project.type':'backend','stack.backend':'FastAPI 0.99','stack.api_type':'REST','stack.runtime':'Python 3.12 (uvicorn)','stack.database':'None (in-memory for now)','stack.connection':'None','stack.hosting':'Docker on ECS','stack.build':'uv','stack.cicd':'GitHub Actions',
   'project.goal':'Orders service for the shop: customers and their orders',
   'human_context.who':'Python developers on the shop team','human_context.what':'A FastAPI JSON API','human_context.why':'Split orders out of the monolith',
   'human_context.where':'Docker on ECS','human_context.when':'Pinned to Pydantic 1.10 until the shared models package moves to v2',
   'human_context.how':'Pydantic v1 APIs only (class Config, .dict(), parse_obj, orm_mode); FastAPI 0.99 is the last release that supports v1'},
 'express5': {'project.name':'files-api','project.type':'backend','stack.backend':'Express 5','stack.api_type':'REST','stack.runtime':'Node.js 22','stack.database':'None','stack.connection':'None','stack.hosting':'Docker','stack.build':'None (plain ESM JavaScript)','stack.cicd':'GitHub Actions',
   'project.goal':'File metadata API for the docs site',
   'human_context.who':'One Node developer','human_context.what':'An Express 5 JSON API','human_context.why':'The docs site needs file listings',
   'human_context.where':'Docker','human_context.when':'MVP this month',
   'human_context.how':'Express 5 routing (path-to-regexp 8): named wildcards like /files/*path, no bare * or regex strings; async handlers may throw'},
 'ormmig': {'project.name':'blog-api','project.type':'backend','stack.backend':'Node.js (TypeScript)','stack.api_type':'REST','stack.runtime':'Node.js 22','stack.database':'PostgreSQL','stack.connection':'Drizzle ORM (Prisma legacy, being removed)','stack.hosting':'Railway','stack.build':'tsc','stack.cicd':'GitHub Actions',
   'project.goal':'Blog backend: posts, authors and comments',
   'human_context.who':'Two TypeScript developers','human_context.what':'A blog API moving from Prisma to Drizzle','human_context.why':'Prisma client size and cold starts',
   'human_context.where':'Railway with managed PostgreSQL','human_context.when':'Migration in progress: authors done in Drizzle, posts still Prisma',
   'human_context.how':'All new tables and queries go in Drizzle (src/db/schema.ts, drizzle-kit migrations); never add Prisma models; src/legacy is read-only'},
 'rawsql': {'project.name':'bookmarks','project.type':'backend','stack.backend':'Node.js (TypeScript)','stack.api_type':'REST','stack.runtime':'Node.js 22','stack.database':'PostgreSQL','stack.connection':'postgres.js (raw SQL, no ORM)','stack.hosting':'Fly.io','stack.build':'tsc','stack.cicd':'GitHub Actions',
   'project.goal':'Personal bookmarks service',
   'human_context.who':'One developer','human_context.what':'Bookmarks stored in PostgreSQL','human_context.why':'Own the data, no SaaS',
   'human_context.where':'Fly.io','human_context.when':'Tags next, then search',
   'human_context.how':'Raw SQL with postgres.js tagged templates, no ORM or query builder; every schema change is a numbered file in migrations/'},
 'monorepo': {'project.name':'acme','project.goal':'Acme shop: storefront web app and its API',
   'human_context.who':'Full-stack team of four','human_context.what':'Bun workspaces: apps/api (Hono), apps/web, packages/shared','human_context.why':'One repo, shared types',
   'human_context.where':'Cloudflare Workers (api) and Pages (web)','human_context.when':'Checkout next',
   'human_context.how':'HTTP endpoints only in apps/api (Hono); shared constants and types only from @acme/shared, never duplicated'},
 'internalui': {'project.name':'shop-admin','project.goal':'Admin console for the shop',
   'stack.css_framework':'Plain CSS (shop- classes)','stack.ui_library':'@shop/ui (our own, src/ui)','stack.database':'None (API client)','stack.connection':'None','stack.hosting':'Netlify','stack.cicd':'GitHub Actions',
   'human_context.who':'Front-end team','human_context.what':'React 18 admin app','human_context.why':'Staff manage orders and accounts',
   'human_context.where':'Netlify','human_context.when':'Account management this sprint',
   'human_context.how':'UI only from @shop/ui (Button, Modal); no third-party component libraries'},
 'dockeronly': {'project.name':'ops-tools','project.type':'cli','project.main_language':'Python','project.goal':'Ops command-line tools for the status page',
   'human_context.who':'The on-call engineer','human_context.what':'A Typer CLI shipped as a Docker image','human_context.why':'Quick checks during incidents',
   'human_context.where':'Docker image, deps pinned in the Dockerfile','human_context.when':'URL checks next',
   'human_context.how':'Typer 0.12 commands; HTTP with httpx 0.27 (not requests); output with rich'},
 'intent': {'project.name':'inventory-api','project.type':'backend','stack.backend':'FastAPI','stack.api_type':'REST','stack.runtime':'Python 3.12 (uvicorn)','stack.database':'PostgreSQL (SQLite in tests)','stack.connection':'SQLModel','stack.hosting':'Docker on Render','stack.build':'uv','stack.cicd':'GitHub Actions',
   'project.goal':'Inventory API for a small shop: items, then orders',
   'human_context.who':'One Python developer','human_context.what':'A JSON API over items','human_context.why':'Replace a spreadsheet',
   'human_context.where':'Docker on Render','human_context.when':'Items done. Next: orders, where an order has a customer email and line items (item id, quantity), and its total comes from item prices',
   'human_context.how':'FastAPI with SQLModel table models and Annotated Depends sessions'},
 'gostd': {'project.name':'people','project.type':'backend','stack.backend':'Go net/http (standard library)','stack.api_type':'REST','stack.runtime':'Go 1.23','stack.database':'None (in-memory store)','stack.connection':'None','stack.hosting':'Docker','stack.build':'go build','stack.cicd':'GitHub Actions',
   'project.goal':'People directory API',
   'human_context.who':'Go developers','human_context.what':'A JSON API on the standard library','human_context.why':'No dependencies to audit',
   'human_context.where':'Docker','human_context.when':'Read endpoints now',
   'human_context.how':'Standard library only, no router packages; Go 1.22+ ServeMux patterns ("GET /users/{id}") with r.PathValue'},
}
def run(args, cwd): return subprocess.run(FAF+args, cwd=cwd, capture_output=True, text=True)
for case in (sys.argv[1:] or F):
    a, b = C/case/'A', C/case/'B'
    if b.exists(): shutil.rmtree(b)
    subprocess.run(['cp','-c','-R',str(a),str(b)], check=True)
    run(['init'], b)
    for k,v in F[case].items():
        r = run(['edit',k,v], b)
        if r.returncode: print(case,'EDIT FAIL',k, (r.stderr or r.stdout).strip()[:120])
    s = run(['score'], b).stdout.strip().splitlines()
    print(f'{case:11}', ' | '.join(l.strip() for l in s[-2:]))
