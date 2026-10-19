# ROOTLINE OMNI — Graph Hacks Competition Rebuild Plan and Antigravity Execution Prompt

## Situation and objective

This repository must be treated as a serious hackathon engineering submission, not a graph-themed website. The existing application has been described as ROOTLINE OMNI, with React/Vite frontend, FastAPI backend, FalkorDB, synthetic service/incident/evidence seed data, and a Live Graph Surgery/counterfactual concept. Do not assume every feature works because a previous report says it does. Inspect the actual code and demonstrate each claim.

The supplied Graph Hacks brief states:
- FalkorDB must be the primary graph database and support a central product capability. A visualization laid over ordinary storage is not sufficient.
- The brief welcomes agents that act on connected data, agent memory/coordination, and company brain.
- Submissions require a public repository, README setup instructions and graph data model, Cypher queries or graph algorithms, demo video, live deployment or complete local instructions, and track declaration(s).
- AI coding assistants are allowed but must be disclosed. Entrants must understand and be able to explain code and technical decisions.
- Public, synthetic, or owned data is allowed; restricted/private data is not.
- The source states the submission deadline was October 18, 2026 at 11:59 PM IST. Current time appears to be after that deadline; before spending the night on polish, open the hackathon portal and determine whether submissions are still possible. Do not claim late submission is accepted without proof.

## Strategic correction: build an agent first, then its control room

The current concept risks looking like a dependency-graph viewer with an edge-removal demo. A strong entry must tell a judge, in a repeatable two-minute demonstration:
1. A real operational question arrives.
2. An agent constructs context from graph relationships in FalkorDB.
3. The graph changes the next tool/decision the agent selects.
4. The agent explains the exact graph paths/evidence behind the decision.
5. The agent proposes a bounded, explicit action or counterfactual experiment.
6. The app records the investigation and result to FalkorDB so a later session can reuse it.
7. A second query demonstrates persistent memory/learning from the previous investigation.
8. The judge can inspect the query, graph path, tool trace, action status, and limitations.

Do not add three unrelated mini-products just to claim all three tracks. Target Track 01 (Agents That Act on Connected Data) as the primary track. Evaluate Track 02 (Agent Memory and Coordination) as a secondary track only if persistent memory across sessions is genuinely implemented and testable. Do not claim Track 03 unless company knowledge entities/queries/actions are real. The submitted track list must match the implementation and the portal fields.

### Candidate product framing

**ROOTLINE OMNI — a graph-grounded incident response agent that investigates blast radius, chooses the next diagnostic action from connected evidence, tests an isolated counterfactual, and remembers verified incident outcomes.**

Concrete user: an on-call engineer responding to a synthetic microservice outage.

Primary question example:
“Checkout latency is spiking. What is the most likely upstream dependency path, what evidence supports it, what should I inspect next, and what would change if dependency edge X were unavailable?”

The system must distinguish:
- Observed synthetic signals/evidence
- Graph-derived relationships and paths
- Heuristic hypotheses
- Agent-selected next tool/action
- Counterfactual findings
- Persisted investigation memory

Avoid claiming this diagnoses real production telemetry. If all seeded data is synthetic, prominently identify it as a synthetic lab/demo.

## Critical FalkorDB test

Write and run a test that disables/blocks the FalkorDB adapter and demonstrates that graph-dependent investigation fails or materially loses required capabilities. The product must not be able to silently answer the core multi-hop question from prebuilt frontend data.

For every user investigation:
- Fetch nodes/relationships or paths from FalkorDB using actual graph queries.
- Use Cypher/graph traversal results as structured tool outputs to the agent policy.
- Make candidate tool selection or hypothesis ranking depend on those graph results.
- Persist the investigation/event/action and evidence provenance in FalkorDB.
- Retrieve that prior investigation for a follow-up query in a new session.
- Provide tests proving the graph materially influences output and memory persistence.

Do not simply render a graph after answering from hardcoded JSON. Do not add an LLM and call it an agent unless its tool loop actually observes results and chooses actions based on state. A deterministic bounded policy is acceptable and preferable under time constraints; it must still use state and tool feedback rather than following a hardcoded fixed sequence. If a real LLM provider is wired, use structured output and safe tool schemas; keep the app usable with a deterministic mode if API credentials are missing. Disclose clearly which mode ran.

## Core agent loop

Implement or verify this sequence using actual backend APIs and real FalkorDB queries:

1. **Parse intent**: normalize the incident/question and extract target service(s), symptoms, and desired output. Make the interpreted intent visible to the user.
2. **Read graph context**: query incident/service/dependency/evidence and prior-investigation memory. Prefer parameterized Cypher. Do not interpolate arbitrary user input into query strings.
3. **Build evidence ledger**: each claim includes source/evidence ID, node/edge/path, confidence/heuristic label, and verification state.
4. **Find graph gap**: identify what is still unknown (upstream dependency, shared dependency, affected downstream service, stale evidence, contradictory observations, previously attempted check).
5. **Choose next tool based on current state**: e.g. `trace_upstream`, `expand_blast_radius`, `inspect_evidence`, `lookup_prior_incident`, `simulate_edge_failure`. A policy must use current evidence coverage, graph topology, previous tool results and remaining budget to select the next action. Do not hardcode the same tool sequence for every query.
6. **Execute one bounded tool** and capture input, result summary, latency, and source paths.
7. **Verify**: validate paths/identifiers and separate observed data from inference. Do not treat model confidence as proof.
8. **Stop/continue governor**: fixed step/tool-call budget, duplicate-action guard, no-progress guard, contradiction guard. Stop when evidence is sufficient or explain why the run stopped.
9. **Action proposal**: produce one specific, reversible, human-approved action recommendation grounded in a graph path and evidence IDs. Do not auto-remediate or mutate production systems.
10. **Counterfactual sandbox**: for Live Graph Surgery, copy/use an isolated temporary graph through backend support, apply the selected edge removal only to that graph, rerun the same graph-dependent investigation, compare outcomes, verify baseline topology remains unchanged, and always clean up the temporary graph in a `finally`-style path. Report verified baseline integrity only after querying it.
11. **Persist memory**: record investigation, evidence links, chosen tools, action recommendation, operator decision, counterfactual summary, and timestamps in FalkorDB. Avoid duplicates with idempotency keys when appropriate.
12. **Follow-up test**: in a new session/request, ask “Have we investigated this dependency failure before? What did we learn and what action was chosen?” The result must come from stored graph memory.

If deadline forces scope reduction, complete one excellent end-to-end loop before adding advanced agent frameworks, multiple agents, MCP servers, or extra deployment infrastructure.

## Suggested graph data model to verify/adapt to code

Only use types that are genuinely persisted and queried.

Nodes:
- `Service {id, name, tier, owner, criticality}`
- `Dependency {id, kind, since}` only if a dependency must be an entity; otherwise use `DEPENDS_ON` edge properties.
- `Incident {id, title, status, severity, started_at}`
- `Signal {id, metric, value, unit, observed_at, source, synthetic}`
- `Evidence {id, statement, evidence_type, observed_at, source_ref, verified}`
- `Investigation {id, question, status, started_at, completed_at, mode}`
- `AgentStep {id, tool_name, input_summary, output_summary, latency_ms, step_index}`
- `Recommendation {id, action, rationale, risk, requires_approval, status}`
- `OperatorDecision {id, decision, actor_label, decided_at, note}`
- Optional `RunMemory {id, summary, created_at, last_used_at}` only if independently useful.

Edges:
- `(Incident)-[:AFFECTS]->(Service)`
- `(Service)-[:DEPENDS_ON {criticality, latency_ms, confidence, since}]->(Service)`
- `(Signal)-[:OBSERVED_ON]->(Service)`
- `(Evidence)-[:SUPPORTS]->(Incident|Service|Recommendation)`
- `(Investigation)-[:TARGETS]->(Incident|Service)`
- `(Investigation)-[:USED_EVIDENCE]->(Evidence)`
- `(Investigation)-[:HAS_STEP]->(AgentStep)`
- `(Investigation)-[:PRODUCED]->(Recommendation)`
- `(Investigation)-[:FOLLOWED_BY]->(Investigation)` only if the relation is real
- `(OperatorDecision)-[:DECIDES_ON]->(Recommendation)`
- `(Investigation)-[:INFORMED_BY]->(Investigation)` for retrieved prior cases where appropriate.

Create id constraints/indexes if supported and justified. Keep identifiers stable; avoid duplicate seed creation; make seeding idempotent. Document all essential graph queries in `docs/GRAPH_MODEL.md` or README.

## Graph query/algorithm deliverables

Verify these actual query/algorithm files exist and reflect production code; add them if missing:
- Seed: idempotently create synthetic demo graph.
- Incident context: identify affected service and known evidence.
- Upstream trace: parameterized variable-length traversal to discover dependencies.
- Blast radius: traverse dependency edges in reverse to find downstream dependents.
- Evidence paths: return concrete paths connecting signal → service → dependency → incident/recommendation.
- Prior memory: retrieve related investigations by shared service, dependency path, incident type, or evidence.
- Recommendation grounding: link each recommendation to one or more evidence IDs/paths.
- Counterfactual comparison: same question/algorithm against baseline and isolated graph.
- Integrity check: compare baseline topology fingerprints/counts or deterministic path signatures before/after and verify temporary graph cleanup.
- Persist result: store investigation, steps, evidence links, recommendation, approval state.
- Follow-up: retrieve saved result via graph relationships, not an in-memory Python dictionary.

Use actual FalkorDB/Cypher syntax compatible with the installed FalkorDB version. Run each query against a live local database; do not invent a successful query result.

## Product experience: an evidence-first incident command surface

The frontend is not a marketing homepage with decorative network graphics. The core workspace should let a judge inspect the agent’s work:
- **Question/incident command bar**: user asks a question or chooses one seeded scenario.
- **Agent run timeline**: current step, tool selected, why the policy selected it, what FalkorDB returned, and whether it changed the next step.
- **Evidence graph**: interactive, selectable, zoom/pan, fit view; labels/relationship directions; selected path is highlighted from returned graph path data.
- **Evidence ledger**: claims, source IDs, paths, evidence state, observed/inferred distinction.
- **Action recommendation**: concrete proposal, rationale, cited evidence, risk/impact and approval requirement; no fake production write.
- **Live Graph Surgery**: baseline vs isolated result, actual changed topology, diff, cleanup and baseline integrity.
- **Persistent memory panel**: prior investigation found by graph query, what was reused and what new information was added.
- **Trace export**: downloadable JSON/Markdown trace produced by backend data, useful for judge inspection.
- **System status**: real FalkorDB/API connectivity state, no fake green “live” indicator.
- Clear synthetic-data label, scope/limitations, AI-use disclosure.
- Accessibility: keyboard-operable graph alternative/details table, visible focus, labels, reduced motion, sufficient contrast, responsive layout and useful empty/error states.

The aesthetic should be a precise research/operations instrument with a distinctive editorial type system, space used intentionally, clear hierarchy, restrained ink/stone palette with a single controlled accent, honest data display, excellent tables and graphs. Avoid generic dashboard kit layouts, random blobs, purple gradients, fake activity feeds, fake logos, fake counts, stock people photos, giant blank hero, three-card template, emojis as UI icons, or animations with no semantic purpose.

Animation must amplify the product model:
- Orchestrated agent-step transition with clear step state.
- A short graph-path highlight when the backend returns a real path.
- Edge disappearance only within the confirmed isolated counterfactual graph.
- Smooth baseline/counterfactual comparison using Motion layout/variants.
- Subtle route/panel transitions and purposeful hover/focus feedback.
- Respect `prefers-reduced-motion`. Avoid scroll-jacking, cursor trails, endless floating particles, distracting page entrance effects.
- Do not animate false events. Visual animation must reflect actual API state.

## Skills and tooling to install in Antigravity

Use project-local/agent skills where supported. Inspect README/package.json first and don’t blindly switch the stack or add multiple animation libraries.

1. UI/UX Pro Max (supports Antigravity per repository docs):
   `npx ui-ux-pro-max-cli init --ai antigravity`
   Repository: https://github.com/nextlevelbuilder/ui-ux-pro-max-skill
   After installation, explicitly invoke the installed `ui-ux-pro-max` skill, run its design-system/search workflow for developer-tools/observability/infrastructure and select a coherent style/palette/type system. Do not trust the phrase “21 skills” without checking what the installed package actually installs; confirm installed skills and paths from command output.

2. Vercel skills:
   `npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-best-practices`
   `npx skills add https://github.com/vercel-labs/agent-skills --skill web-design-guidelines`
   If deploying to Vercel and appropriate:
   `npx skills add https://github.com/vercel-labs/agent-skills --skill deploy-to-vercel`
   Use the official docs: https://vercel.com/docs/agent-resources/skills
   Apply React performance rules and UI accessibility/performance review. Do not migrate a working Vite/FastAPI backend to Next.js purely for fashion. Vercel can host the frontend; the Python API and FalkorDB need a suitable reachable service or documented deployment architecture.

3. Motion:
   `npx motion-ai`
   Docs: https://motion.dev/docs/react
   If Motion React is not installed and React version supports it:
   `npm install motion`
   Import from `motion/react`. Keep graph rendering on an appropriate graph library; use Motion for state/panel/step transitions, not to rebuild a graph renderer from scratch.

4. Optional Vercel deployment CLI skill:
   Use only if the app architecture will actually be deployable to Vercel. Do not promise a production deployment before verifying backend/FalkorDB connectivity, secrets, CORS, persistence and health checks.

After installing, inspect generated skill files. Report exact names/paths. Never claim every advertised skill was installed unless the command output proves it.

## Work phases (execute, do not only write a plan)

### Phase 0 — submission gate
- Open the Graph Hacks portal immediately and determine whether the submission form accepts entries after the published deadline.
- If closed, don't misrepresent status. Continue only if a late submission, portfolio-quality build, or learning goal still makes sense.
- Save screenshots/records of the actual portal state; do not attempt to bypass restrictions.

### Phase 1 — audit current code and make a baseline
- `git status`, branch/remotes, `git log -5 --oneline`, `git ls-files`, inspect `.gitignore` and ensure `.env` stays ignored.
- Identify current repository root; confirm local `rootline` is linked to `https://github.com/shashankkumar8/ROOTLINE-OMNI.git`.
- Record baseline commands/results: pytest, frontend build, API health, FalkorDB health, seed counts, current primary routes.
- Verify actual code vs claimed reports. Don't trust test totals from pasted logs without rerunning.
- Document frontend components, API endpoints, graph schema, current query operations, and known gaps.

### Phase 2 — install skills and create a design system
- Install the named skills. Read their actual instructions.
- Search UI UX Pro Max recommendations and derive a written design system for this particular graph-investigation product.
- Create a UI review checklist based on Vercel web-design-guidelines and React best practices.
- Add Motion only as an intentional enhancement. If adding package dependencies, commit lockfile updates and test builds.

### Phase 3 — make FalkorDB central
- Add/verify query service and graph-dependent agent tools.
- Implement bounded dynamic tool loop; capture per-step trace.
- Add evidence and confidence semantics; don't mislabel heuristic scores.
- Persist investigation memory and retrieve it in a follow-up request.
- Verify graph outage materially degrades or blocks the core investigation rather than silently using hardcoded JSON.
- Ensure no unsafe arbitrary Cypher from model/user; tools are allow-listed and parameters validated.

### Phase 4 — Live Graph Surgery safety and correctness
- Use actual supported temporary graph/clone/isolated graph operations.
- Apply mutation only to isolated graph; run identical investigation; compute a real diff.
- Always cleanup; test failures during clone, mutate, rerun, compare, and cleanup.
- Verify baseline topology before vs after. Don't report PASS unless a real query/invariant check passed.
- If isolated graph copying is unsupported or unreliable, implement a safe alternative using a separate temporary graph populated from a deterministic topology snapshot. Document semantics exactly; never silently mutate baseline.

### Phase 5 — serious product UI
- Replace decorative landing page with evidence-first command surface.
- Agent event timeline, graph path, evidence ledger, proposed action and memory must be actual API-backed.
- Add Motion interactions tied to real states and honor reduced motion.
- Give graph a readable alternate table/details view.
- Add proper loading/error/offline state; no fake live labels or mock fallback behind failures.
- Add real Privacy/Terms if needed, synthetic-data disclosure and AI-use disclosure.

### Phase 6 — testing
Add automated tests for:
- Cypher/query correctness against live FalkorDB (integration tests labeled clearly).
- Graph results influence agent action choice.
- Agent changes next tool based on different graph states.
- Evidence IDs and paths are preserved in recommendation.
- Follow-up memory works across a new request/session (not just process memory).
- Duplicate/no-progress/budget stop conditions.
- Counterfactual changes only temp graph.
- Baseline integrity remains unchanged.
- Temporary graph cleanup on success and exceptions.
- No graph connection means explicit bounded error/no silent mock answer.
- API contracts, invalid input, auth/approval controls where applicable.
- API/Frontend builds, accessibility basics, reduced motion, deep-linked routes.

Run everything in project’s documented environment; report commands and exact pass/fail. Do not weaken tests to pass.

### Phase 7 — judge-grade packaging and demo
- Update README with problem, target user, track declaration, why graph is essential, graph schema, core Cypher, agent loop, memory semantics, safety model, setup, environment examples, commands, architecture diagram, tests, deployment topology, limitations and AI-assistant disclosure.
- Include a `docs/JUDGE_WALKTHROUGH.md` with question prompts, expected tool timeline, expected graph paths, what to inspect, and failure handling.
- Include an architecture diagram. Prefer Mermaid source plus rendered image if easy.
- Build reproducible synthetic seed fixtures. Provide exact Docker Compose startup and shutdown instructions.
- Ensure ZIP contains source/docs but excludes `.env`, secrets, `.venv`, `node_modules`, caches and data not permitted by the rules.
- Prepare a 2:30–3:00 demo only after the live flow works. Don't edit together fake successful states.

## Three-minute judge demo script (only use if implementation truly supports it)

0:00–0:20 — State the operational problem: graph context prevents the agent from reasoning about dependencies in isolation.
0:20–0:45 — Submit a known incident question; show parsed goal and live FalkorDB status.
0:45–1:20 — Watch the agent choose one query/tool based on current graph state, inspect actual Cypher/return summary and an evidence path. Then show the returned result changes the next tool choice.
1:20–1:50 — Show a recommendation grounded in concrete evidence IDs/paths, with human approval required.
1:50–2:20 — Run Live Graph Surgery on an isolated graph; show edge removal, repeated query, real before/after result, temp cleanup and baseline invariance.
2:20–2:40 — Start a new request/session and demonstrate prior investigation memory retrieved from FalkorDB.
2:40–3:00 — Show README/model/query docs and state honest limitations/synthetic data/AI disclosure.

If any stage doesn't work, fix it or omit it. Don't fake outputs on the screen.

## Commands and local environment
Use PowerShell in:
`C:\Users\LENOVO\Downloads\ROOTLINE_OMNI_FINAL (1)\rootline`

Before doing the full work, run:
```powershell
git status
git remote -v
Get-Content .gitignore
Get-ChildItem frontend -Force
Get-Content frontend\package.json
Get-Content docker-compose.yml
```
Do not overwrite local work or the remote branch with `git push --force`. Keep secrets excluded. Commit in small coherent changes after tests:
- `feat(agent): add graph-grounded investigation loop`
- `feat(memory): persist investigation context in FalkorDB`
- `feat(counterfactual): verify isolated graph surgery`
- `feat(ui): build evidence-first incident command surface`
- `docs: document graph model, tracks, setup and AI use`

## Acceptance criteria

Do not announce “winner-level”, “production-ready”, “all tests pass”, or “deployed” unless there is concrete evidence. Aim for a technically defensible, judge-reproducible build that:
- Cannot perform its main analysis without FalkorDB graph context.
- Uses an agent policy or LLM tool loop with real feedback.
- Produces traceable decisions and graph evidence.
- Persists and reuses investigation memory.
- Has a safe, genuinely isolated counterfactual experiment and baseline-invariant check.
- Provides a polished UI that exposes actual reasoning and evidence, not fake numbers.
- Works from a fresh clone following README.
- Has tests, queries, graph model, demo, track declaration and AI disclosure.
- Is honest about synthetic data and what remains incomplete.

## Final report to user
Return:
1. Whether portal accepted/closed.
2. Exact skills installed and paths.
3. Actual product behavior implemented (not planned items).
4. Graph queries and graph schema.
5. Test/build commands and actual results.
6. Demo and repo paths.
7. What the user must personally understand/be able to explain.
8. Remaining blockers; no fabricated metrics or guarantees.

Begin by checking the submission portal and auditing the existing code. Then implement in the same working tree. Do not stop at a plan, but do not pretend to have direct filesystem access to the user's Windows workspace.
