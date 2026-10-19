# ROOTLINE OMNI — Revised Strategy: Recall + Live Graph Surgery

## Decision

Do not copy Lore and do not replace ROOTLINE with a generic multi-agent chatbot. Combine the strongest idea from Recall (shared, persistent graph memory and agent handoffs) with ROOTLINE's existing differentiator (isolated graph surgery and before/after counterfactual verification).

**Product:** ROOTLINE OMNI is a graph-grounded incident investigation agent that remembers prior investigations, coordinates bounded specialist roles through FalkorDB, and safely tests whether a dependency relationship changes the investigation outcome.

**Primary track:** Track 01 — Agents That Act on Connected Data, because the graph must change investigation/tool choices and the agent proposes a grounded action.
**Secondary track:** Track 02 — Agent Memory and Coordination, only if cross-session memory and graph-backed handoffs are genuinely implemented and demoed.
Do not claim Track 03 unless company-knowledge functionality is actually present.

The supplied Lore description is a reference for engineering quality, not a feature checklist to clone. Lore already demonstrates public-repository knowledge, explainable graph tools, memory, MCP, and backtesting. ROOTLINE's defensible distinction should be operational incident reasoning + counterfactual graph surgery + remembered outcomes.

## One-sentence pitch

“ROOTLINE OMNI investigates service incidents through FalkorDB, shows the exact evidence path behind each decision, safely rehearses dependency changes on an isolated graph, and remembers verified outcomes so the next investigation starts smarter.”

## Why this is a better direction

The product should have one coherent loop:
1. An engineer asks about a synthetic incident.
2. The investigator queries FalkorDB for incident, service, dependency, signal, and prior-investigation context.
3. A planner identifies the most important uncertainty.
4. A researcher selects and executes a graph-backed tool; its result must change what happens next.
5. A critic checks whether the proposed conclusion is supported by source IDs and graph paths and flags contradictions or missing evidence.
6. ROOTLINE proposes a reversible, human-approved next diagnostic action.
7. Live Graph Surgery tests one supported edge change in an isolated temporary graph, reruns the same investigation, and compares results.
8. The system verifies that the baseline graph was not modified and cleans up the temporary graph.
9. The investigation, selected tools, evidence, recommendation, operator decision, and counterfactual outcome are persisted in FalkorDB.
10. In a new session, a follow-up question retrieves the earlier investigation through graph queries and explains what it reused.

This is not “three chatbots.” The roles are bounded stages over shared graph state. They coordinate through FalkorDB, not by stuffing the full transcript into every prompt.

## Required anti-decoration proof

Build a judge-visible “graph dependency test”:
- Run a question and show retrieved memory plus a graph path.
- Demonstrate the actual Cypher/tool trace and evidence IDs.
- Disable/unavailable the graph memory connection in a controlled test.
- Show that cross-session recall and the related recommendation cannot be produced, and the app reports the missing dependency rather than quietly returning hardcoded output.
- Restore FalkorDB and repeat the follow-up successfully.

Never delete a production database or mutate the baseline graph to stage this test. Use a controlled test graph/configuration.

## Roles: keep it small

### Planner
Input: question, incident context, known evidence, prior investigations, remaining tool budget.
Output: next uncertainty and one allow-listed tool to call, with reason.

### Researcher
Executes one graph-backed tool at a time:
- `trace_dependencies`
- `expand_blast_radius`
- `inspect_evidence`
- `recall_prior_investigation`
- `simulate_dependency_change`
Each returns structured results and provenance. Tool choice must respond to the previous result; do not run a fixed theatrical sequence.

### Critic
Checks every material claim against evidence IDs and returned graph paths, separates observed facts from heuristics, catches contradictions, and can request one additional tool or mark the answer inconclusive.

If time is short, implement Planner → Researcher → Critic as three explicit functions/stages, not a heavyweight multi-agent framework. A deterministic policy is acceptable if transparent, bounded, stateful, and driven by live tool results. If an LLM is used, use structured outputs and allow-listed tool schemas; document which mode is active. No provider key must be required for the basic deterministic demo.

## Graph data model: minimal, traceable, queryable

Adapt to the existing schema; do not create duplicate competing models without need.

Core nodes:
- `Service`
- `Incident`
- `Signal`
- `Evidence`
- `Investigation`
- `AgentStep`
- `Recommendation`
- `OperatorDecision`
- `Memory` or `Finding` if needed

Core relationships:
- `(:Incident)-[:AFFECTS]->(:Service)`
- `(:Service)-[:DEPENDS_ON {criticality, ...}]->(:Service)`
- `(:Signal)-[:OBSERVED_ON]->(:Service)`
- `(:Evidence)-[:SUPPORTS]->(:Incident|:Service|:Recommendation)`
- `(:Investigation)-[:TARGETS]->(:Incident|:Service)`
- `(:Investigation)-[:USED_EVIDENCE]->(:Evidence)`
- `(:Investigation)-[:HAS_STEP]->(:AgentStep)`
- `(:Investigation)-[:PRODUCED]->(:Recommendation)`
- `(:OperatorDecision)-[:DECIDES_ON]->(:Recommendation)`
- `(:Investigation)-[:INFORMED_BY]->(:Investigation)` when a previous investigation was actually retrieved and reused.

Store enough to reconstruct why the agent chose a tool: step index, tool name, input summary, output summary, evidence IDs, timestamp, and outcome. Use stable IDs and idempotent seed/write operations. Never store secrets in the graph.

Memory layers:
- Episodic: completed investigations and their step traces.
- Semantic: services, dependencies, signals, evidence, and supported findings.
- Procedural: prior action/decision outcomes and critic verdicts, but only if those outcomes are recorded. Do not infer a successful action merely because it was recommended.

## Essential Cypher/query deliverables

Use parameterized queries compatible with the actual installed FalkorDB version; execute them against a running database and document their real output.

1. Seed synthetic service topology idempotently.
2. Load incident + affected services + linked evidence.
3. Trace upstream dependencies (bounded variable-length path).
4. Calculate downstream blast radius.
5. Retrieve evidence path and provenance for each claim.
6. Recall previous investigations sharing a service, incident type, dependency path, or evidence.
7. Persist investigation and agent-step records.
8. Retrieve persisted history from a fresh request/process.
9. Compare baseline and isolated counterfactual result.
10. Verify baseline topology invariant and temporary graph cleanup.
11. Store operator decision and later retrieve the outcome.

Do not rely on a Python dictionary, browser local storage, static JSON, or prompt history for “persistent memory.” FalkorDB must be the source of truth for cross-session recall.

## Live Graph Surgery: retain the existing differentiator

- Inspect the current implementation and verify whether the installed FalkorDB version supports the actual copy/clone operation being used. Do not assume `GRAPH.COPY` is available or safe without an integration test.
- If the copy mechanism is unavailable, use a separately named temporary graph populated from a deterministic topology snapshot and clearly document that implementation.
- Apply the chosen edge removal only to the temporary graph.
- Rerun the same investigation question and tool logic against the temporary graph.
- Show a real result diff: changed path/reachability/evidence/recommendation, as returned by the backend.
- Verify baseline topology before and after with a real query or deterministic signature.
- Always attempt temporary graph cleanup even if the investigation fails.
- Never claim baseline integrity passed unless the actual verification succeeded.
- Do not perform real production remediation. This is a synthetic isolated experiment.

## UI: serious agent control room, not a marketing dashboard

The product view should prioritize:
1. Question / incident input.
2. Agent timeline: current role, selected tool, reason, returned graph result, and what changed in the next step.
3. Evidence path graph: actual FalkorDB nodes and relationships, selected path highlighted, with a textual accessible alternative.
4. Evidence ledger: source ID, relationship/path, observed vs inferred, verified vs heuristic.
5. Action proposal: concrete next diagnostic step, rationale, cited evidence, risk, and human-approval requirement.
6. Live Graph Surgery: baseline and isolated graph side-by-side or a focused comparison, operation states, diff, cleanup and integrity verification.
7. Memory panel: prior investigation retrieved from FalkorDB, what was reused, what changed.
8. Trace export from real backend data.
9. Honest connection state and clear synthetic-data/limitations disclosure.

Design should be distinctive and restrained, with high-quality typography, intentional whitespace, precise alignment, restrained color, clear hierarchy, accessible contrast, and a real interactive graph. Avoid fake metrics, testimonials, stock AI art, random gradients, generic three-card layouts, excessive rounded pills, decorative terminal mockups, emoji icons, and false “live” indicators.

Use Motion for purposeful state changes:
- agent step transition,
- returned-path highlight,
- isolated edge removal,
- baseline/counterfactual diff,
- subtle panel transitions.
All animations must reflect actual backend events, respect `prefers-reduced-motion`, and avoid scroll-jacking or constant decoration.

## Skills to use in Antigravity

First inspect the current repository and read each installed skill's actual instructions. Do not migrate the current React/Vite + FastAPI architecture solely for fashion.

```powershell
cd "C:\Users\LENOVO\Downloads\ROOTLINE_OMNI_FINAL (1)\rootline"

npx ui-ux-pro-max-cli init --ai antigravity
npx skills add https://github.com/vercel-labs/agent-skills --skill vercel-react-best-practices
npx skills add https://github.com/vercel-labs/agent-skills --skill web-design-guidelines
npx motion-ai
```

Motion package, only if not already installed:
```powershell
cd frontend
npm install motion
```
React import: `motion/react`.

Confirm which skill files were actually installed. Do not claim “21 skills” unless the installed files/command output verifies it. Vercel deployment skill is optional and only relevant if the actual FastAPI + FalkorDB topology can be hosted correctly; frontend hosting alone is not a working deployment.

## Scope control

Do not rebuild everything. Previous project status reported 32 backend tests and a frontend build passing in a sandbox, but those do not verify Windows, Docker, `GRAPH.COPY`, browser behavior, remote GitHub state, or a final submission. Treat those checks as unverified until rerun in the actual workspace.

Preserve working code and tests. Start with `git status`, current branch/remote, `README`, `backend`, `frontend`, `tests`, `docker-compose.yml`, and `.gitignore`. Ensure `.env`, credentials, `.venv`, `node_modules`, and caches are never committed. Work in small commits; never force-push.

### Phase 0 — deadline check
The supplied Graph Hacks page stated a deadline of Oct 18, 2026 at 11:59 PM IST. Current date is after that. Check the portal before investing further; do not claim late submissions are accepted unless the portal confirms it. If closed, decide whether to continue for portfolio/learning purposes.

### Phase 1 — baseline audit
Run existing backend tests and frontend build. Check live FalkorDB health, actual endpoints, graph seed, graph schema, current Live Graph Surgery, current test coverage, and README accuracy. Preserve the last known passing baseline; do not trust old reports as proof of the current workspace.

### Phase 2 — graph-backed memory
Implement or verify a persistent investigation/step schema and Cypher read/write tools. Demonstrate memory retrieval in a new session or fresh process. Add tests.

### Phase 3 — bounded agent coordination
Implement Planner → Researcher → Critic with explicit structured state in FalkorDB. Add tool budget, duplicate/no-progress stop condition, and evidence/provenance validation. Demonstrate that a different graph result changes the next tool.

### Phase 4 — counterfactual correctness
Integration-test isolated graph creation, edge mutation, rerun, comparison, baseline invariant, and cleanup on success and failure. If the existing copy approach fails, use a safe temporary graph snapshot and document the exact behavior.

### Phase 5 — interface polish
Only after the agent loop works, design the UI around real traces and results. Install the design/performance/motion skills, implement purposeful animations, responsive layout, keyboard support, loading/error states, reduced motion, and synthetic data disclosure.

### Phase 6 — judge package
Update README and `docs/GRAPH_MODEL.md` with:
- problem and target user,
- primary and secondary track,
- why FalkorDB is essential,
- schema and key Cypher,
- agent loop and role boundaries,
- memory and coordination semantics,
- counterfactual isolation and safety,
- setup/deploy instructions,
- tests and reproducible demo,
- synthetic-data limits,
- AI assistant disclosure and the human decisions/contributions.

Provide a 2:30–3:00 video only after the whole workflow is live and reproducible. Do not fake successful runs in edited footage.

## Judge demo

0:00–0:15 — State the incident problem and explain that FalkorDB is the shared source of operational memory.
0:15–0:45 — Ask a seeded incident question; show real graph queries and evidence path.
0:45–1:15 — Show Planner/Researcher/Critic stages and a tool choice changing in response to actual graph results.
1:15–1:40 — Show recommendation with source evidence and human approval requirement.
1:40–2:05 — Run isolated Graph Surgery, show the changed result, cleanup, and baseline verification.
2:05–2:35 — Start a fresh session and ask a follow-up; show previous investigation retrieved from FalkorDB and the path supporting the answer.
2:35–3:00 — Show graph model/Cypher docs, tests, setup and honest limitations.

If a segment fails, fix it or omit it; never stage fake data as a successful result.

## Acceptance criteria

The build is ready to demonstrate only if:
- Core multi-hop investigation fails or explicitly degrades when FalkorDB is unavailable; no silent mock answers.
- The agent's next tool depends on actual graph/tool results.
- Every material claim includes graph/source evidence or is labeled uncertain.
- Persistent memory survives a new request/process and is queried from FalkorDB.
- Handoffs use graph state rather than transcript stuffing alone.
- Graph Surgery mutates only an isolated graph, verifies baseline integrity, and cleans up.
- UI displays actual run traces and paths.
- Tests/build/API checks were run and their exact results are recorded.
- README has schema, Cypher, setup, track declaration, demo and AI-use disclosure.
- No credentials or local dependency directories are committed.

## Final report requirements

Report only what was actually done:
1. Portal status.
2. Installed skill names and file paths.
3. Agent behavior demonstrated.
4. Cypher and graph schema implemented.
5. Test/build commands with actual output.
6. Graph Surgery integrity/cleanup results.
7. Demo and repository links.
8. Remaining gaps and what the participant must be able to explain.

Begin with the deadline check and repository audit. Implement the smallest complete end-to-end agent before adding polish. Do not stop after a plan, but do not claim access to or changes in the user's Windows workspace unless actually performed.
