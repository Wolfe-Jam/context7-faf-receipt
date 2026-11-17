import json, re, subprocess, pathlib, glob, collections, sys
W = pathlib.Path(__file__).parent; OUT = W/'codex'
GOOD = {'intent': r'class Order\b|class OrderLine|class OrderItem|/orders', 'deploy': r'Cloud Run|gcloud|run\.app', 'logs': r'pino'}
EXCL = ['node_modules','.venv','__pycache__','.pytest_cache','*.db','uv.lock','package-lock.json','bun.lock']
rows = []
for f in sorted(glob.glob(str(OUT/'*-P?-*.jsonl'))):
    name = pathlib.Path(f).stem; case, arm, n = name.split('-')
    read_faf = False; text = []; tools = 0; tok = 0
    for l in open(f):
        try: d = json.loads(l)
        except Exception: continue
        it = d.get('item', {})
        if d.get('type') == 'item.completed' and it.get('type') in ('command_execution', 'file_change', 'mcp_tool_call'):
            tools += 1
            if 'project.faf' in json.dumps({k: it.get(k) for k in ('command', 'changes')}): read_faf = True
        if it.get('type') == 'agent_message': text.append(it.get('text', ''))
        if d.get('type') == 'turn.completed': tok = d.get('usage', {}).get('input_tokens', 0) + d.get('usage', {}).get('output_tokens', 0)
    diff = subprocess.run(['diff','-ruN']+sum([['-x',e] for e in EXCL+['opencode.json']],[])+[str(W/'fixtures'/case/arm), str(OUT/name)], capture_output=True, text=True).stdout
    added = '\n'.join(x[1:] for x in diff.splitlines() if x.startswith('+') and not x.startswith('+++'))
    good = bool(re.search(GOOD[case], added + '\n'.join(text), re.I))
    built = bool(added.strip())
    chk = (OUT/f'{name}.check').read_text().strip().splitlines()[-1] if (OUT/f'{name}.check').exists() else ''
    rows.append(dict(run=name, case=case, arm=arm, right=good and built, built=built, read_faf=read_faf, ok='exit=0' in chk, tools=tools, tok=tok, wall=chk.split('wall=')[-1]))
if sys.argv[-1] == '--json': print(json.dumps(rows)); sys.exit()
agg = collections.defaultdict(lambda: [0,0,0,0])
for r in rows:
    a = agg[(r['case'], r['arm'])]; a[0]+=1; a[1]+=r['right']; a[2]+=r['read_faf']; a[3]+=r['ok']
for k in sorted(agg):
    a = agg[k]; print(f'{k[0]:7} {k[1]}  right {a[1]}/{a[0]}  read project.faf {a[2]}/{a[0]}  check pass {a[3]}/{a[0]}')
