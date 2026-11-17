import subprocess, sys, pathlib, shutil, time
from concurrent.futures import ThreadPoolExecutor
W = pathlib.Path(__file__).parent
PROMPT = {
 'logs':    'Add request logging and log any unhandled errors. Make sure `npm test` passes. You can add dependencies.',
 'storage': 'Store the file metadata so it survives a restart, and add an endpoint that lists the stored files. Make sure `npm test` passes. You can add dependencies.',
}
def job(agent, case, arm, n):
    name = f'{agent}-{case}-{arm}-{n}'; d = W/'runs'/name
    if d.exists(): shutil.rmtree(d)
    subprocess.run(['cp','-c','-R', str(W/'fixtures'/case/arm), str(d)], check=True)
    if agent == 'codex':
        (d/'opencode.json').unlink(missing_ok=True)
        cmd = ['codex','exec','--json','--skip-git-repo-check','--ephemeral','--ignore-user-config','-s','workspace-write','-c','sandbox_workspace_write.network_access=true','-C',str(d),PROMPT[case]]
    else:
        cmd = ['opencode','run','--format','json','--model','opencode/big-pickle','--dir',str(d),PROMPT[case]]
    t0 = time.time()
    with open(W/'runs'/f'{name}.jsonl','w') as o, open(W/'runs'/f'{name}.err','w') as e:
        try: subprocess.run(cmd, cwd=d, stdout=o, stderr=e, stdin=subprocess.DEVNULL, timeout=900)
        except subprocess.TimeoutExpired: e.write('\nTIMEOUT\n')
    wall = round(time.time()-t0)
    r = subprocess.run('npm test', shell=True, cwd=d, capture_output=True, text=True, timeout=600)
    (W/'runs'/f'{name}.check').write_text(r.stdout[-2000:]+r.stderr[-2000:]+f'\nexit={r.returncode} wall={wall}\n')
    print(f'{name} exit={r.returncode} wall={wall}', flush=True)
if __name__ == '__main__':
    agent = sys.argv[1]
    jobs = [(agent,c,a,n) for n in range(1,6) for c in PROMPT for a in ('P0','P1','P2','P3')]
    with ThreadPoolExecutor(4 if agent=='opencode' else 3) as ex: list(ex.map(lambda j: job(*j), jobs))
