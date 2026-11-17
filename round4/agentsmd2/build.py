import pathlib, subprocess, shutil, json, re, sys
W = pathlib.Path(sys.argv[1]); R = pathlib.Path('<rig>/c7test/cases')
FAF = ['bun', str(pathlib.Path.home()/'FAF/cli/dist/cli.js')]
PERM = {'storage': {'*': 'deny', 'ls*': 'allow', 'cat *': 'allow', 'find *': 'allow', 'grep *': 'allow', 'npm *': 'allow', 'node *': 'allow', 'npx *': 'allow'},
        'logs2': {}, 'intent': {'uv run *': 'allow', 'uv run': 'allow'},
        'deploy': {'uv run *': 'allow', 'uv run': 'allow'},
        'logs': {'*': 'deny', 'ls*': 'allow', 'cat *': 'allow', 'find *': 'allow', 'grep *': 'allow', 'npm *': 'allow', 'node *': 'allow', 'npx *': 'allow'}}
POINTER = "Project facts, including the six W's (who, what, why, where, when, how): see `project.faf`."
def six_ws(case):
    lines = (R/case/'B'/'CLAUDE.md').read_text().splitlines()
    i = lines.index('## Context')
    out = ['## Context', '']
    for l in lines[i+1:]:
        if l.startswith('- **'): out.append(l)
        elif l.startswith('## ') or l.startswith('---'): break
    return '\n'.join(out)
for case in ('logs', 'storage'):
    for arm in ('P0', 'P1', 'P2', 'P3'):
        d = W/'fixtures'/case/arm; d.mkdir(parents=True, exist_ok=True)
        subprocess.run(['rsync','-a','--exclude=CLAUDE.md','--exclude=.faf-dna','--exclude=*.db', str(R/case/'A')+'/', str(d)+'/'], check=True)
        shutil.copy(R/case/'B'/'project.faf', d/'project.faf')
        cfg = {'$schema': 'https://opencode.ai/config.json',
               'permission': {'edit': 'allow', 'webfetch': 'deny', 'bash': PERM[case]}}
        (d/'opencode.json').write_text(json.dumps(cfg, indent=2)+'\n')
        if arm == 'P0': continue
        subprocess.run(FAF+['export','--agents'], cwd=d, capture_output=True, check=True)
        a = (d/'AGENTS.md').read_text()
        if arm == 'P2': a = a.replace('<!-- faf:end -->', POINTER+'\n<!-- faf:end -->')
        if arm == 'P3': a = a.replace('<!-- faf:end -->', six_ws(case)+'\n<!-- faf:end -->')
        (d/'AGENTS.md').write_text(a)
print('built')
