# ROOTLINE OMNI — Final Track 01 Engineering Plan
## Reviewed against Graph Hacks brief, organizer reference article, and the supplied implementation draft

**Decision:** Upgrade the existing ROOTLINE OMNI repository. Do not start from scratch.
**Track:** Track 01 — Agents That Act on Connected Data.
**Core product:** A graph-grounded incident investigation agent that traces multi-hop dependencies, selects safe predefined tools based on observed results, tests a proposed intervention using isolated counterfactual graph surgery, and explains the evidence behind its recommendation.

This is an engineering plan, not a claim that the current code already implements everything below. Verify each phase in the actual workspace before describing it as complete.

---

## 1. Why Track 01 is the best fit

The existing ROOTLINE project already has the right problem domain: incident investigation over service dependencies, contradictory evidence, blast-radius traversal, saved decisions, and Live Graph Surgery. These are naturally graph-dependent and align directly with Track 01's focus on multi-hop reasoning, graph queries and algorithms as tools, tool selection through MCP, actions based on graph evidence, and explainable results.

Do not dilute the submission by trying to fully compete in all three tracks. Company ownership information may be included only where it directly improves incident routing. Persistent memory may support prior investigation context, but do not claim Track 02 as a second entry unless it is actually complete and deliberately selected.

## 2. Non-negotiable product story

A judge gives ROOTLINE a service incident. The agent:

1. Resolves incident and service references against FalkorDB, rejecting unknown entities.
2. Chooses from a fixed catalogue of human-authored tools; it never invents arbitrary Cypher.
3. Traverses multi-hop service dependencies and inspects supporting and contradicting evidence.
4. Uses graph algorithms only when supported by the installed FalkorDB version, reporting the actual algorithm used or a clearly named fallback.
5. Returns a ranked cause or abstains when evidence is insufficient.
6. Tests a proposed edge-level intervention on an isolated temporary graph, compares before/after topology, verifies the original graph is unchanged, and cleans up the temporary graph even on errors.
7. Returns the exact graph paths, supporting evidence IDs, tool trace, uncertainty, blast radius, and a human-reviewable action proposal.
8. Persists an approved decision/action only after an explicit human action; no real infrastructure is changed by the demo.

The graph must alter the result. If the graph is removed, graph-only tools and cross-node path evidence must be unavailable, not silently replaced by the same graph answer.

## 3. Critical audit of the supplied draft

### A. Hardcoded “agent” sequence
The draft uses keyword checks and then runs a mostly fixed tool sequence. That can be a useful deterministic baseline, but it is not proof of adaptive tool selection. Replace it with a bounded state-driven loop:
- Observe the user request and resolve known entities.
- Select one tool from a fixed registry using validated arguments.
- Execute it and inspect the actual structured result.
- Choose the next tool based on that result and the remaining question.
- Stop on a clear answer, unknown entity, disconnected path, insufficient evidence, or maximum step budget.
- Record actual tool timings and decisions; never invent latency values.
If no LLM provider is configured, label the selector as a deterministic policy, not an autonomous LLM agent. The project can still be graph-native and technically strong.

### B. Fake ablation benchmark
Do not hardcode the graph-free baseline as wrong. Build a reproducible evaluation:
- A versioned set of synthetic labeled incident cases, including known cause, ambiguous/inconclusive case, disconnected graph case, and unknown entity.
- Mode A: the normal graph-backed tools.
- Mode B: a genuinely graph-removed baseline that receives only the permitted flat incident facts, without dependency edges or graph-derived paths.
- Run both modes over identical cases and prompts.
- Compute accuracy, abstention correctness, unknown-entity rejection, and path-grounding rate from actual outputs.
- Display sample count and per-case outputs. If the baseline is intentionally simple, call it a baseline, not a representative of all LLMs.
- Never hardcode `0%`, `100%`, or a favorable result. If a mode fails, show the failure.

### C. Fake grounding
`grounding_verified=True` must be computed, never assigned as a constant. The verifier should:
- Receive the exact structured tool outputs used for the answer.
- Extract entity IDs and evidence IDs cited in the answer object.
- Confirm every cited service, incident, team, runbook, evidence item, and path edge exists in those outputs or is independently verified against FalkorDB.
- Verify each consecutive pair in a returned path corresponds to an actual directed edge in the relevant graph snapshot.
- Return `verified_entities`, `unsupported_entities`, `verified_edges`, and `grounding_verified`.
- On failure, suppress the unsupported claim and downgrade the result to an explicit uncertainty/abstention state.

Prefer structured answer fields and evidence references over trying to validate arbitrary prose with fragile substring matching.

### D. Native algorithm claims
Do not assume `CALL algo.pageRank`, `CALL algo.SPpaths`, `CALL algo.betweenness`, or `CALL algo.WCC` are available with the exact signature in the installed image. Before coding them:
1. Record the FalkorDB server image/version and Python client version.
2. Run minimal read-only smoke queries for each procedure on a tiny test graph.
3. Save the verified syntax and output shape in tests/docs.
4. Implement a fallback only where useful, and return truthful metadata such as `engine_used="native_page_rank"` or `engine_used="cypher_degree_fallback"`.
5. Do not call a traversal a native PageRank or shortest-path algorithm if it is not one.
Use parameterized values. If a hop bound must be inserted as a Cypher literal, clamp it to a small integer allowlist before interpolation; never interpolate arbitrary user input.

### E. MCP is more than a tools list
A `GET /api/mcp/tools` endpoint can be useful for UI inspection, but it is not by itself a complete MCP server. Either:
- implement and test the actual MCP transport and protocol methods you claim, including tool discovery and tool invocation with valid JSON-RPC requests; or
- label the component honestly as an internal structured tool registry/API and do not claim full MCP compliance.
Keep one source of truth for tool names, schemas, argument validation, and handlers.

### F. Unsafe counterfactual assumptions
Do not assume `GRAPH.COPY` or its client wrapper is available/behaves identically in every installed version. Use the official client method only after a smoke test. A safe surgery operation must:
- Create a unique temporary graph name not accepted from arbitrary user input.
- Capture baseline node/edge counts and a stable representation/hash of relevant topology.
- Verify the target edge exists with the expected direction before removing it.
- Perform the edge removal and rerun the same query in the clone.
- Compare before/after outcomes.
- Recheck the baseline topology after the experiment.
- Delete the temporary graph in a `finally` path and verify cleanup.
- Return a failed/unknown status if any assertion fails. Never report `baseline_unchanged=true` merely because no exception was thrown.
- Do not execute production rollback/circuit-break actions. Demo actions are proposed or recorded after human approval only.

### G. Entity resolution flaws
Avoid keyword-specific hacks such as checking only for "postgres", "mongodb", or "billing-legacy". Resolve names against graph nodes with:
- exact ID/name match first;
- a small explicit alias table validated against existing nodes;
- optional fuzzy candidates with a conservative threshold, returning suggestions rather than silently picking an ambiguous match.
An unknown entity must stop the relevant tool flow. It must not continue with a default service.

### H. Hidden hardcoded values and silent exception handling
Remove invented defaults for owner, team, runbook, path, or action when graph results are missing. Return `missing_data` or `inconclusive` instead. Do not swallow broad exceptions in seed/enrichment code; surface an error and fail tests when required nodes are absent.

### I. Tenant graph isolation
Multi-tenant graph selection is not required for the selected Track 01 scope. If retained, sanitize and validate tenant IDs, select the graph once, and pass that graph object into every tool. Never return to `get_graph()` inside a tenant-specific call. Add cross-tenant isolation tests. Otherwise defer it to avoid scope expansion.

### J. UI claims
Every panel must be driven by real API data. No hardcoded green status badges, fake millisecond timings, fake benchmark percentages, simulated tool outputs, or pretend “live” traces. Motion should animate actual query paths and operation states. Use restrained, intentional transitions, accessible focus states, reduced-motion support, loading skeletons, empty/error states, and responsive layouts. Avoid generic AI gradients, emoji icons, fake metrics, testimonials, or decorative graph visualizations that do not correspond to the backend.

---

## 4. Recommended architecture

### Backend modules
- `backend/investigator.py`: preserve the existing incident scoring and evidence logic.
- `backend/queries.py`: human-authored, parameterized Cypher query functions.
- `backend/surgery.py`: isolated copy/modify/compare/cleanup operation with invariants.
- `backend/track1_agent.py`: bounded state-driven agent policy/loop, entity resolution, structured outcomes, grounding verifier.
- `backend/mcp_tools.py`: one fixed tool registry with JSON schemas, validation, and dispatch; implement actual MCP protocol only if explicitly supported.
- `backend/algorithms.py`: version-verified native algorithms plus truthful fallbacks.
- `backend/benchmark.py`: repeatable graph-vs-flat baseline evaluation using labeled cases.
- `backend/main.py`: thin API routes; preserve existing routes.
- `tests/`: unit, integration, failure-path, and regression tests.

### Fixed tool catalogue (recommended)
1. `triage_incident_with_evidence(incident_id)`
2. `multi_hop_blast_radius(service_id, max_hops)`
3. `shortest_dependency_path(source_service_id, target_service_id)`
4. `graph_algorithms_suite(algorithm, optional scope)`
5. `verify_action_by_graph_surgery(incident_id, source_service_id, target_service_id)`
6. `resolve_owners_and_runbook(service_id)`

Each tool returns a stable structured shape:
- `tool`
- `status` / `outcome`
- `arguments_resolved`
- `data`
- `paths`
- `evidence_ids`
- `cypher_id` or safe query label (do not expose secrets)
- `engine_used`
- `duration_ms`
- `errors` when applicable

Use consistent outcomes, at minimum:
- `answered_with_path`
- `not_in_graph` (known nodes, no relevant path)
- `unknown_entity` (node does not exist)
- `inconclusive` (evidence insufficient or conflicting)
- `tool_error` (execution/engine failure)
A memory-specific outcome is not required for Track 01; if prior investigation memory is shown, it must be genuinely persisted and retrieved.

### API surface
Preserve existing API routes. Add only what the frontend needs:
- `GET /api/health`
- `GET /api/mcp/tools` (only if this is the actual tool registry or a documented protocol facade)
- `POST /api/mcp/call` (validated tool dispatch; do not expose arbitrary Cypher)
- `POST /api/agent/act`
- `GET /api/algorithms`
- `GET /api/benchmark`
- `POST /api/agent/execute-action` (optional; persist a proposed/approved demo action, never operate real infrastructure)

Do not add all endpoints blindly. Reuse existing routes when possible and document exact request/response schemas.

---

## 5. Execution phases and acceptance criteria

### Phase 0 — Freeze and audit
1. Check `git status`; commit or branch the current working state before editing.
2. Confirm repository root and remote. Never run `git add .` before reviewing `.env`, credentials, generated bundles, `.venv`, `node_modules`, caches, and ZIPs.
3. Run existing tests and frontend build before changing code.
4. Record actual pass count, failures, versions, running port, and Docker container.
5. Inspect current graph schema, queries, surgery code, and API routes. Avoid duplicate modules/endpoints.

**Gate:** a known baseline report and recoverable Git state exist.

### Phase 1 — Graph correctness and entity guardrails
1. Implement exact/alias entity resolution from graph results.
2. Parameterize user values and clamp traversal depth.
3. Ensure all read-only diagnostic tools use `ro_query()` when supported; fail explicitly if read-only enforcement is required but unavailable.
4. Return paths and evidence IDs from the same query/graph snapshot used for the result.
5. Add unknown entity, disconnected path, invalid incident, and no-evidence tests.

**Gate:** no default-service fallback, no fabricated paths, and tests prove correct outcome shapes.

### Phase 2 — Tool registry and adaptive agent loop
1. Create a fixed registry of validated tool schemas and handlers.
2. Implement a bounded loop (for example, maximum 5 tool calls) that chooses its next tool from prior structured results.
3. If an LLM provider is used, keep tool selection constrained to the registry and validate every proposed argument. If no provider is configured, label the policy as deterministic rather than pretending an LLM made the choice.
4. Record actual tool invocation, input, result summary, timing, and next-step rationale.
5. Add tests showing that changing a graph edge or tool result changes the next decision or final result.

**Gate:** the graph changes a meaningful decision; trace data is generated from execution, not hardcoded.

### Phase 3 — Native graph algorithms
1. Verify the algorithms supported by the installed server.
2. Test each supported procedure against a small known graph with known expected ordering/path.
3. Add truthful native/fallback metadata and tests for both success and unsupported-procedure paths.
4. Use algorithms as agent tools only where their output informs the incident decision or impact analysis.

**Gate:** no false claim of native algorithm execution.

### Phase 4 — Live Graph Surgery hardening
1. Test the installed client's graph copy API.
2. Add unique clone naming, edge-existence validation, topology snapshots, invariant assertions, and `finally` cleanup.
3. Test clone creation failure, edge missing, query failure, cleanup failure, and baseline mutation detection.
4. Return a verified result only when all required invariants pass.
5. Keep real remediation out of scope; require human approval for any persisted demo action.

**Gate:** failure paths are safe and no test leaves temporary graphs behind.

### Phase 5 — Honest ablation benchmark
1. Create at least 10 deterministic synthetic cases if time permits, including positive, contradictory, ambiguous, disconnected, and unknown-entity cases.
2. Label expected outcome and valid supporting paths before running evaluation.
3. Run the same cases in graph mode and a real flat/no-edge baseline.
4. Compute metrics from actual outputs: cause accuracy, abstention correctness, unknown-entity rejection, path grounding, and tool errors.
5. Show the cases and raw per-case outputs. Never hardcode the graph-free score.

**Gate:** benchmark is repeatable and reproducible; results may be imperfect but are honest.

### Phase 6 — Frontend redesign
Use the installed UI/UX Pro Max, Vercel React Best Practices/Web Design Guidelines, 21st.dev components where they genuinely help, and Motion only after checking installation and compatibility.

Build one cohesive “Incident Command” workspace:
- Header with explicit Track 01 and live backend/database connection state.
- Main prompt input with scenario chips.
- Evidence-backed investigation summary and outcome.
- Interactive dependency graph whose highlighted path is the exact backend-returned path.
- Tool trace panel with actual tool names, durations, result counts, and expandable safe query text.
- Blast-radius comparison.
- Counterfactual before/after diff and verified invariants.
- Grounded owner/runbook/action proposal with explicit approval.
- Benchmark panel with measured per-case results.
- Strong loading, empty, error, and disconnected-database states.

Design rules:
- Avoid purple gradients, fake metrics, fake testimonials, decorative-only graphs, emoji icons, excessive cards, and unnecessary scroll animations.
- Use a restrained dark operations-console visual system, clear typography, spacing, subtle borders, and high contrast.
- Support keyboard navigation, visible focus, reduced motion, mobile widths, and accessible status labels.
- Every button must perform a real API action or be removed.

**Gate:** a judge can run the primary scenario without reading documentation, and every displayed claim traces to backend data.

### Phase 7 — Verification and submission packaging
Run and record:
1. `python -m pytest -q`
2. `npm run build`
3. API smoke tests for health, investigation, tool list/call, algorithms, benchmark, and surgery.
4. Fresh database seed and repeat-run idempotence.
5. Manual UI run against the actual Docker FalkorDB instance.
6. Git secret scan and `git status`.
7. README review: setup, graph schema, key Cypher, tool catalogue, algorithm/fallback behavior, tests, demo steps, limitations, and truthful AI-assistance disclosure.
8. Rebuild ZIP only after final tests; exclude `.env`, credentials, `.venv`, `node_modules`, `.git`, caches, and stale generated artifacts.
9. Push only after reviewing the exact staged diff.

**Gate:** all claims in the README and demo match the tested implementation.

---

## 6. Recommended demo (about 2:30–3:00)

1. **0:00–0:20 — The problem:** Show a checkout incident with a misleading recent payment deployment.
2. **0:20–0:55 — Graph-dependent reasoning:** Run the agent, show its actual tool choices, multi-hop path to the cache dependency, contradictory canary evidence, and why the graph changed the conclusion.
3. **0:55–1:20 — Depth and algorithms:** Compare direct vs. multi-hop blast radius; show only algorithms verified on the running FalkorDB image.
4. **1:20–1:55 — Counterfactual:** Copy the graph, remove a validated edge, rerun the same query, compare results, verify baseline invariance, and show temporary graph cleanup.
5. **1:55–2:20 — Guardrails:** Try an unknown service and an ambiguous/insufficient-evidence case; show refusal to guess.
6. **2:20–2:45 — Measured ablation and proof:** Show actual per-case benchmark outputs, passing tests, architecture/README, and GitHub repository.

Do not claim production remediation, real telemetry, or broad accuracy from a tiny synthetic dataset.

---

## 7. Immediate Antigravity instruction

Paste this first; do not paste a massive rewrite prompt yet:

> **ROOTLINE OMNI — Track 01 audit only. Do not edit files yet.**
>
> Inspect the existing repository and report:
> 1. Current Git root, branch, remote, and working-tree state.
> 2. Actual existing tests and exact test pass count.
> 3. Existing FastAPI routes and frontend API base/proxy.
> 4. Current graph schema and key Cypher queries.
> 5. Exact Live Graph Surgery implementation, supported copy/delete APIs, and all failure/cleanup paths.
> 6. Installed FalkorDB server and Python client versions, and smoke-test results for the native algorithms the current version supports.
> 7. Which proposed capabilities already exist, are partial, or are missing.
> 8. Any hardcoded values, fake timings, fabricated benchmark scores, default entities, broad exception swallowing, or hardcoded grounding flags.
> 9. Secret/packaging risks, including `.env`, ZIP files, caches, `.venv`, and `node_modules`.
>
> Return a prioritized audit with file paths and evidence. Do not claim a feature works unless you ran a test or inspected the implementation. Do not install packages, alter files, commit, push, or submit during this audit.

After the audit, implement one phase at a time and rerun the gates. Do not ask Antigravity to “make it a winner” or promise zero cons; require evidence and test output.

## 8. Final decision

**Upgrade ROOTLINE OMNI, do not start over.** Make the incident agent and graph surgery correct first, then add the bounded tool loop, verified algorithms, honest benchmark, and polished interface. Choose Track 01 only. The project's strongest competitive argument is not the number of features: it is a reproducible demonstration that the graph changes the agent's decision, that the answer's path is verifiable, and that the counterfactual experiment leaves the baseline graph untouched.

The official deadline shown in the supplied brief was October 18, 2026 at 11:59 PM IST; the current date is October 19, 2026. Check the submission portal for any extension before assuming the entry can still be submitted.
