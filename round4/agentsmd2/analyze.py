import json, re, subprocess, pathlib, glob, collections, sys
W = pathlib.Path(__file__).parent
TARGET = {'logs': r'pino', 'storage': r'better-sqlite3'}
EXCL = ['node_modules','.venv','__pycache__','*.db','package-lock.json','bun.lock','data','opencode.json']
def events(agent, f):
    text, faf = [], False
    for l in open(f):
        try: d = json.loads(l)
        except Exception: continue
        if agent == 'codex':
            it = d.get('item', {})
            if it.get('type') == 'agent_message': text.append(it.get('text', ''))
            if it.get('type') == 'command_execution' and 'project.faf' in str(it.get('command')): faf = True
        else:
            p = d.get('part', {})
            if d.get('type') == 'text': text.append(p.get('text', ''))
            if d.get('type') == 'tool_use' and 'project.faf' in json.dumps(p.get('state', {}).get('input', {})): faf = True
    return ' '.join(text), faf
rows = []
for f in sorted(glob.glob(str(W/'runs'/'*-P?-*.jsonl'))):
    name = pathlib.Path(f).stem; agent, case, arm, n = name.split('-')
    text, faf = events(agent, f)
    diff = subprocess.run(['diff','-ruN']+sum([['-x',e] for e in EXCL],[])+[str(W/'fixtures'/case/arm), str(W/'runs'/name)], capture_output=True, text=True).stdout
    added = '\n'.join(x[1:] for x in diff.splitlines() if x.startswith('+') and not x.startswith('+++'))
    used = bool(re.search(TARGET[case], added, re.I)); knew = used or bool(re.search(TARGET[case], text, re.I))
    built = bool(added.strip())
    asked = (not built) and bool(re.search(r'\?|confirm|may i|approval', text, re.I))
    chk = (W/'runs'/f'{name}.check').read_text().strip().splitlines()[-1]
    rows.append(dict(run=name, agent=agent, case=case, arm=arm, knew=knew, used=used, built=built, asked=asked, read_faf=faf, ok='exit=0' in chk))
if sys.argv[-1] == '--json': print(json.dumps(rows)); sys.exit()
agg = collections.defaultdict(lambda: collections.Counter())
for r in rows:
    a = agg[(r['agent'], r['case'], r['arm'])]; a['n'] += 1
    for k in ('knew','used','built','asked','read_faf','ok'): a[k] += r[k]
for k in sorted(agg):
    a = agg[k]; print(f"{k[0]:8} {k[1]:7} {k[2]}  knew {a['knew']}/{a['n']}  used {a['used']}/{a['n']}  built {a['built']}/{a['n']}  asked {a['asked']}/{a['n']}  read project.faf {a['read_faf']}/{a['n']}  tests {a['ok']}/{a['n']}")
