import subprocess, shutil, pathlib, sys
C = pathlib.Path(__file__).parent/'cases'
FAF = ['npx', '-y', 'faf-cli@8.10.0']
F = {
 'kit3': {'project.name':'recipe-box','project.goal':'Recipe box: browse and share recipes',
   'stack.frontend':'SvelteKit 3.1','stack.backend':'SvelteKit 3.1','stack.state_management':'Svelte 5 runes','stack.database':'Static data (src/lib)','stack.connection':'load functions','stack.css_framework':'Plain CSS','stack.ui_library':'Own Svelte components','stack.hosting':'Vercel (adapter-auto)','stack.build':'Vite 8','stack.cicd':'GitHub Actions',
   'human_context.who':'A home cook and a front-end developer','human_context.what':'A SvelteKit 3 app','human_context.why':'Share family recipes',
   'human_context.where':'Vercel','human_context.when':'Upgraded to SvelteKit 3 in October 2026; search next',
   'human_context.how':'SvelteKit 3.1 with Svelte 5 runes'},
 'logs': {'project.name':'files-api','project.type':'backend','stack.backend':'Express 5','stack.api_type':'REST','stack.runtime':'Node.js 22','stack.database':'Filesystem (file metadata, no database)','stack.connection':'node:fs/promises','stack.hosting':'Docker','stack.build':'None (plain ESM JavaScript)','stack.cicd':'GitHub Actions',
   'project.goal':'File metadata API for the docs site',
   'human_context.who':'One Node developer; ops reads the logs in Grafana Loki','human_context.what':'An Express 5 JSON API','human_context.why':'The docs site needs file listings',
   'human_context.where':'Docker; stdout shipped to Loki','human_context.when':'Logging before launch',
   'human_context.how':'Logging decided: pino with pino-http, JSON to stdout (Loki parses it); no console.log in app code'},
 'deploy': {'project.name':'inventory-api','project.type':'backend','stack.backend':'FastAPI','stack.api_type':'REST','stack.runtime':'Python 3.12 (uvicorn)','stack.database':'PostgreSQL on Cloud SQL (SQLite in tests)','stack.connection':'SQLModel','stack.hosting':'Google Cloud Run','stack.build':'uv','stack.cicd':'GitHub Actions',
   'project.goal':'Inventory API for a small shop',
   'human_context.who':'One Python developer','human_context.what':'A JSON API over items','human_context.why':'Replace a spreadsheet',
   'human_context.where':'Google Cloud Run: a container that listens on $PORT, scales to zero, no local disk',
   'human_context.when':'First deploy this week',
   'human_context.how':'FastAPI with SQLModel table models and Annotated Depends sessions'},
}
def run(a, cwd): return subprocess.run(FAF+a, cwd=cwd, capture_output=True, text=True)
for case in (sys.argv[1:] or F):
    a, b = C/case/'A', C/case/'B'
    if b.exists(): shutil.rmtree(b)
    subprocess.run(['cp','-c','-R',str(a),str(b)], check=True)
    run(['init'], b)
    for k,v in F[case].items():
        r = run(['edit',k,v], b)
        if r.returncode: print(case,'EDIT FAIL',k,(r.stderr or r.stdout).strip()[:100])
    s = run(['score'], b).stdout.strip().splitlines()
    print(case, ' | '.join(x.strip()[:150] for x in s[-2:]))
    if 'TROPHY' in ' '.join(s): print('  sync', run(['sync'], b).returncode)
