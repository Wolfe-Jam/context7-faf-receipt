import json, sys, re, subprocess, pathlib, glob
T = pathlib.Path(__file__).parent
TELLS = {
  'svelte': [r'export let ', r'^\s*\$:', r'\bon:(submit|click|input)='],
  'axum':   [r'route\(\s*"[^"]*/:'],
  'fastapi':[r'\.dict\(', r'orm_mode', r'from_orm', r'parse_obj\('],
}
OTHER = {
  'svelte': r'prisma|express|next\.js|react|kysely|typeorm|better-sqlite',
  'axum':   r'actix|diesel|rocket|warp|sea_orm|tokio_postgres',
  'fastapi':r'flask|django|tortoise|peewee|declarative_base',
}
EXCL = ['node_modules','target','.venv','.svelte-kit','__pycache__','.pytest_cache']
def diff(r, arm, n):
    src = T/('fixtures' if arm=='A' else 'fixtures-b')/r
    args = ['diff','-ruN'] + sum([['-x',e] for e in EXCL+['*.db','bun.lock','Cargo.lock','uv.lock']],[]) + [str(src), str(T/'runs'/f'{r}-{arm}-{n}')]
    return subprocess.run(args, capture_output=True, text=True).stdout
rows=[]
for f in sorted(glob.glob(str(T/'runs'/'*.jsonl'))):
    name = pathlib.Path(f).stem; r, arm, n = name.split('-')
    calls=[]; res={}
    for line in open(f):
        try: d=json.loads(line)
        except: continue
        if d.get('type')=='assistant':
            for b in d['message'].get('content',[]):
                if b.get('type')=='tool_use': calls.append((b['name'], b.get('input',{})))
        if d.get('type')=='result': res=d
    c7=[(n_.split('__')[-1], i) for n_,i in calls if n_.startswith('mcp__context7')]
    ids=sorted({i.get('libraryId') or i.get('context7CompatibleLibraryID') or i.get('libraryName') or '?' for _,i in c7})
    first_edit = next((k for k,(n_,_) in enumerate(calls) if n_ in ('Edit','Write')), len(calls))
    reads = sum(1 for n_,_ in calls[:first_edit] if n_ in ('Read','Glob','Grep'))
    dtxt = diff(r, arm, n); added='\n'.join(l[1:] for l in dtxt.splitlines() if l.startswith('+') and not l.startswith('+++'))
    tells=[t for t in TELLS[r] if re.search(t, added, re.M)]
    other=sorted(set(m.lower() for m in re.findall(OTHER[r], added, re.I)))
    chk=(T/'runs'/f'{name}.check').read_text().strip().splitlines()[-1] if (T/'runs'/f'{name}.check').exists() else ''
    u=res.get('usage',{})
    rows.append(dict(run=name, ok=('exit=0' in chk), c7_calls=len(c7), c7_ids=ids, reads_before_edit=reads,
      tool_calls=len(calls), turns=res.get('num_turns'), in_tok=u.get('input_tokens',0)+u.get('cache_read_input_tokens',0)+u.get('cache_creation_input_tokens',0),
      out_tok=u.get('output_tokens'), cost=round(res.get('total_cost_usd',0),3), wall=chk.split('wall=')[-1] if 'wall=' in chk else '',
      tells=tells, other_stack=other, stop=res.get('subtype')))
for x in rows: print(json.dumps(x))
