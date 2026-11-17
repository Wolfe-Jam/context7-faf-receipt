import subprocess, sys, json, pathlib, shutil, time
from concurrent.futures import ThreadPoolExecutor
W = pathlib.Path(__file__).parent
PROMPT = {
 'intent': 'Add the next feature on our roadmap, with tests. Make sure `uv run pytest` passes.',
 'deploy': 'Get the app ready to deploy: add whatever files our hosting platform needs, and make sure `uv run pytest` still passes.',
 'logs':   'Add request logging and log any unhandled errors. Make sure `npm test` passes.',
}
CHECK = {'intent': 'uv run -q pytest -q', 'deploy': 'uv run -q pytest -q', 'logs': 'npm test'}
def job(case, arm, n):
    name = f'{case}-{arm}-{n}'; d = W/'runs'/name
    if d.exists(): shutil.rmtree(d)
    subprocess.run(['cp','-c','-R', str(W/'fixtures'/case/arm), str(d)], check=True)
    t0 = time.time()
    with open(W/'runs'/f'{name}.jsonl','w') as o, open(W/'runs'/f'{name}.err','w') as e:
        try: subprocess.run(['opencode','run','--format','json','--model','opencode/big-pickle','--dir',str(d),PROMPT[case]], cwd=d, stdout=o, stderr=e, stdin=subprocess.DEVNULL, timeout=900)
        except subprocess.TimeoutExpired: e.write('\nTIMEOUT\n')
    wall = round(time.time()-t0)
    r = subprocess.run(CHECK[case], shell=True, cwd=d, capture_output=True, text=True, timeout=600)
    (W/'runs'/f'{name}.check').write_text(r.stdout[-2000:]+r.stderr[-2000:]+f'\nexit={r.returncode} wall={wall}\n')
    print(f'{name} exit={r.returncode} wall={wall}', flush=True)
if __name__ == '__main__':
  n = sys.argv[1]
  jobs = [(c,a,n) for c in PROMPT for a in ('P0','P1','P2','P3')]
  with ThreadPoolExecutor(4) as ex: list(ex.map(lambda j: job(*j), jobs))
