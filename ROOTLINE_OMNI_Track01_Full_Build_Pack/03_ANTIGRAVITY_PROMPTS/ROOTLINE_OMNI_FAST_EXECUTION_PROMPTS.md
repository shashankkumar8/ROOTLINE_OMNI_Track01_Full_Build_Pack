# ROOTLINE OMNI — Fast Execution Playbook for Antigravity + Google AI Studio

## What to open first

1. Extract `ROOTLINE_OMNI_FINAL.zip` into a new working folder named `rootline`.
2. Open that extracted `rootline` folder in Antigravity. Do not ask an agent to work on the ZIP itself.
3. Keep the original ZIP untouched as your rollback copy.
4. Open `ROOTLINE_OMNI_Antigravity_Master_Prompt.md` and use it as the governing prompt. This playbook contains the execution prompts in the order to run them.
5. Do not start by rewriting everything. Audit, run, fix the highest-risk failure, then polish.

## Fast strategy (deadline mode)

**P0 — Must work:** backend starts, frontend builds, FalkorDB-backed investigation works, Live Graph Surgery either truly isolates and cleans up or honestly reports an unsupported capability, baseline topology remains unchanged, tests pass, README is truthful.

**P1 — Judge clarity:** one memorable end-to-end journey; obvious baseline vs counterfactual comparison; loading/error/cleanup states; readable evidence and heuristic score explanations; no fake data claims.

**P2 — Release:** fresh setup instructions, screenshots, short demo, public repository, AI disclosure, submission fields.

**P3 — Only after P0/P1:** optional infrastructure and design extras. Do not add databases, queues, authentication, Kubernetes, Terraform, gRPC, or multiple live-update protocols merely to tick boxes.

At every phase ask the agent to report: files changed, exact commands run, pass/fail output, unverified items, and the next single highest-priority action. If a test fails, stop feature work and fix the failure first.

---

# PROMPT 0 — Workspace audit and safe plan (run first in Antigravity)

You are the senior engineer responsible for finishing ROOTLINE OMNI in the currently open workspace. Read `README.md`, `docs/BUILD_STATUS.md`, `docs/FINAL_REVIEW.md`, `docs/graph-model.md`, backend, frontend, and tests before editing anything.

Rules:
- Do not delete working functionality, replace the project with a generic template, or reset Git history.
- Keep the original extracted folder as the working copy and the ZIP as rollback.
- Do not invent test output, benchmark results, AI behavior, user data, integrations, or deployment status.
- Keep FalkorDB central. Synthetic incident data must be labeled synthetic. Scores are heuristics, not probabilities.
- Use the complete `ROOTLINE_OMNI_Antigravity_Master_Prompt.md` as the governing requirements source. Do not discard any of its design rules or any of the 80 engineering concepts.

Tasks:
1. Inspect the file tree, Git status, Python and Node versions, dependency files, config, API routes, graph queries, graph surgery implementation, UI, tests, and docs.
2. Run non-destructive checks first: Python version, Node/npm versions, `pytest -q`, frontend `npm run build` (install dependencies only if necessary).
3. Report the exact current status without claiming checks that were not run.
4. Create/update `docs/EXECUTION_PLAN.md` with P0/P1/P2/P3 priorities, dependencies, verification commands, and risks.
5. Create/update `docs/REQUIREMENT_TRACEABILITY.md` mapping every source requirement and all 80 engineering concepts to `IMPLEMENT NOW`, `IMPLEMENT AS OPTIONAL PROFILE`, `DOCUMENT / ARCHITECT`, `NOT APPLICABLE`, or `BLOCKED`. Include a reason and verification evidence/gap for every item. No item may silently disappear.
6. Make no broad refactor in this phase. End with the three most urgent concrete blockers and wait for the next prompt.

Output format: audit findings, exact command results, files changed, risks, next step. Do not say “all done” if any check remains unverified.

---

# PROMPT 1 — Make the app run locally (P0)

Using the audit, make the smallest safe changes needed to get ROOTLINE OMNI running locally on Windows. Preserve the existing architecture and product features.

1. Ensure Python backend setup is documented and dependencies are accurate.
2. Ensure frontend dependencies and build are accurate; do not upgrade packages gratuitously.
3. Ensure `.env.example` is safe and contains placeholders only. Never put secrets in source control.
4. Ensure health endpoint reports actual backend/graph connection state, not a hard-coded success.
5. Ensure the seed operation is repeatable and clearly uses synthetic demo data.
6. Make errors actionable and redact secrets from logs.
7. Add/repair a minimal smoke test for health and a graph-backed investigation.
8. Run the tests and frontend production build; fix real failures before adding features.
9. Update `docs/BUILD_STATUS.md` with the exact commands run, environment, output summary, and anything not verified.

Do not add production infrastructure to pass a checklist. Do not fake FalkorDB availability. Stop and report if a prerequisite cannot be verified.

Acceptance: a fresh user can follow README commands; backend health is truthful; investigation is backed by the configured graph; tests and frontend build have actual recorded results.

---

# PROMPT 2 — Prove Live Graph Surgery is real and safe (highest differentiator)

Audit `backend/surgery.py`, `backend/graph.py`, `backend/queries.py`, `backend/investigator.py`, and all surgery tests. Focus on correctness, not visual polish.

Required behavior:
1. Capture baseline dependency topology and the baseline investigation result.
2. Create a genuinely isolated temporary graph using a copy mechanism supported by the actual FalkorDB server/client version. Verify the command/API against installed version or reliable documentation before relying on it.
3. If graph copy is unsupported, fails, or cannot be verified, return an explicit blocked/unsupported state. Never report a successful isolated simulation when none happened.
4. Remove only the selected edge in the temporary graph, and verify that the intended edge was actually removed there.
5. Rerun the same investigation logic against the temporary graph and compare affected paths, candidate ranking, and explanation deltas.
6. Verify baseline dependency topology still matches the captured baseline after the experiment. Explain in the UI/docs that an audit event may still be written to the baseline graph; topology-preserved is not equivalent to byte-for-byte graph immutability.
7. Clean up the temporary graph in a `finally`-style path on success and failure. Report cleanup outcome truthfully.
8. Use unique, collision-resistant temporary graph names and safe identifier handling. Avoid unsafe string interpolation for user-controlled query values.
9. Add tests for success, edge missing, copy unsupported, copy failure, investigation failure, cleanup failure, baseline topology mutation, duplicate/concurrent requests if applicable, and a negative control edge whose removal should not change the target outcome.
10. Add a test or command that proves the chosen graph-copy mechanism works against the intended FalkorDB mode. If the current test double cannot prove it, label that limitation.

Do not add fabricated results, a fake graph-copy adapter, or a mocked success presented as a real integration. Run relevant tests, then the full suite. Update docs with actual evidence and limitations.

Acceptance: the judge can see the real intervention, baseline vs counterfactual comparison, baseline-topology verification, and temporary graph cleanup. Any unsupported case is visibly honest.

---

# PROMPT 3 — Make the judge journey obvious and memorable

Inspect the current UI before changing it. Keep the product an operational incident-investigation workspace, not a generic SaaS marketing page.

Optimize this exact demo story:
1. Open seeded incident `INC-2026-101` (or the actual seeded ID if it differs; use the real source of truth).
2. Run the investigation and show graph-derived paths, affected services, evidence, contradictory evidence where available, and transparent heuristic ranking.
3. Open the Company Brain for ownership/runbooks/ADRs where supported.
4. Select the actual dependency edge `inventory-service → cache-redis` only if that edge exists in seeded data; otherwise use the actual existing edge and update docs consistently.
5. Run Live Graph Surgery; show clear stages: baseline captured, isolated graph created, edge removed, investigation rerun, comparison produced, baseline topology verified, temporary graph cleaned up, audit saved (only when each is actually confirmed).
6. Show the counterfactual result next to baseline, explain what changed and what did not, and record a human decision with rationale.
7. Refresh and prove history persists if persistence is implemented; otherwise disclose the limitation.

Design constraints from the preserved source prompt are mandatory. In particular, avoid purple gradient pill buttons, fake reviews/metrics, vague hero copy, emojis, em dashes, generic AI stock copy/photos, cursor animation, fake counters, pure-white or purple-black themes, neon/pastel gradients, radial orbs/dot grids/grain, liquid glass, shadows everywhere, colored left stripes, gradient hero text, banned default font pairings, generic buzzwords, three identical feature cards, bento grids, hero badges, Lucide icons everywhere, uncustomized shadcn, excessive rounded cards, fake testimonials, mock terminals, inconsistent spacing, hover effects everywhere, fade-on-hover buttons, animated arrows, and scroll-fade sections.

Required: intentional tokenized design system, accessible focus states and contrast, 4/8px spacing logic, responsive layout, useful skeleton loaders matching the content layout, empty/error/loading/success/blocked states, purposeful Framer Motion state transitions only if available and useful, reduced-motion support, favicon, and accurate `/terms` and `/privacy` pages if public-facing.

Use real backend responses. No decorative control that does nothing. Every primary action must have a visible outcome and errors must be understandable. Avoid unnecessary new dependencies. If a library/component cannot be installed or its license/API cannot be checked in time, do not pretend it was used.

After changes, run frontend build and relevant tests. List each interaction manually checked vs not checked. Do not claim browser verification unless you actually opened and exercised it.

---

# PROMPT 4 — API, security, reliability, and 80-item requirement review

Review the traceability matrix against the complete source prompt. Do not force every engineering concept into this prototype. Keep every concept visible and assign one honest disposition with rationale.

Implement now only the changes that directly improve the local hackathon path or are minimum security/reliability requirements. Consider input validation, safe graph/query construction, strict CORS, request-size limits, timeouts, bounded retries where safe, health/readiness truthfulness, safe error messages, temporary-graph cleanup, idempotency for state-changing actions if duplicate submissions are possible, and tests for concurrency/race conditions where relevant.

For each item among the 80 concepts:
- preserve its intent and technical meaning;
- say whether it applies to the actual architecture;
- point to implementation/config/docs and test evidence, or explain the gap;
- do not claim relational SQL behavior for FalkorDB/Cypher;
- do not add Redis/Kafka/Postgres/Kubernetes/Terraform/OAuth/gRPC/HTTP3/WebSockets/SSE/long-polling unless an actual product requirement justifies it and it can be integrated and tested;
- document production alternatives and adoption triggers for future scaling.

Review secrets, `.env`, `.gitignore`, dependency lockfiles, package audit output, CORS, error handling, request validation, temporary graph naming/cleanup, audit records, and public documentation. Never commit API keys, tokens, personal data, or real incident information.

Run all tests and builds after changes. Update the traceability matrix only with evidence. Finish with an honest gap report, not a claim that all 80 items are implemented.

---

# PROMPT 5 — Release and judge demo pack

Prepare the project for a reproducible hackathon submission without publishing anything automatically.

Create/update:
- `README.md`: problem, target user, why graph-native, key differentiator, architecture, setup, run, test, limitations, synthetic-data note, AI-assistance disclosure, and actual demo/repository URLs only when known.
- `docs/ARCHITECTURE.md`: components, request flow, graph schema, graph surgery lifecycle, trust boundaries, cleanup, and failure modes.
- `docs/REQUIREMENT_TRACEABILITY.md`: all source design requirements plus all 80 engineering concepts, with honest dispositions and evidence.
- `docs/BUILD_STATUS.md`: exact verified checks and unverified environments.
- `docs/DEMO_SCRIPT.md`: a timed script under 3 minutes, exact clicks, expected visible states, fallback if graph copy is unsupported, and claims not to make.
- `docs/AI_DISCLOSURE.md`: tools actually used (e.g. Antigravity and Google AI Studio only if actually used), the tasks they assisted with, and the human verification performed. Do not state that tools were used if they were not.
- `/terms` and `/privacy` routes only if they can be made accurate and tested before release.

Demo order (target 2:30–2:50):
0:00–0:20 problem and pitch; 0:20–0:55 run an investigation; 0:55–1:20 inspect evidence and dependency path; 1:20–2:05 perform Live Graph Surgery and compare; 2:05–2:25 verify baseline topology and cleanup; 2:25–2:45 save human decision and close with limits/impact.

Do not invent video URLs, repo URLs, screenshots, benchmark numbers, users, or judging claims. Never push to GitHub, deploy, or submit without my explicit approval. Provide exact commands and a final checklist.

---

# PROMPT 6 — Final adversarial judge review (run last)

Act as a skeptical graph database engineer, hackathon judge, and first-time user. Inspect the actual code and run the available tests. Try to disprove the product's strongest claims.

Check:
1. Does the core investigation actually query FalkorDB?
2. Is graph surgery truly isolated, or is it a mock / shared graph mutation?
3. Is the edge removal verified?
4. Is the baseline dependency topology checked before and after?
5. Is temporary graph cleanup reliable on every failure path?
6. Are results deterministic and labeled as heuristic/synthetic where appropriate?
7. Can a first-time user complete the story without verbal help?
8. Do loading/error/blocked/empty states explain what happened?
9. Do README and demo claims match code and test evidence?
10. Does the traceability matrix contain all 80 concepts and all original design requirements, with no silently dropped item?
11. Can a clean clone reproduce setup and tests?
12. Are any secrets, fake metrics, non-working controls, fake success states, or unsupported claims present?

Fix only high-value, low-risk issues that fit the deadline. Rerun tests and frontend build. Produce a final table with `Claim | Evidence | Verified? | Remaining risk`. Do not submit or publish. End with a concise Go / No-Go recommendation and the single next action.

---

## Google AI Studio: safe ways to use it alongside Antigravity

Use Google AI Studio as a **review and planning assistant**, not as a second agent editing the same files simultaneously. Antigravity remains the single source of truth for code changes.

### AI Studio prompt A — independent architecture reviewer

You are an independent reviewer, not the implementer. Review the attached ROOTLINE OMNI README, architecture docs, graph surgery implementation, tests, and build logs. Do not invent unseen files or claim execution. Return: (1) the 5 highest-risk correctness issues, (2) graph isolation and cleanup failure modes, (3) test cases missing, (4) UX confusion points in the judge journey, (5) exact file/line evidence where supplied, and (6) a prioritized fix list with P0/P1/P2. Preserve FalkorDB as the core. Clearly separate evidence from inference. Do not propose new infrastructure unless justified by a specific failure mode.

### AI Studio prompt B — adversarial test designer

Given the supplied source for ROOTLINE OMNI Live Graph Surgery, design adversarial tests for graph-copy failure, missing edge, duplicate requests, cleanup failure, partial failure after edge deletion, baseline topology mutation, temporary graph name collision, unsupported server version, malformed input, and concurrent surgery. For each test, give setup, action, expected observable behavior, and invariant. Do not write tests against imaginary APIs. Flag any test that requires a real FalkorDB integration environment. Do not assert that a test passed.

### AI Studio prompt C — judge/demo critic

Act as a skeptical hackathon judge watching a 2:45 screen recording with no narration context. Review the actual screenshots or recording transcript I provide. Identify where the core idea is unclear, which UI elements distract, what proof is missing for the graph intervention, and what one visual comparison would make the outcome unmistakable. Do not recommend fake metrics, testimonials, invented AI, or a generic landing page. Return timestamped edits and a revised 2:45 narration only when evidence is supplied.

### AI Studio prompt D — requirement-traceability auditor

Audit the provided source prompt and `docs/REQUIREMENT_TRACEABILITY.md`. Verify every original visual/design constraint and all 80 engineering concepts appear exactly once or have an explicit mapping. Do not silently remove, merge away, or mark as implemented without evidence. Flag missing requirements, duplicate IDs, inconsistent dispositions, and unsupported implementation claims. Return only a correction list and proposed traceability entries; Antigravity will apply changes.

### AI Studio prompt E — documentation and claim consistency

Compare the supplied README, build status, demo script, AI disclosure, architecture document, traceability matrix, and test output. Find contradictions, unverified claims, missing setup commands, wrong paths, invented URLs, or inaccurate AI-use statements. Never infer that a command succeeded unless output is provided. Return a file-by-file patch proposal, not a rewritten architecture.

## How to combine the tools without losing time

1. Antigravity executes one prompt/phase at a time and owns the workspace edits.
2. After Prompt 0, send the audit output to AI Studio prompt A or B for an independent review.
3. Paste only the review findings back into Antigravity and ask it to validate each finding against code before changing anything.
4. After graph surgery is verified, use AI Studio prompt C on actual screenshots or a real demo transcript.
5. Before release, use AI Studio prompts D and E against the actual matrix and docs.
6. Do not run two agents that independently rewrite the same files. Do not paste secrets, credentials, private keys, or real user/production data into either tool.
7. If the deadline is close, stop after P0, the core judge journey, accurate docs, and a reproducible demo. Optional production infrastructure is not a substitute for a working graph intervention.

## Windows local run checklist

From the extracted `rootline` folder, in PowerShell:

```powershell
python --version
node --version
npm --version
docker --version
```

Start FalkorDB (if Docker is installed and the project is configured for this local mode):

```powershell
docker run -d --name rootline-falkordb -p 6379:6379 -p 3000:3000 falkordb/falkordb:latest
```

If the container already exists:

```powershell
docker start rootline-falkordb
docker ps
```

Backend environment and tests:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-dev.txt
pytest -q
python -m backend.seed
uvicorn backend.main:app --reload --port 8000
```

In a second terminal, from the project root:

```powershell
cd frontend
npm install
npm run dev
```

Open the URL printed by Vite (commonly `http://localhost:5173`). Then run the production build in that terminal:

```powershell
npm run build
```

If PowerShell blocks venv activation, use this only for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
```

Important: these are the intended commands, not proof they all work in every environment. If Docker, graph copy, or a dependency fails, capture the exact error and use it as evidence. Do not claim the cloud or browser flow is verified unless it was actually tested.

## Final go/no-go checklist

- [ ] Fresh extraction setup works on the target machine.
- [ ] FalkorDB connection and health state are real.
- [ ] Investigation results are graph-backed.
- [ ] Live Graph Surgery is truly isolated or visibly blocked honestly.
- [ ] Baseline topology invariant is tested.
- [ ] Temporary graph cleanup is tested on success and failure.
- [ ] Negative control edge test exists.
- [ ] Backend tests pass; exact count/output recorded.
- [ ] Frontend production build passes.
- [ ] Primary UI actions are manually click-tested.
- [ ] Requirement matrix includes every source requirement and all 80 concepts.
- [ ] README, build status, demo script, and AI disclosure agree with evidence.
- [ ] Public repo/demo links are real, not placeholders.
- [ ] Demo recorded and replayed once; no sensitive data shown.
- [ ] Final submission reviewed manually; nothing published/submitted by an agent without approval.
