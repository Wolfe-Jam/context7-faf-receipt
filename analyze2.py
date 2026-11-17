import json, re, subprocess, pathlib, glob, sys
T = pathlib.Path(__file__).parent; sys.path.insert(0, str(T)); from cases import CASES
EXCL = ['node_modules','target','.venv','.svelte-kit','__pycache__','.pytest_cache','*.db','bun.lock','bun.lockb','uv.lock','Cargo.lock','go.sum','.faf-dna']
def changed(case, arm, name):
    args = ['diff','-ruN'] + sum([['-x',e] for e in EXCL],[]) + [str(T/'cases'/case/arm), str(T/'runs2'/name)]
    out = subprocess.run(args, capture_output=True, text=True).stdout
    files = [l.split('\t')[0][4:].replace(str(T/'runs2'/name)+'/','') for l in out.splitlines() if l.startswith('+++ ')]
    added = '\n'.join(l[1:] for l in out.splitlines() if l.startswith('+') and not l.startswith('+++'))
    return files, added
rows = []
for f in sorted(glob.glob(str(T/'runs2'/'*.jsonl'))):
    name = pathlib.Path(f).stem; case, arm, n = name.split('-'); c = CASES[case]
    calls = []; res = {}
    for line in open(f):
        try: d = json.loads(line)
        except Exception: continue
        if d.get('type') == 'assistant':
            for b in d['message'].get('content', []):
                if b.get('type') == 'tool_use': calls.append((b['name'], b.get('input', {})))
        if d.get('type') == 'result': res = d
    c7 = [i for nm, i in calls if nm.startswith('mcp__context7')]
    ids = sorted({i.get('libraryId') or i.get('libraryName') or '?' for i in c7})
    first = next((k for k, (nm, _) in enumerate(calls) if nm in ('Edit', 'Write')), len(calls))
    files, added = changed(case, arm, name)
    bad = [p for p in c['bad'] if re.search(p, added, re.M | re.I)] + [p for p in c.get('badfiles', []) if p in files]
    good = [p for p in c['good'] if re.search(p, added, re.M)] + [p for p in c.get('goodfiles', []) if any(re.search(p, x) for x in files)]
    chk = (T/'runs2'/f'{name}.check').read_text().strip().splitlines()[-1] if (T/'runs2'/f'{name}.check').exists() else ''
    u = res.get('usage', {})
    rows.append(dict(run=name, edge=c['edge'], ok='exit=0' in chk, bad=bad, good=good, c7=len(c7), ids=ids,
        reads=sum(1 for nm, _ in calls[:first] if nm in ('Read', 'Glob', 'Grep')), tools=len(calls),
        tok=u.get('input_tokens', 0)+u.get('cache_read_input_tokens', 0)+u.get('cache_creation_input_tokens', 0),
        cost=round(res.get('total_cost_usd', 0), 3), wall=chk.split('wall=')[-1] if 'wall=' in chk else '', files=files,
        denied=len(res.get('permission_denials', []) or []), stop=res.get('subtype')))
if '--json' in sys.argv:
    print(json.dumps(rows)); sys.exit()
for r in rows:
    print(f"{r['run']:14} {'PASS' if r['ok'] else 'FAIL'} bad={r['bad'] or '-'} good={len(r['good'])}/{len(CASES[r['run'].split('-')[0]]['good'])+len(CASES[r['run'].split('-')[0]].get('goodfiles',[]))} c7={r['c7']} {r['ids']} reads={r['reads']} tools={r['tools']} tok={r['tok']//1000}k ${r['cost']} {r['wall']}s denied={r['denied']}")
