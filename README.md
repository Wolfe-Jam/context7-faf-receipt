# context7-faf-receipt

A rerunnable test: with [Context7](https://context7.com) on, does a coding agent do better when the project's facts are written down in [`project.faf`](https://github.com/Wolfe-Jam/faf) (the IANA-registered `application/vnd.faf+yaml` format)?

91 runs of Claude Code across 13 small fixture repos, three rounds, every run published: transcript, check output and the patch it made. Results that didn't hold are reported next to the ones that did.

## The answer, short

- **When a fact exists only with the team** (what's next on the roadmap, where it deploys, which logger was chosen), the agent with Context7 alone **stopped and asked, or guessed: 0 of 9**. With the facts written down it **built the right thing: 9 of 9**, and asked Context7 for the docs of what the facts named (`/pinojs/pino-http`, uv's Docker guide).
- **The same facts in a hand-written CLAUDE.md also scored 9 of 9.** The difference comes from the facts being written down, not from the file format. `project.faf` is one way to write them: detected by `faf init`, confirmed by a person, scored, and synced into CLAUDE.md by `faf sync`. This test does not measure that part.
- **Library versions:** when the manifest pins a version, Context7 and the manifest already get it right without `project.faf`, even for SvelteKit 3.1 (released 2026-10-01). No version claim is made.
- **Monorepo and mid-migration repos:** with `project.faf` the agent made its first edit after fewer reads (0–1 against 4–5). Time and cost were the same.

## Setup

| | |
|---|---|
| Agent | Claude Code 2.1.326, headless (`claude -p --output-format stream-json`) |
| Model | `claude-sonnet-5-5`, fixed |
| MCP servers | Context7 remote MCP only (`--strict-mcp-config`) |
| Isolation | `--setting-sources project` (no user settings or plugins), `--disable-slash-commands` (no skills), WebSearch and WebFetch disallowed, fixtures outside the home folder, fresh auto-memory |
| Prompts | every prompt ends with `use context7`, in every arm |
| Tools allowed | Read, Glob, Grep, Edit, Write, Context7, and the one check command per case |
| faf-cli | 8.10.0 |

### Arms

| Arm | Repo contains |
|---|---|
| A | the code only |
| B | the code + `project.faf` at 100% + the CLAUDE.md that `faf sync` writes from it |
| A2 | the code + a hand-written CLAUDE.md with the same facts as B, no `project.faf` (round 3, three cases) |

Claude Code reads CLAUDE.md on its own and does not read `project.faf` unless asked, so arm B is what a developer gets from `faf init` + `faf sync`.

### What is counted

Fixed in [`cases.py`](cases.py) before any run: the check command (build, type-check or tests), the patterns that mean right and wrong, the Context7 libraries asked for, reads before the first edit, tool calls, tokens, cost, wall time.

## Results

### Round 1: three ordinary repos (1 run per arm)

SvelteKit 2 + Drizzle, axum 0.8 + sqlx, FastAPI + SQLModel. Both arms passed every check, resolved the right libraries and versions, and wrote nearly the same code. No difference.

### Round 2: ten edge cases (1 run per arm)

| Case | Edge | Result |
|---|---|---|
| svelte4 | Svelte 4 pinned | both correct |
| pydv1 | Pydantic 1.10 pinned | both correct |
| express5 | Express 5 routing | both correct |
| ormmig | Prisma → Drizzle migration | both correct (Drizzle); B fewer reads |
| rawsql | raw SQL, no ORM | both correct |
| monorepo | bun workspaces | both correct (run 2); B 0 reads before the first edit |
| internalui | own component library | both correct |
| dockeronly | deps only in the Dockerfile | both correct |
| intent | "add the next feature on our roadmap" | **A stopped and asked; B built orders** |
| gostd | Go stdlib only | both correct |

B asked Context7 for version-specific docs in three cases (Svelte v4, Express v5.1.0, Go 1.23). This did **not** hold in round 3.

### Round 3: signal cases and new edges (3 runs per arm)

| Case | A: Context7 only | B: + project.faf | A2: hand-written CLAUDE.md |
|---|---|---|---|
| intent | 0/3: stopped and asked | **3/3** built orders + tests | **3/3** |
| deploy (Cloud Run) | 0/3: stopped and asked | **3/3** Cloud Run Dockerfile on `$PORT` | **3/3** |
| logs (pino chosen) | 0/3: hand-written console logging | **3/3** pino-http | **3/3** |
| kit3 (SvelteKit 3.1) | 3/3 correct | 3/3 correct | — |
| svelte4, express5, gostd | correct; version-pinned docs in most A runs too | same | — |
| monorepo (reads before first edit) | 5, 1, 4 | 1, 1, 0 | — |
| ormmig (reads before first edit) | 5, 0, 5 | 0, 1, 0 | — |

Per-run numbers: `results/round*/summary.json`.

## Limits

- One model, one agent. Other agents and models may differ.
- Small fixtures built for this test; the team facts in them are fictional and consistent with the code.
- 1 run per arm in rounds 1–2, 3 in round 3.
- Bash file writes are not allowed in the runs. In round 2 one run (`monorepo-B-1`) changed nothing yet reported success; the check passed on the unchanged code. The pair was rerun (`monorepo-*-2`) and both runs are reported. From round 3 every arm gets one appended line: "Write and edit files with the Edit and Write tools, not with Bash."
- Arm B's CLAUDE.md is longer than A2's (140–151 words against 72–86) because of FAF's header and status lines.
- Transcripts have local paths replaced with `<rig>`, `<tmp>` and `~`.

## Rerun it

Needs Claude Code, a [Context7 API key](https://context7.com/dashboard) (free), bun, uv, Go and Rust. Cost at the time: about $0.10 a run.

```bash
cp c7-mcp.example.json c7-mcp.json            # put your key in it
(cd fixtures/svelte && bun install)           # install each fixture's deps (bun / uv sync / cargo build)
./run.sh svelte A 1                           # round 1: <repo> <A|B> <n>
python3 run2.py all 1                          # round 2: <cases|all> <n>
python3 run3.py intent,deploy,logs 1 runs3 A,B,A2   # round 3: <cases> <n> <out> <arms>
python3 analyze3.py --runs=runs3               # tables
```

`mkb.py`, `mkb2.py` and `mkb3.py` rebuild arm B (`faf init`, facts confirmed, `faf sync`) from arm A.

## Layout

```
fixtures/, fixtures-b/     round 1 repos (A, B)
cases/<case>/{A,B,A2}/     rounds 2–3 repos
prompts/                   round 1 prompts
cases.py                   rounds 2–3 prompts, checks, right/wrong patterns
run.sh, run2.py, run3.py   runners
analyze*.py                analyzers
mkb*.py                    arm B builders
results/round{1,2,3}/      transcript (.jsonl), check output, patch, summary per run
```

## Credits

Context7 is made by [Upstash](https://upstash.com). This test is independent and not endorsed by Upstash. The test was designed, built and run with Claude Code.

MIT licensed.
