# ROOTLINE OMNI — Track 01 Detailed Implementation Guide

**Goal:** Turn the existing ROOTLINE OMNI starter into a credible, graph-native incident investigation agent, with a premium UI and verifiable engineering claims.

**Guiding rule:** Audit first, then work in small phases. Preserve working code. Treat all “production-ready”, “zero-cons”, fixed accuracy, and “causal proof” claims in Gemini's original proposal as unverified until demonstrated by tests against the actual workspace and server.

## 1. Recommended implementation order

1. Workspace audit and rollback.
2. Live FalkorDB connection, schema, and repeatable seeding.
3. Investigator and scoring correctness.
4. Entity resolution and structured grounding.
5. Bounded observation-driven agent loop.
6. Native algorithm compatibility and honest fallbacks.
7. Isolated graph surgery, invariants and cleanup.
8. Fair graph-versus-flat baseline evaluation.
9. Internal tool API or a real MCP protocol implementation—choose and label accurately.
10. Premium React UI built around real API responses.
11. Automated tests, browser journey, README and release audit.

Don't redesign the UI first. Don't paste one of the overlapping Gemini agent drafts on top of the current source without reviewing its schema and routes.

## 2. Research grounding: what is supported

### Think-on-Graph (ToG), ICLR 2024
Paper: https://proceedings.iclr.cc/paper_files/paper/2024/hash/10a6bdcabbd5a3d36b760daa295f63c1-Abstract-Conference.html

Useful idea: iterative graph exploration and beam-search path selection. ROOTLINE can adapt the principle by resolving entities, inspecting one-hop candidates, retrieving evidence, pruning contradictory/weak candidates, selectively expanding, and returning grounded paths. If the selector is deterministic, describe it as a bounded observation-driven policy—not a full LLM implementation of ToG.

### Reasoning on Graphs (RoG), ICLR 2024
Paper: https://proceedings.iclr.cc/paper_files/paper/2024/hash/3e2aeb66481dd63a32421bf032b70384-Abstract-Conference.html
Official implementation: https://github.com/RManLuo/reasoning-on-graphs

Useful idea: reasoning should be grounded in retrieved relation paths. Make the answer structured and verify every node, edge and evidence reference before displaying the conclusion. This is design inspiration, not proof ROOTLINE reproduces RoG's entire learned pipeline.

### MicroRCA, IEEE/IFIP NOMS 2020
Paper: https://doi.org/10.1109/noms47738.2020.9110353
Reference implementation: https://github.com/elastisys/MicroRCA

Useful idea: root cause localization considers anomaly propagation and correlated service/resource behavior. ROOTLINE's heuristic may combine support, contradictions, hop distance, and deployment recency. Do not equate a small synthetic heuristic with the original MicroRCA method or call scores probabilities unless calibrated.

### FalkorDB Python client
Client: https://github.com/falkordb/falkordb-py
Documentation: https://falkordb-py.readthedocs.io/en/stable/falkordb.html

The official client documents `graph.ro_query(...)`, `graph.copy(...)`, and graph deletion. Still run smoke tests against the exact installed client and Docker image before assuming graph algorithm procedures/signatures or clone cleanup behavior.

### MCP
Tools specification: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/server/tools.mdx
Schema: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/2025-06-18/schema/2025-06-18/schema.ts

A tool list endpoint is not a complete MCP server. Either implement the protocol lifecycle, schemas, JSON-RPC behavior and supported transport, or call the feature an internal structured tool registry/API.

### Graph surgery terminology
Removing a dependency from a clone and observing changed results is a **counterfactual topology experiment**. It is not proof of real-world causality without an explicit causal model and assumptions. Prefer `ranking_delta_after_edge_removal` to `causal_effect`.

## 3. Phase 0 — audit before editing

PowerShell:

```powershell
cd "C:\Users\LENOVO\Downloads\ROOTLINE_OMNI_FINAL (1)\rootline"
git status --short
git branch --show-current
git log -5 --oneline
python --version
node --version
npm --version
docker ps
.\.venv\Scripts\Activate.ps1
python -m pytest -q
```

Second terminal:

```powershell
cd "C:\Users\LENOVO\Downloads\ROOTLINE_OMNI_FINAL (1)\rootline\frontend"
npm run build
```

Save actual output. Do not assume any previously reported test count still applies. Record the Docker image tag, connection configuration, schema, API routes, Git changes and existing features.

**Gate:** baseline tests/build complete or failures accurately recorded; a rollback point exists.

## 4. Phase 1 — graph correctness and seed

- Verify the app reaches the expected FalkorDB graph.
- Run seeding twice and confirm node/edge counts do not double.
- Inspect real labels, relationship types and property names before writing Cypher.
- Use parameterized values. If a variable-length path requires an interpolated hop bound, clamp the value to a small integer allowlist before query construction.
- Require native read-only queries for diagnostics. If `ro_query` is unavailable, fail closed; don't fall back to a mutating query and still call it read-only.
- Smoke-test an incident lookup, one-hop traversal, multi-hop traversal, evidence lookup and unknown ID.

**Gate:** observed paths/IDs match known seeded fixtures on the actual graph server.

## 5. Phase 2 — deterministic investigator

A documented score might have this form:

`score = supporting_evidence - contradiction_penalty + recency_prior - distance_penalty + optional_structural_prior`

These are example components, not calibrated probabilities. Each candidate response should include:
- service ID and rank;
- component scores and total heuristic score;
- supporting and contradicting evidence IDs;
- relevant deployment IDs/timestamps, where present;
- exact returned paths;
- missing-data flags and confidence/abstention rationale.

Tests should cover a strong candidate, a contradicting red herring, ties, missing evidence and insufficient evidence. If evidence is weak, return `inconclusive` instead of guessing.

**Gate:** score components explain the ordering and negative evidence is visible.

## 6. Phase 3 — bounded observation-driven agent

Use one fixed registry and one bounded loop, not multiple overlapping `tog_agent.py`/`track1_agent.py` implementations.

Pseudo-flow:

```python
state = initialize_request_and_resolve_entities(request)
for step in range(MAX_STEPS):
    observation = execute_validated_tool(state.next_tool, state.arguments)
    trace.append(trace_from_real_observation(observation))
    state = update_policy_from_observation(state, observation)
    if state.is_terminal:
        break
return structured_result(state, trace)
```

Next-tool choice examples:
- Unknown incident/service → stop with `unknown_entity`.
- Contradictory/weak first hop → expand to a capped deeper frontier.
- Enough evidence and a supported candidate → compute blast radius.
- Explicit counterfactual request and verified candidate edge → propose graph surgery.
- Tool budget exhausted or evidence remains thin → `inconclusive`.

Every trace step records the actual tool, sanitized arguments, observation, measured `time.perf_counter()` latency, outcome, and why the next tool was selected. If no LLM is actually configured, describe the selector as a deterministic policy—not autonomous LLM reasoning.

**Gate:** test that changing a prior observation changes the chosen next tool; test termination at the maximum budget.

## 7. Phase 4 — entities and strict grounding

- Exact graph ID/name lookup first.
- Explicit aliases only where justified by fixtures.
- Fuzzy matches yield suggestions, never silent selection when ambiguous.
- Unknown service stops its operation; do not fall back to a default.
- Return structured claims, not only free-form prose.
- Verify each path node exists and every directed edge exists in the current result or verified graph snapshot.
- Verify every evidence ID is connected to the relevant incident/service; verify team/runbook/ADR records and relationships where those records exist.
- If any claim fails, suppress it and downgrade to `verification_failed` or `inconclusive`.

Adversarial tests must inject valid nodes with fabricated edges, fabricated evidence IDs and nonexistent runbooks.

**Gate:** IDs alone cannot make a fake relationship pass grounding.

## 8. Phase 5 — graph algorithms

Run each algorithm against a tiny graph with known expected properties on the actual installed server. Record the exact server/client versions and verified syntax.

Return honest `engine_used` values such as:
- `falkordb_native_pagerank`
- `falkordb_native_betweenness`
- `cypher_transitive_degree_fallback`
- `cypher_shortest_path`

A fallback must never be reported as a native algorithm. Log technical errors safely and expose a stable public error result.

**Gate:** integration tests confirm the algorithm and result shape; fallbacks are named truthfully.

## 9. Phase 6 — safe graph surgery

Required sequence:
1. Resolve nodes and verify the directed edge exists.
2. Record a baseline topology fingerprint for the relevant graph scope.
3. Create a unique temporary clone using the tested client API.
4. Confirm the clone includes the expected edge.
5. Remove exactly the requested edge and verify the removal count.
6. Re-run the same query/scoring logic with the same incident on the clone.
7. Compare path, score and ranking.
8. Re-query the original graph and verify its topology fingerprint is unchanged.
9. Delete the clone in `finally` and verify it no longer exists.
10. If any invariant fails, return `verification_failed`—never a successful boolean by default.

Test successful surgery and failures at clone, edge removal, rerun and cleanup stages. Do not execute production rollback/circuit-breaking; demo actions are proposed or persisted only after human confirmation.

**Gate:** original graph and clone cleanup are verified even on exceptions.

## 10. Phase 7 — fair benchmark

- Use a documented set of labeled synthetic cases with expected answer/abstention.
- Run graph-backed and graph-free baseline on the same prompts and labels.
- Flat baseline must not traverse dependency edges or consume paths/edge-derived labels.
- Do not leak ground-truth labels into either prediction method.
- Compute all metrics from actual prediction rows; show sample count and every case.
- Include an inconclusive case, disconnected/no-path case and unknown entity if relevant.
- Never force a desired score such as 100% vs. 0%.
- Explain that a small synthetic set demonstrates mechanism, not general production accuracy.

**Gate:** metric tests recompute counts from per-case rows, and topology dependence is tested directly.

## 11. Phase 8 — tool API and MCP

Use a single source of truth for tool names, schemas, validation and handlers. Candidate tools:
1. `triage_incident_with_evidence(incident_id)`
2. `multi_hop_blast_radius(service_id, max_hops)`
3. `shortest_dependency_path(source_service_id, target_service_id)`
4. `graph_algorithms_suite(algorithm, optional_scope)`
5. `verify_action_by_graph_surgery(incident_id, source_service_id, target_service_id)`
6. `resolve_owners_and_runbook(service_id)`

Use explicit outcomes: `answered_with_path`, `not_in_graph`, `unknown_entity`, `inconclusive`, `missing_data`, `verification_failed`, `tool_error`.

Tests cover valid/malformed JSON-RPC, unknown methods/tools, required arguments, type/range validation, exceptions, and whether read-only tools remain read-only. If full MCP is out of scope, document the actual internal structured API instead.

## 12. Phase 9 — UI, API and ports

Keep the existing API working and inspect `vite.config.js`/`package.json` before assuming environment names. Port 8010 is a suggested local workaround for the earlier Windows port-8000 bind issue; the backend and Vite proxy must agree.

Example backend launch:

```powershell
cd "C:\Users\LENOVO\Downloads\ROOTLINE_OMNI_FINAL (1)\rootline"
.\.venv\Scripts\Activate.ps1
python -m backend.seed
python -m pytest -q
uvicorn backend.main:app --host 127.0.0.1 --port 8010 --reload
```

Second terminal:

```powershell
cd "C:\Users\LENOVO\Downloads\ROOTLINE_OMNI_FINAL (1)\rootline\frontend"
npm run build
npm run dev
```

Premium UI sections: incident queue; candidate/evidence view; path explorer; agent trace; direct vs. multi-hop blast radius; counterfactual before/after panel; graph-backed owner/runbook results; persisted decision history; per-case benchmark. Add responsive layout, keyboard focus, reduced-motion support, and loading/error/empty states.

Only display actual API results. No fake timings, graph paths, green badges, owner/runbook records or benchmark totals. Animate actual trace events only.

**Gate:** browser journey works from incident selection through investigation and surgery; production build alone is not enough.

## 13. Required verification matrix

- seed idempotency;
- directed path correctness and hop count;
- supporting and contradicting evidence;
- strong and inconclusive incident;
- unknown incident, unknown service and ambiguous entity;
- bounded agent selection and termination;
- fake node/edge/evidence/runbook grounding failures;
- native algorithm or truthful fallback;
- original topology unchanged and clone cleanup on success/failure;
- tool/API protocol validation;
- fair per-case benchmark calculations;
- graph-down behavior returns a clear error, not sample fake success;
- frontend production build;
- manual browser journey.

At the end, inspect:

```powershell
git status --short
git diff --check
git diff --stat
git diff
```

Do not stage `.env`, secrets, `.venv`, `node_modules`, caches, local graph dumps or build artifacts unless explicitly required. Review staged files before commit. Do not push, deploy or submit without explicit approval.

## 14. Demo order (2:30–3:00)

1. Explain why a service alert isn't enough.
2. Investigate `INC-2026-101` and show the actual graph path/evidence.
3. Compare one-hop with multi-hop blast radius.
4. Show a trace observation driving the next tool selection.
5. Perform isolated edge-removal simulation and show invariant/cleanup checks.
6. Demonstrate unknown-entity rejection and inconclusive abstention.
7. Show measured per-case evaluation and actual test output.

## 15. Submission note

The official event date in the provided context is October 15–18, 2026, with the original deadline listed as October 18 at 11:59 PM IST. Since the current date is October 19, check the official portal for a grace window/extension before assuming submission is open: https://www.wemakedevs.org/hackathons/falkordb
