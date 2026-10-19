# ROOTLINE OMNI — Antigravity Phased Prompt Pack

**Run one phase at a time.** Keep the original Gemini transcripts unchanged. Do not ask the coding agent to paste multiple complete versions of `tog_agent.py` over one another. Do not push/deploy/submit without approval.

## PROMPT 0 — Audit only

You are the senior engineer for ROOTLINE OMNI, Track 01. Audit the current workspace before editing. Inspect Git status, tree, dependencies, graph schema, seed, investigator, surgery, routes, frontend, tests, README, Docker image/client versions, and current run commands. Run existing tests and frontend build if safe. Do not edit code in this phase. Report exact output, current functionality to preserve, risks, and the top three blockers. Focus on hardcoded benchmark values, missing-data defaults, entity parsing, graph-copy invariants/cleanup, native algorithm availability, MCP claims, and API/proxy port consistency.

## PROMPT 1 — Graph correctness and investigator

Implement only graph/data correctness and investigator reliability. Preserve existing public APIs and tests. Verify idempotent seed, parameterized Cypher, native read-only queries, evidence polarity, score breakdown, missing-data behavior, and abstention. Add targeted tests for strong, contradicted, ambiguous, and inconclusive cases. Run relevant tests and report exact results and changed files. Do not redesign the frontend yet.

## PROMPT 2 — Bounded agent and grounding

Add a single bounded observation-driven agent loop using one fixed, validated tool registry. The next tool must be selected from actual previous tool output, not a predetermined sequence. Add max steps, safe argument validation, graph-backed entity resolution, structured answer claims, and path/edge/evidence grounding checks. Do not invent owners/runbooks. Unknown entity, inconclusive, missing data and tool error must be distinct outcomes. Add positive/adversarial tests; report actual traces and test results.

## PROMPT 3 — Algorithms and graph surgery

Verify algorithm support against the actual FalkorDB Docker image/client before implementation. Use a tiny known graph for each algorithm. Report actual engine use and name fallbacks honestly. Harden graph surgery: verify edge direction/existence, clone uniqueness, removal count, same-query rerun, original topology fingerprint, cleanup in `finally`, and cleanup verification. Describe it as a counterfactual topology experiment, not causal proof. Test successful and failing paths; do not fake safety booleans.

## PROMPT 4 — Evaluation and MCP

Implement a fair graph-backed vs graph-free evaluator with identical labeled cases, actual predictions, per-case output, computed metrics, sample size, and limitations. Do not force accuracy targets or hardcode baseline predictions. Decide whether to implement a full MCP-compliant server or document an internal tool API; if MCP, follow the official specification for initialization, capabilities, tool schemas, `tools/list`, `tools/call`, transport, JSON-RPC errors and validation. Add evaluation/protocol tests.

## PROMPT 5 — Premium frontend

Redesign the existing ROOTLINE OMNI UI as a premium dark operations console while preserving all working workflows. Drive every graph, trace, metric, badge, evidence item, latency, runbook and action from actual API responses. Add responsive layout, accessible focus states, reduced-motion support, and real loading/error/empty states. Do not fabricate paths or statuses. Inspect API response shapes first; then implement and run the production build. Report exact output.

## PROMPT 6 — Release audit

Run the complete backend test suite, frontend production build, health/API smoke tests, and manual browser journey against the actual Docker FalkorDB instance. Review Git diff and staged files. Verify README setup instructions as far as practical. Produce a report splitting VERIFIED, FAILED and NOT VERIFIED items with exact commands, counts, server/client versions, benchmark output, surgery invariants, MCP status and remaining limitations. Never push, deploy or submit without explicit user approval.
