import subprocess, pathlib
C = pathlib.Path(__file__).parent/'cases'
FAF = ['npx', '-y', 'faf-cli@8.10.0']
P = {
 'svelte4': {'stack.state_management':'Svelte 4 stores and reactive statements','stack.connection':'load functions (static data)'},
 'pydv1': {'stack.connection':'In-memory dict (no database client yet)'},
 'express5': {'stack.database':'Filesystem (file metadata, no database)','stack.connection':'node:fs/promises'},
 'monorepo': {'stack.monorepo_tool':'Bun workspaces','stack.workspaces':'apps/*, packages/*','stack.admin':'Cloudflare dashboard','stack.cache':'Cloudflare KV','stack.search':'Postgres full-text (planned with checkout)','stack.storage':'Cloudflare R2',
   'monorepo.packages_count':'3 (@acme/api, @acme/web, @acme/shared)','monorepo.build_orchestrator':'bun run in each package (no turbo/nx)','monorepo.versioning_strategy':'Private packages, not published; workspace:*','monorepo.shared_configs':'Each app owns its tsconfig.json','monorepo.remote_cache':'Bun install cache in CI'},
 'internalui': {'stack.state_management':'React state and context','stack.connection':'fetch to the shop API'},
 'dockeronly': {'stack.hosting':'Docker image in the ops registry','stack.build':'docker build','stack.cicd':'GitHub Actions'},
 'gostd': {'stack.connection':'In-memory map behind sync.RWMutex'},
}
for case, edits in P.items():
    b = C/case/'B'
    for k,v in edits.items():
        r = subprocess.run(FAF+['edit',k,v], cwd=b, capture_output=True, text=True)
        if r.returncode: print(case,'EDIT FAIL',k,(r.stderr or r.stdout).strip()[:120])
for case in sorted(p.name for p in C.iterdir()):
    b = C/case/'B'
    s = subprocess.run(FAF+['score'], cwd=b, capture_output=True, text=True).stdout.strip().splitlines()
    sync = subprocess.run(FAF+['sync'], cwd=b, capture_output=True, text=True).returncode
    print(f'{case:11}', s[-2].split(' — ')[0].strip() if len(s)>1 else s, '| sync', sync, '| CLAUDE.md', (b/'CLAUDE.md').exists())
