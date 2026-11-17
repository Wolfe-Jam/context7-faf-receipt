import subprocess, sys, pathlib, shutil, time
from concurrent.futures import ThreadPoolExecutor
W = pathlib.Path(__file__).parent; OUT = W/'codex'
sys.path.insert(0, str(W)); from run import PROMPT, CHECK
def job(case, arm, n):
    name = f'{case}-{arm}-{n}'; d = OUT/name
    if d.exists(): shutil.rmtree(d)
    subprocess.run(['cp','-c','-R', str(W/'fixtures'/case/arm), str(d)], check=True)
    (d/'opencode.json').unlink(missing_ok=True)
    t0 = time.time()
    with open(OUT/f'{name}.jsonl','w') as o, open(OUT/f'{name}.err','w') as e:
        try: subprocess.run(['codex','exec','--json','--skip-git-repo-check','--ephemeral','--ignore-user-config','-s','workspace-write',
                             '-c','sandbox_workspace_write.network_access=true','-C',str(d),PROMPT[case]], stdout=o, stderr=e, stdin=subprocess.DEVNULL, timeout=900)
        except subprocess.TimeoutExpired: e.write('\nTIMEOUT\n')
    wall = round(time.time()-t0)
    r = subprocess.run(CHECK[case], shell=True, cwd=d, capture_output=True, text=True, timeout=600)
    (OUT/f'{name}.check').write_text(r.stdout[-2000:]+r.stderr[-2000:]+f'\nexit={r.returncode} wall={wall}\n')
    print(f'codex {name} exit={r.returncode} wall={wall}', flush=True)
n = sys.argv[1]
jobs = [(c,a,n) for c in PROMPT for a in ('P0','P1','P2','P3')]
with ThreadPoolExecutor(3) as ex: list(ex.map(lambda j: job(*j), jobs))
