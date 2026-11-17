import subprocess, sys, json, pathlib, shutil, time
from concurrent.futures import ThreadPoolExecutor
sys.path.insert(0, str(pathlib.Path(__file__).parent)); from cases import CASES
T = pathlib.Path(__file__).parent; OUT = T/'runs2'; OUT.mkdir(exist_ok=True)
def job(case, arm, n):
    c = CASES[case]; name = f'{case}-{arm}-{n}'; d = OUT/name
    if d.exists(): shutil.rmtree(d)
    subprocess.run(['cp','-c','-R', str(T/'cases'/case/arm), str(d)], check=True)
    cmd = ['claude','-p',c['prompt'],'--model','claude-sonnet-5-5','--setting-sources','project','--strict-mcp-config','--mcp-config',str(T/'c7-mcp.json'),
           '--disable-slash-commands','--no-session-persistence','--max-budget-usd','3','--disallowedTools','WebSearch','WebFetch',
           '--allowedTools','Read','Glob','Grep','Edit','Write','mcp__context7',*c['allow'],'--output-format','stream-json','--verbose']
    t0 = time.time()
    with open(OUT/f'{name}.jsonl','w') as o, open(OUT/f'{name}.err','w') as e:
        subprocess.run(cmd, cwd=d, stdout=o, stderr=e, stdin=subprocess.DEVNULL, timeout=1200)
    wall = round(time.time()-t0)
    r = subprocess.run(c['check'], shell=True, cwd=d, capture_output=True, text=True, timeout=600)
    (OUT/f'{name}.check').write_text(r.stdout[-3000:]+r.stderr[-3000:]+f'\nexit={r.returncode} wall={wall}\n')
    print(f'{name} exit={r.returncode} wall={wall}', flush=True)
cases = sys.argv[1].split(',') if len(sys.argv)>1 and sys.argv[1] != 'all' else list(CASES)
n = sys.argv[2] if len(sys.argv)>2 else '1'
jobs = [(c,a,n) for c in cases for a in ('A','B')]
with ThreadPoolExecutor(4) as ex: list(ex.map(lambda j: job(*j), jobs))
