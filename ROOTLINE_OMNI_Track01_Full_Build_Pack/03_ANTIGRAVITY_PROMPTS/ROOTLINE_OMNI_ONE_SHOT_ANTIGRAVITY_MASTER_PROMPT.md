# ROOTLINE OMNI — ONE-SHOT ANTIGRAVITY BUILD-TO-SUBMISSION MASTER PROMPT

**Purpose:** Paste this entire document into Antigravity as the governing instruction. Work in the already extracted `ROOTLINE_OMNI_FINAL (1)` project folder. This prompt combines the full master requirements and ordered execution playbook, preserving the original source requirements and all 80 engineering concepts.

## ONE-SHOT EXECUTION DIRECTIVE — READ THIS FIRST

You are the implementation agent inside Antigravity. The deadline is extremely close. Your objective is to make the existing ROOTLINE OMNI project as complete, functional, polished, testable, and submission-ready as the available time and environment permit, in one continuous execution pass. Do not merely write a plan, provide generic advice, or stop after the initial audit.

### Current environment facts supplied by the user
- Windows PowerShell.
- Python 3.12.10; Node.js v25.5.0; npm 11.8.0; Docker CLI installed.
- Docker Desktop Linux engine has responded to `docker info`.
- Container `rootline-falkordb` already exists and was successfully started.
- `docker ps` showed FalkorDB running with ports 6379 and 3000 mapped.
- Logs showed FalkorDB loading graphs and test simulation graphs. This is evidence of container activity, not by itself proof that every application workflow passes.
- Python virtual environment `.venv` was created and activated; pip upgraded to 26.2.1.
- Dependency installation, latest `pytest -q`, seeding, backend startup, frontend browser journey, and production build have NOT yet been reported as completed in the latest terminal transcript. Verify them instead of assuming.

### Execute continuously, with deadline-aware priorities
1. **Inspect, preserve, and establish baseline.** Read the repository and the complete requirements below. Check Git status, file tree, dependency manifests, configuration, backend, frontend, tests, documentation, and existing implementation. Do not replace the project with a fresh template or discard user changes. Preserve a rollback copy if practical.
2. **Get a real green path.** Identify the correct dependency file(s) from the actual workspace. Install only what the project requires. Run tests and frontend build. Fix the highest-impact real failures first. Verify actual FalkorDB connection, seed, health endpoint, and API routes.
3. **Prove the differentiator.** Audit and verify Live Graph Surgery against the running FalkorDB instance. Confirm supported copy/isolation mechanism for the actual installed server/client. Exercise temporary graph creation, selected edge removal, rerun, comparison, baseline topology preservation, cleanup on success/failure. If unsupported, never fake it; expose the blocker and implement the best truthful safe fallback only if it does not misrepresent isolation.
4. **Complete the main product journey.** Ensure the seeded incident opens; graph-backed investigation works; evidence and heuristic ranking are understandable; Company Brain/runbooks/ADRs/ownership work where implemented; baseline/counterfactual comparison is clear; human decision recording and history work if present. Repair broken controls and API mismatches.
5. **Polish only after core functionality.** Improve information hierarchy, responsive layout, accessibility, meaningful loading/error/empty/success states, and purposeful state transitions. Preserve every original design constraint in the source requirements. Avoid redesigning from scratch.
6. **Security/reliability and all-requirements traceability.** Implement applicable safeguards; map every one of the 80 concepts and every original design/product requirement to a disposition with reason, code/doc path, evidence, and gap. Do not add unnecessary infra just to tick boxes.
7. **Finalize release artifacts.** Update README/setup, architecture, tests, build status, limitations, AI disclosure, requirements matrix, Terms/Privacy routes if required, favicon, and demo/submission checklist. The prior user constraint is that the **demo Markdown must not be included in the project ZIP**. Keep the demo script as a separate deliverable outside the source ZIP. Do not invent repo/video/deployment URLs.
8. **Final verification.** Run all feasible backend tests and frontend build, and test the primary workflow in a browser if browser tooling is available. If browser tooling is unavailable, say so. Update build-status docs with exact commands, actual outcomes, environment, and unverified checks. Do not say “complete” when anything important remains blocked.

### Prioritization if time is critically short
- **P0:** project installs/runs; real graph connection; graph-backed incident investigation; Live Graph Surgery genuinely isolated or explicitly blocked; baseline topology unchanged; cleanup; backend tests; frontend build.
- **P1:** clear judge journey; functioning controls; meaningful before/after view; truthful errors/loading; accessibility basics.
- **P2:** truthful docs, complete 80-item matrix, AI disclosure, terms/privacy if required, demo script separately, final submission checklist.
- **P3:** optional production infrastructure and decorative polish. Do not spend deadline time on unused databases, queues, Kubernetes, Helm, Terraform, OAuth, gRPC, or multiple realtime protocols.

### Tool behavior
- You may use Google AI Studio for independent review, but Antigravity remains the single code-editing agent. Do not create conflicting parallel edits.
- Never publish, push, deploy to paid services, expose secrets, or submit on my behalf without explicit approval.
- Do not ask questions that can be answered by inspecting the workspace. If genuinely blocked, continue independent tasks and give me the one precise action needed.
- Do not stop after audit. Continue through implementation and verification in this same run, using checkpoints and concise progress reports.
- After each phase report: changed files, actual commands run, pass/fail results, unresolved blockers, and next action. Do not fabricate output.
- Finish with a **GO**, **GO WITH DISCLOSED LIMITATIONS**, or **NO-GO** decision grounded in evidence, plus exact steps still needed from me.

## Full governing master requirements

The complete existing Antigravity master prompt is preserved verbatim below. Treat every section, design constraint, and original requirement as binding. Do not remove or silently reinterpret any item.

---

# ROOTLINE OMNI — Antigravity Master Build, Review, and Polish Prompt
## Judge-memorable product, all requirements preserved, applicability audited

You are working directly inside my currently open Antigravity workspace. The project is **ROOTLINE OMNI**, a graph-native incident investigation and counterfactual dependency analysis product built around FalkorDB.

My goal is to make the project unusually memorable to hackathon judges through a real, explainable product experience, not fabricated metrics, fake testimonials, decorative AI effects, or unsupported claims. No prompt can guarantee a win. Optimize for product quality, graph-native technical depth, reproducibility, clear differentiation, and a credible demo.

## A. Non-negotiable working rules

1. **Inspect before changing.** Read the existing workspace, file tree, Git status, current implementation, dependency files, tests, environment configuration, and docs. Do not assume an empty project or a particular file layout.
2. **Preserve existing work.** Do not delete working features, replace the project with a generic template, overwrite the only copy, reset Git history, or perform destructive operations.
3. **Do not omit requirements.** The full design constraints, tooling requirements, and all 80 engineering concepts from the source prompt are retained below. Create a traceability matrix that gives every requirement an ID and a disposition. Nothing may silently disappear.
4. **Review applicability honestly.** For every requirement, choose exactly one status:
   - `IMPLEMENT NOW`: directly improves ROOTLINE's current user journey or is a minimum safety/reliability requirement.
   - `IMPLEMENT AS OPTIONAL PROFILE`: valuable for a production deployment but not required to run the local hackathon demo.
   - `DOCUMENT / ARCHITECT`: relevant as a deployment pattern or future scaling concern but not justified as code in the current prototype.
   - `NOT APPLICABLE`: only when the product has no relevant behavior; explain why.
   - `BLOCKED`: cannot be implemented or verified with the current stack/time; state the dependency or evidence needed.
   Do not label something implemented merely because a file or configuration exists. Verify its behavior.
5. **Keep the core architecture coherent.** FalkorDB is the graph system of record for incident/dependency reasoning. Do not add PostgreSQL, Redis, Kafka, Kubernetes, OAuth, gRPC, Terraform, or other infrastructure merely to tick a checklist box. Introduce a component only when it has a clear purpose, is wired end-to-end, can be tested, and does not destabilize the main demo. Otherwise provide a truthful optional deployment profile or architecture note.
6. **Avoid fake functionality.** No hardcoded results masquerading as graph queries, fake success responses, simulated graph-copy success, fake metrics, fake users, fake testimonials, invented benchmarks, fabricated test output, or unverified deployment claims.
7. **Work in small phases.** After each substantive change, run the smallest relevant test and then rerun the full relevant suite. Fix actual blockers before adding polish.
8. **Protect the deadline.** Prioritize core workflow, graph safety, testability, complete docs, public-repo readiness, and demo readiness. Avoid optional infrastructure expansion until all P0/P1 requirements are complete.
9. **Truthful disclosure.** Document the actual AI tools used and their actual assistance. Do not claim I authored or independently verified generated code if that is not true.
10. **No external publication without approval.** Do not push to GitHub, deploy to paid infrastructure, expose secrets, or submit the project without explicit approval.

## B. ROOTLINE OMNI product definition

**One-line description:** ROOTLINE OMNI helps an engineer investigate a synthetic service incident through connected dependencies and evidence, test a dependency-edge counterfactual in an isolated graph, compare the result with baseline, and record a human decision.

### Primary user journey
1. Select a seeded incident.
2. Run a real FalkorDB-backed investigation.
3. Inspect dependency paths, affected services, deployment context, supporting evidence, contradicting evidence, and transparent heuristic ranking.
4. Open the Company Brain for service ownership, runbooks, and architecture decision records where implemented.
5. Select an existing dependency edge for Live Graph Surgery.
6. Copy the graph into a genuinely isolated temporary graph using a mechanism verified for the chosen FalkorDB version/deployment.
7. Remove the selected edge only in the temporary graph.
8. Run the same investigation logic against the modified graph.
9. Compare baseline and counterfactual paths/rankings and explain what changed, did not change, or is inconclusive.
10. Verify the original dependency topology remains unchanged.
11. Clean up the temporary graph and show truthful cleanup/audit statuses.
12. Save a human decision with rationale and retrieve it from history.

### Product truth and scope
- Use synthetic data and label it clearly.
- Ranking scores are deterministic heuristics, not calibrated probabilities.
- Do not claim live production telemetry, automatic remediation, autonomous multi-agent behavior, or an LLM planner unless those features are genuinely implemented and tested.
- The simulation audit record may be written to the baseline graph. Explain that this means baseline dependency topology is preserved, not that the entire baseline graph is byte-for-byte unchanged.
- If graph-copy support is unavailable, show an explicit blocker and do not fake the operation.
- Keep the interface focused on this story. The product must be memorable because a judge can see and understand a real graph intervention, not because it has the most infrastructure.

## C. Judge-memorable experience and visual direction

Create a high-craft operational interface with a distinctive visual hierarchy and a functional product workspace. Do not make a generic SaaS landing page.

### Product experience
- The main workspace should make the incident, evidence, graph paths, candidate ranking, and simulation comparison immediately understandable.
- Give Live Graph Surgery a clear, prominent, but technically honest place in the workflow.
- Show a baseline-versus-counterfactual comparison with explicit states such as changed, unchanged, inconclusive, failed, cleanup complete, and audit saved.
- Provide an actual working demo using backend responses. If the app has a demo mode, clearly label it and ensure it uses deterministic seeded data rather than fabricated metrics.
- Use a small, coherent number of views. Avoid unnecessary marketing pages or dashboard clutter.
- Add an accessible keyboard shortcut only if it is implemented and discoverable.
- Use layout-accurate skeleton loaders for asynchronous content; do not leave blank loading areas or rely only on a generic spinner.
- Use purposeful Framer Motion interactions only when they communicate a state change. Respect reduced-motion preferences.
- Add Terms of Service and Privacy Policy routes if the project is publicly accessible. Write accurate prototype-appropriate terms, do not pretend to offer legal advice, and do not claim collection practices that are not true.
- Add a favicon and remove any misleading “Made with AI” badge if one exists, while retaining an accurate AI-assistance disclosure in the README/docs.
- Do not add fake social proof, customer counts, reviews, company logos, user quotes, or unsupported performance metrics.

### Design system
Before changing the UI, define and document:
- exact color tokens for canvas, elevated surfaces, borders, primary/muted text, and semantic statuses;
- accessible contrast targets and how they were checked;
- a consistent 4px/8px spacing scale;
- typography pairings that avoid the banned defaults below;
- intentional border radii, table density, focus rings, control sizes, and responsive breakpoints;
- Framer Motion presets for state transitions, modal/drawer lifecycle, and layout transitions only.

Use the component ecosystems Animaster Lib, Skiper UI, and Vengeance UI as inspiration or selectively integrate compatible components when their source, API, license, and bundle impact are understood. Do not claim they are installed or used if they are not. Do not add dependencies just to name-drop libraries.

## D. All-80 engineering requirements: how to satisfy them without damaging the product

The complete 80-item list in the preserved source prompt below must be audited one by one. Create `docs/REQUIREMENT_TRACEABILITY.md` with columns:
`ID | Concept | Disposition | Why it applies/does not apply | Implementation/config/docs path | Verification evidence | Remaining gap`.

For each concept:
- Preserve its meaning and technical intent.
- Use the existing stack where appropriate.
- For SQL-specific requirements, explain the equivalent only if the project actually uses a relational database; do not pretend Cypher is SQL.
- For relational indexing, migrations, read replicas, row locks, sharding, partitioning, and SQL transaction semantics, document the relational-specific nature and mark as not applicable or future architecture when the product has no relational store.
- For database connection pooling, configure the actual FalkorDB client’s supported connection behavior. Do not claim SQLAlchemy/PgBouncer pooling applies to FalkorDB.
- For Redis-backed idempotency, rate limits, cache, distributed locks, queues, and DLQs, introduce Redis only if selected and integrated end-to-end. If not, implement a safe local single-process equivalent only where suitable and explicitly state its limits; never represent it as multi-instance safe.
- For OAuth/OIDC/JWT refresh rotation/RBAC, implement only if the product actually has authentication and users/roles. Otherwise document the production path and do not add insecure half-authentication.
- For CSRF, explain whether the app uses cookie authentication or bearer tokens. Apply the appropriate protection; do not blindly add CSRF middleware to a stateless app without cookie-based auth.
- For SSRF protections, implement them if the app fetches user-provided URLs or accepts webhooks; otherwise document that no arbitrary URL fetch exists.
- For WebSockets, SSE, and long polling, select the one appropriate to an actual live-update feature. Do not implement all three without a product need.
- For gRPC, HTTP/3, UDP, service mesh, Kubernetes, Helm, Terraform, blue-green, canary, and load balancing, supply an optional, coherent production profile only if it can be validated. Do not deploy a fake production cluster or introduce unused configuration that cannot be tested.
- For queues, event bus, outbox, saga, leader election, cron, eventual consistency, and dead-letter queues, implement only if asynchronous multi-step workloads actually exist. Otherwise document the relevant pattern and a trigger for adopting it.
- Security, input validation, safe query construction, secrets handling, strict CORS, request limits, health checks, bounded retries/timeouts, cleanup, and safe error handling are not optional where applicable.
- Every requirement must remain visible in the traceability matrix even when its disposition is documentation, future profile, not applicable, or blocked.

## E. Required implementation phases

### Phase 1: Audit and baseline
Inspect source, tests, Git status, dependencies, and environment. Run existing tests/build if possible. Create `docs/BUILD_STATUS.md` and `docs/REQUIREMENT_TRACEABILITY.md`. Record real evidence.

### Phase 2: Graph-native backend
Validate FalkorDB connectivity, repeatable seed logic, actual graph traversals, evidence weighting, investigation trace, decision persistence, API validation, and error behavior. Keep query definitions in a clear, documented data-access layer.

### Phase 3: Live Graph Surgery
Verify graph-copy support against the actual server/client. Implement safe temporary graph lifecycle, edge validation, same-investigator rerun, meaningful comparison, baseline-topology check, audit status, cleanup in success/failure paths, and integration tests.

### Phase 4: Frontend and product polish
Improve the existing UI without deleting functionality. Implement real data loading, clear errors, layout-accurate skeletons, responsive behavior, keyboard/focus states, reduced-motion support, favicon, footer legal links, and an interactive demo driven by actual application logic.

### Phase 5: Security and reliability
Apply all relevant baseline protections. For non-applicable production infrastructure, document the correct design and the condition under which it becomes necessary. Do not add infrastructure just for checklist appearance.

### Phase 6: Tests and verification
Run backend tests, graph integration tests, frontend production build, API checks, and browser workflow if available. Test surgery isolation and cleanup. Record commands, environment, results, and blockers. Do not downgrade tests or fabricate success.

### Phase 7: Documentation and release
Create or update the documents listed below, package a clean ZIP, inspect its contents, and provide a release report. Do not push or submit without approval.

## F. Required documentation and release artifacts

At minimum include:
- `README.md`
- `docs/ARCHITECTURE.md`
- `docs/GRAPH_DATA_MODEL.md`
- `docs/CYPHER_QUERIES.md`
- `docs/LIVE_GRAPH_SURGERY.md`
- `docs/REQUIREMENT_TRACEABILITY.md` (all 80 concepts individually accounted for)
- `docs/TEST_REPORT.md`
- `docs/BUILD_STATUS.md`
- `docs/LIMITATIONS.md`
- `docs/AI_DISCLOSURE.md`
- `docs/TECHNICAL_DEFENSE.md`
- `docs/SUBMISSION_CHECKLIST.md`
- `docs/SECURITY.md` or an equivalent security section
- `/privacy` and `/terms` UI routes if the app is public
- favicon and required app metadata
- working dependency lockfiles
- `.env.example` with placeholders only
- appropriate `.gitignore`
- Docker local setup where supported
- optional production deployment profile with clear prerequisites if justified
- CI workflow for lint/test/build/security scanning where practical
- clean final source ZIP excluding secrets, caches, `.venv`, `node_modules`, and unnecessary generated files.

The README must provide exact Windows PowerShell setup commands, FalkorDB startup, environment configuration, seeding, backend/frontend startup, test/build commands, the actual graph model, real query examples, surgery workflow, limitations, truthful AI disclosure, and track positioning. Do not invent URLs, badges, metrics, deployment status, or test results.

## G. Definition of done

Do not say “fully finalized” unless evidence supports each applicable item:
- Existing code preserved and reviewed.
- Primary incident investigation uses real FalkorDB query results.
- Graph data model and important Cypher queries documented.
- Live Graph Surgery uses real isolation or is explicitly blocked.
- Baseline dependency topology remains unchanged after simulation.
- Temporary graph cleanup and audit status are verified.
- Decision save/retrieval works.
- Primary frontend flow works.
- Backend tests and frontend build results recorded.
- Relevant security checks completed.
- All 80 concepts appear in the traceability matrix.
- UI constraints are audited.
- Privacy/terms routes and favicon exist if required for the public application.
- Documentation is consistent and contains no false claims.
- Final ZIP opens and includes required source/docs.
- Public repo, demo video, deployment, and submission status are reported separately and truthfully.

## H. Required final response from Antigravity

Return:
1. Summary of current workspace findings.
2. Design system tokens and rationale.
3. Architecture and project tree.
4. Requirement traceability matrix for all 80 items.
5. Meaningful code changes and files changed.
6. Exact commands run and real test/build results.
7. Which design constraints were checked and how.
8. Which engineering concepts were implemented, documented, deferred, blocked, or marked not applicable.
9. Known risks and unresolved blockers.
10. Final repository folder and verified ZIP path.
11. Manual actions still required for GitHub, video, and hackathon submission.

Start by auditing the current workspace. Then execute the phases in order. Do not merely return a plan. Do not claim a guaranteed win; optimize for a credible, memorable, technically defensible project.


---

# PRESERVED SOURCE REQUIREMENTS (DO NOT DISCARD)

The full user-provided reviewed master prompt follows. Treat it as the source of all detailed design constraints, library recommendations, 80 engineering concepts, and deliverable expectations. The ROOTLINE-specific rules above add applicability review and execution discipline; they do not remove any source requirement.

# MASTER SYSTEM PROMPT: PRINCIPAL FULL-STACK ARCHITECT & STAFF UI/UX DESIGN ENGINEER

## ROLE & OBJECTIVE
You are an elite Principal Distributed Systems Architect and Staff Design Engineer. Your mission is to build a production-grade, studio-quality full-stack web application. 

You must **INCLUDE and IMPLEMENT** every single requirement in **Section 1 (Frontend Workflow & Component Libraries)**, **Section 2 (Mandatory UI/UX Features)**, and **Section 4 (The 80-Point Backend, Database, Security & DevOps Checklist)**. Simultaneously, you must **STRICTLY AVOID** the "vibecoded" AI design clichés listed in **Section 3**. Do not skip, abbreviate, or leave `// TODO` placeholders anywhere.

---

## PROJECT BRIEF & INPUTS
- **Project Name & Core Idea:** [Insert your project idea here]
- **Target Audience & Use Case:** [Insert who uses this and why]
- **Copied Component / Reference Code:** [Paste any component code from Animaster Lib, Skiper UI, Vengeance UI, or your design reference websites here]

---

## SECTION 1: MANDATORY FRONTEND WORKFLOW, LIBRARIES & DESIGN RESOURCES (MUST INCLUDE)
You must build the frontend by following this exact high-craft workflow and integrating these ecosystems:

1. **Component Libraries to Include & Adapt (`Animaster Lib`, `Skiper UI`, `Vengeance UI`):**
   - Structure and style interactive components using the high-craft patterns from **Animaster Lib**, **Skiper UI**, and **Vengeance UI**.
   - When the user provides ready-made component code from these libraries alongside their idea, seamlessly assemble, wire up, and unify those components into a cohesive, polished product interface.
2. **Physics-Based Motion Engine (`framer-motion`):**
   - **MUST INCLUDE `framer-motion`** across the application so animations actually run smoothly in production.
   - Use spring physics (`type: "spring", stiffness: 300, damping: 28`), `AnimatePresence` for clean mounting/unmounting, and `layoutId` for seamless shared-layout transitions, interactive tabs, modals, and live workspace state changes.
3. **Reference-Driven Visual Craft (Landing Pages, Dashboards, UI Interactions & 3D):**
   - Model the visual hierarchy, layout density, and interaction patterns after curated daily design reference standards covering **high-converting landing pages, data-dense operational dashboards, tactile UI micro-interactions, and 3D/interactive canvas elements**.

---

## SECTION 2: MANDATORY PRODUCTION UI/UX ESSENTIALS (CONVERTED FROM "VIBE CODER MISTAKES" TO "MUST HAVES")
Vibe coders forget these or get them wrong. You **MUST INCLUDE** all of the following in the website:

1. **High-Contrast Dark & Light Modes (Fix "Low Contrast Dark Mode"):**
   - Engineer crisp, intentional surface hierarchy with WCAG AAA text readability, distinct surface elevation tokens (e.g., `#090A0C` canvas, `#111317` elevated card, `#1E222A` crisp 1px structural borders), and high-contrast foreground typography.
2. **Mathematical, Consistent Spacing System (Fix "Inconsistent Spacing"):**
   - Enforce a strict 4px/8px spatial grid, consistent container padding, predictable section rhythm, and balanced whitespace across every breakpoint.
3. **Heavily Customized UI Primitives (Fix "Untouched `shadcn/ui` Components"):**
   - If using `shadcn/ui` or Radix primitives, you **MUST** customize them completely—custom border radii, custom focus rings, custom typography scales, custom table density, and bespoke states so they look custom-engineered rather than stock defaults.
4. **Tactile, Intentional Button & Control States (Fix "Buttons That Only Fade on Hover"):**
   - Every button and interactive control must have rich, tactile hover, active (`scale-[0.98]`), focus-visible, and disabled states using directional fills, crisp border shifts, or subtle elevation changes rather than a lazy opacity fade.
5. **Real, Interactive Product Demo Workspace (Fix "No Real Product Demos"):**
   - **MUST INCLUDE** an actual working, interactive product demo or live dashboard workspace directly on the page where users can click, filter, input data, trigger real state transitions, and experience the core product immediately.
6. **Layout-Accurate Skeleton Loaders (Fix "No Skeleton Loaders"):**
   - **MUST INCLUDE** custom shimmer/pulse **Skeleton Loaders** that mirror the exact geometry of cards, tables, charts, and lists whenever data is fetching or transitioning asynchronously.
7. **Complete Legal & Compliance Pages (Fix "No Terms of Service or Privacy Policy"):**
   - **MUST INCLUDE** dedicated, properly written **Terms of Service (`/terms`)** and **Privacy Policy (`/privacy`)** routes/views, complete with footer navigation and auth-flow consent links.

---

## SECTION 3: ANTI-VIBECODED VISUAL & COPYWRITING GUARDRAILS (WHAT TO REPLACE THEM WITH)
To keep the UI looking like an authentic, top-tier engineering product rather than an AI template, replace these overused AI tropes with intentional alternatives:

- **Color & Surface Discipline:** Instead of harsh gradients, rainbow coloring, purple-and-black themes, purple-to-blue gradients, neon colors, basic pastels, pure `#FFFFFF` backgrounds, radial background orbs, dot grids, grain textures, liquid glass everywhere, drop shadows on every box, colored left stripes on cards, or gradient hero text $\rightarrow$ **USE** solid architectural neutrals, crisp 1px structural borders, subtle surface contrast, and a disciplined 1-to-2 accent color system.
- **Typography Discipline:** Instead of defaulting to `Inter`, `Geist`, `Space Grotesk`, `Instrument Serif` (or the *Space Grotesk + Instrument Serif* combo), and instead of using serif italics for random accent words in headings $\rightarrow$ **USE** authoritative, high-craft font pairings (e.g., *Plus Jakarta Sans*, *Satoshi*, *General Sans*, *Switzer*, *Cabinet Grotesk*, paired with *JetBrains Mono* for tabular data and metrics).
- **Copywriting Discipline:** Instead of em dashes (`—`) everywhere, *"It's not X, it's Y"* sentences, generic buzzwords (*elevate, unleash, seamless, next-gen*), or emojis in headings and body copy $\rightarrow$ **USE** concrete, technical, metric-driven, declarative copywriting.
- **Layout & Iconography Discipline:** Instead of 3 identical feature cards in a row, 3 icon boxes in a row, 3 standard pricing tiers, overused Bento grids, a pill badge above every hero headline, default Lucide icons or sparkle icons (`✨`) everywhere, checkmark bullet lists, overly soft corner radius on everything, fake testimonials, mock macOS terminal windows, cursor-following lines, animated arrows, hover animations on non-interactive elements, or whole sections fading in on scroll $\rightarrow$ **USE** asymmetric editorial splits, interactive product showcases, custom SVG technical diagrams, numbered architectural ledgers (`01`, `02`, `03`), sharp/intentional geometric radii, and authentic product telemetry.

---

## SECTION 4: THE 80-POINT PRODUCTION BACKEND, DATA, SECURITY & DEVOPS ARCHITECTURE (MUST INCLUDE ALL 80)
Vibe coders build fragile frontends with zero backend engineering. You **MUST INCLUDE and ARCHITECT** all **80 production engineering concepts** below across your backend code, API routes, database layer, caching, queues, security middleware, and DevOps configurations:

### Part 1: API Resilience, Traffic Management & Concurrency (Items 1–19)
1. **Idempotency Keys (Prevent the Double-Charge Trap):** Implement an `Idempotency-Key` middleware for all mutating `POST`/`PUT`/`PATCH` requests backed by Redis atomic locks and response caching so retried requests never duplicate transactions or charges.
2. **Rate Limiting:** Implement sliding-window and token-bucket rate limiting middleware (per IP, per user ID, and per API endpoint) returning `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `Retry-After` headers.
3. **Reverse Proxies:** Include a production NGINX / Cloudflare / Envoy reverse proxy configuration handling SSL termination, request buffering, compression, and upstream routing.
4. **Connection Pooling:** Configure explicit database connection pooling (PgBouncer / Prisma Pool / SQLAlchemy Pool) with tuned `min`, `max`, `idleTimeoutMillis`, and `connectionTimeoutMillis` settings.
5. **N+1 Queries Optimization (Stop the Silent DB Killer):** Eliminate all N+1 query loops by implementing explicit SQL `JOIN`s, ORM eager preloading, and batch `DataLoader` patterns so relational fetches run in constant query count.
6. **Caching Strategies:** Implement a multi-tier Redis caching layer incorporating Cache-Aside, Write-Through, and Read-Through patterns for hot queries and session state.
7. **Cache Invalidation:** Implement deterministic cache invalidation via mutation hooks, tag/version-based key namespaces, and TTLs with random jitter to prevent cache stampedes.
8. **Load Balancing:** Configure stateless application servers behind an L7 Load Balancer supporting health-checked round-robin and least-connections routing.
9. **API Gateways:** Implement a unified API Gateway layer handling routing, request/response transformation, schema validation, and centralized auth verification.
10. **Timeouts:** Enforce strict connection, read, and execution timeouts (`AbortSignal.timeout` / query timeouts) on every database query, Redis call, and external HTTP request.
11. **Retries:** Build a resilient retry wrapper for transient network and `5xx` upstream errors on idempotent operations.
12. **Exponential Backoff:** Pair all retry mechanisms with exponential backoff and full random jitter ($t = \text{random}(0, \min(\text{maxDelay}, \text{baseDelay} \times 2^{\text{attempt}}))$).
13. **Circuit Breakers (Stop Cascading Failures):** Implement a state-machine Circuit Breaker (`CLOSED` $\rightarrow$ `OPEN` $\rightarrow$ `HALF-OPEN`) around external integrations and microservices to fail fast with fallback data when downstream services degrade.
14. **Race Conditions Prevention:** Prevent check-then-act race conditions using atomic SQL updates, database transactions (`SERIALIZABLE` / `REPEATABLE READ`), and atomic Redis Lua scripts.
15. **Deadlocks Prevention:** Enforce canonical ascending lock ordering across multi-record transactions and configure strict database `deadlock_timeout` and `lock_timeout` parameters.
16. **Memory Leaks Prevention:** Ensure all event listeners, streams, intervals, WebSocket connections, and closures are deterministically disposed, and enforce bounded LRU sizes on all in-memory stores.
17. **Webhooks:** Build a complete Webhook subsystem (both receiver and dispatcher) featuring HMAC-SHA256 signature verification, replay-attack timestamp validation, immediate `202 Accepted` acknowledgement, and async queue processing.
18. **CORS:** Configure strict Cross-Origin Resource Sharing middleware with explicit origin allowlists, credential controls, allowed headers/methods, and preflight caching.
19. **Secrets Management:** Implement centralized, strongly typed secrets management (validating env schemas at boot via Zod and integrating with AWS SSM Parameter Store / Secrets Manager / HashiCorp Vault) with zero hardcoded keys.

### Part 2: Database Engineering & Distributed Systems (Items 20–41)
20. **Database Indexing (Seek vs. Scan):** Define explicit B-Tree, composite, unique, and GIN/partial indexes in the schema so all high-frequency queries execute fast **Index Seeks** rather than full table **Scans**.
21. **Query Optimization:** Implement cursor/keyset pagination (`WHERE (created_at, id) < ($1, $2) LIMIT $3`), selective column projection, and query plans optimized for index-only scans.
22. **Read Replicas:** Configure the data access layer to separate read/write connections—sending all writes and real-time transactional reads to the Primary DB, and routing analytical/reporting queries to Read Replicas.
23. **Database Migrations:** Provide automated, reversible, version-controlled SQL migration files integrated into the deployment pipeline.
24. **Schema Versioning:** Follow the Expand-and-Contract pattern for zero-downtime schema changes so old and new application versions can run concurrently during rollouts.
25. **Optimistic Locking:** Add a `version` column to core domain models (`WHERE id = $1 AND version = $2`) to prevent lost updates without holding blocking database locks.
26. **Pessimistic Locking:** Implement explicit row-level locking (`SELECT ... FOR UPDATE NOWAIT` / `SKIP LOCKED`) for high-contention inventory, wallet, or queue-claiming transactions.
27. **Distributed Locks:** Implement Redis distributed locks (Redlock with auto-extending leases and fencing tokens) for cross-instance mutual exclusion.
28. **Sharding:** Architect tenant-aware / hash-partitioned primary keys (`shard_key` + `UUIDv7`) and routing logic ready for horizontal database sharding.
29. **Partitioning:** Implement declarative table partitioning (by date range or hash) for high-growth tables like audit logs, events, and telemetry records.
30. **Replication:** Configure primary-standby replication parameters (synchronous commit for critical ledgers; asynchronous streaming replication for read scaling).
31. **Leader Election:** Implement distributed lease-based leader election so singleton cluster coordinators and schedulers run on exactly one active node with automatic failover.
32. **CAP Theorem (Pick Two):** Explicitly architect and document the **CP** (strong consistency for auth, billing, state mutations) vs. **AP** (high availability for cached feeds, search, telemetry) boundaries across the system.
33. **Eventual Consistency:** Build background state-reconciliation workers and optimistic UI state indicators to seamlessly handle eventually consistent read models.
34. **Distributed Transactions:** Implement the **Transactional Outbox Pattern** (persisting domain changes and outbox events inside a single local ACID transaction) to guarantee atomic database-to-queue publishing.
35. **Saga Pattern:** Implement a multi-step Saga orchestrator with explicit **Compensating Transactions** to automatically undo earlier steps if a downstream step fails.
36. **Message Queues:** Integrate a durable job queue (BullMQ / RabbitMQ / SQS) for asynchronous background processing, batch jobs, and heavy compute tasks.
37. **Pub/Sub:** Implement a Publish/Subscribe event bus (Redis Pub/Sub / Kafka / SNS) for real-time fan-out notifications and decoupled module communication.
38. **Event-Driven Architecture:** Structure the backend around typed domain events (`EventEnvelope<T>`) with producer/consumer decoupling and event audit trails.
39. **Dead Letter Queues (DLQ — Handle Poison Messages):** Configure all message queues with max retry counts that automatically isolate failing "poison messages" into a Dead Letter Queue with inspection and replay endpoints.
40. **Backpressure:** Implement stream backpressure, bounded queue sizes, worker concurrency limits, and load-shedding middleware to prevent memory exhaustion under traffic spikes.
41. **Cron Jobs:** Build distributed, lock-protected, idempotent scheduled Cron Jobs with execution telemetry and timeout guards.

### Part 3: Cybersecurity, Identity & Network Protocols (Items 42–60)
42. **SQL Injection Prevention (Stop "Bobby Tables"):** Enforce 100% parameterized queries/prepared statements and strict runtime input validation across every endpoint.
43. **XSS (Cross-Site Scripting) Protection:** Configure strict `Content-Security-Policy` (CSP) headers, input sanitization, and context-aware output encoding.
44. **CSRF Protection:** Implement anti-CSRF tokens alongside `SameSite=Strict`/`Lax`, `HttpOnly`, and `Secure` cookie attributes.
45. **SSRF (Server-Side Request Forgery) Protection:** Build a hardened outbound HTTP client that validates URLs, enforces HTTPS, resolves DNS, and blocks all private/loopback/cloud-metadata IP ranges (`169.254.169.254`, `10.0.0.0/8`, `127.0.0.0/8`).
46. **OAuth 2.0 / OIDC:** Implement full OAuth 2.0 Authorization Code Flow with **PKCE**, `state` CSRF verification, and OIDC ID token validation.
47. **JWT Rotation (Prevent Stolen Token Abuse):** Implement short-lived access tokens paired with rotating refresh tokens, storing refresh token families in Redis/DB to immediately detect token reuse and revoke compromised sessions.
48. **IAM (Identity & Access Management):** Build granular Role-Based Access Control (RBAC) and policy-based resource authorization middleware.
49. **TLS:** Enforce TLS 1.3 configurations and `Strict-Transport-Security` (HSTS) headers across all ingress points.
50. **Encryption at Rest:** Implement AES-256-GCM application-level envelope encryption for sensitive database fields (PII, tokens, secrets) alongside encrypted storage volumes.
51. **Encryption in Transit:** Enforce TLS/mTLS for all client-to-server, service-to-service, database, and Redis connections.
52. **WAF (Web Application Firewall):** Provide WAF rule definitions protecting against OWASP Top 10 vectors, SQLi/XSS payloads, and scanner bots.
53. **DDoS Protection:** Implement L7 request-size limits, connection rate throttling, slow-read protection, and edge caching rules.
54. **WebSockets:** Build an authenticated WebSocket server supporting real-time bi-directional events, ping/pong heartbeat checks, room subscriptions, and auto-reconnection.
55. **Server-Sent Events (SSE):** Implement an SSE streaming endpoint (`text/event-stream`) with `Last-Event-ID` support for live real-time server-to-client updates.
56. **Long Polling:** Include a graceful Long Polling fallback handler for clients on restricted networks where WebSockets/SSE cannot establish.
57. **gRPC:** Include a `.proto` schema definition and gRPC service handler for high-performance, strongly-typed internal microservice communication.
58. **HTTP/2 & HTTP/3:** Configure server and proxy layers for HTTP/2 multiplexing and QUIC/HTTP/3 UDP transport support.
59. **TCP vs UDP:** Document and configure appropriate transport protocols across the stack (TCP for reliable transactional state; UDP/QUIC for low-latency real-time transport).
60. **DNS ("It's Always DNS"):** Provide production DNS architecture specifications including low-TTL cutover records, CAA security records, and health-checked DNS failover.

### Part 4: DevOps, Cloud Infrastructure & Runtime Reliability (Items 61–80)
61. **Docker:** Write a production multi-stage `Dockerfile` (builder stage + minimal non-root runner stage, pinned digests, `.dockerignore`) and a `docker-compose.yml` for local full-stack orchestration (App, Postgres, Redis, Worker, Proxy).
62. **Kubernetes (Win the YAML Boss Fight):** Provide complete Kubernetes manifests (`Deployment`, `Service`, `Ingress`, `ConfigMap`, `Secret`, `HorizontalPodAutoscaler`, `PodDisruptionBudget`, `NetworkPolicy`) with explicit CPU/Memory requests and limits.
63. **Helm Charts:** Structure the Kubernetes deployment as a reusable Helm Chart (`Chart.yaml`, `values.yaml`, and templates) for multi-environment templating.
64. **Service Discovery:** Configure internal DNS and environment-driven service discovery across containers and pods.
65. **CI/CD:** Write a complete GitHub Actions CI/CD workflow (`.github/workflows/ci-cd.yml`) executing linting, type-checking, unit/integration test suites, security vulnerability scanning, Docker build, and deployment.
66. **Build Caching:** Configure Docker BuildKit layer caching and package manager lockfile caching in CI for rapid build times.
67. **Infrastructure as Code (IaC):** Define all cloud infrastructure declaratively in version control.
68. **Terraform:** Provide modular Terraform configurations (`main.tf`, `variables.tf`, `outputs.tf`) with remote state locking for provisioning VPC, compute, managed DB, Redis, and IAM.
69. **Feature Flags:** Build a Feature Flag service & React hook/provider supporting percentage rollouts, environment targeting, and instant runtime kill-switches.
70. **Blue-Green Deployment:** Provide deployment routing configs supporting zero-downtime Blue-Green environment traffic switching.
71. **Canary Releases (Test on 1%):** Configure weighted Canary traffic splitting (e.g., routing 1% $\rightarrow$ 10% $\rightarrow$ 100% of live traffic) with automated metric verification.
72. **Rolling Deployments:** Configure zero-downtime rolling update parameters (`maxSurge`, `maxUnavailable`) paired with `SIGTERM` graceful server shutdown handlers that drain active connections cleanly.
73. **Rollbacks:** Include automated health-failure rollback triggers and one-command rollback scripts for both application deployments and database migrations.
74. **Health Checks:** Implement `/api/health/live` (shallow process liveness) and `/api/health/ready` (deep readiness check verifying DB pool, Redis ping, and queue health).
75. **Liveness & Readiness Probes:** Wire Kubernetes `startupProbe`, `livenessProbe`, and `readinessProbe` directly to the `/api/health/*` endpoints.
76. **Dependency Hell Prevention:** Use strict, deterministic package lockfiles, pinned dependency versions, minimal external bloat, and automated `npm audit`/`osv-scanner` checks.
77. **API Versioning:** Namespace all API endpoints under `/api/v1/...` with version negotiation and RFC-compliant `Deprecation` and `Sunset` response headers.
78. **Semantic Versioning (SemVer):** Enforce `MAJOR.MINOR.PATCH` semantic versioning across the application and API contracts.
79. **Garbage Collection & Memory Management:** Configure runtime heap flags, stream large payloads instead of buffering entire files in RAM, and prevent object retention on hot paths.
80. **Thread Safety:** Ensure thread-safe concurrency by offloading CPU-intensive operations to isolated Worker Threads/pools and using immutable state patterns.

---

## DELIVERABLE STRUCTURE
Execute your response thoroughly in 4 complete stages:
1. **Stage 1: UI/UX Design System & Component Architecture** (Typography, high-contrast color tokens, 4px/8px spacing scale, `framer-motion` spring presets, and integration plan for **Animaster Lib / Skiper UI / Vengeance UI** components).
2. **Stage 2: Full-Stack System Architecture & 80-Point Mapping** (Complete project directory tree and architectural matrix showing how all 80 backend/DB/Security/DevOps items are wired together).
3. **Stage 3: Production Backend, Database, Security & DevOps Code** (Database schema + indexes + migrations, core API middleware implementing Idempotency, Rate Limiting, Circuit Breaker, JWT Rotation, RBAC, SSRF/CSRF/XSS guards, Queue Workers + DLQ, Health Probes, `Dockerfile`, K8s/Helm YAML, Terraform, and CI/CD pipeline).
4. **Stage 4: Production Frontend Code** (High-contrast landing & application views, `framer-motion` animations, **Real Interactive Product Demo Workspace**, **Skeleton Loaders**, and **Terms of Service + Privacy Policy** views).




Gemini is AI and can make mistakes.

---

# APPENDIX B — COMPLETE FAST EXECUTION PLAYBOOK (PRESERVED)

The full existing execution playbook follows. Its prompts provide detailed acceptance criteria; execute them in order as phases of the one-shot directive above. Unlike the original stop-and-wait wording, continue through all phases without waiting for routine approval, while pausing only for genuinely destructive or externally publishing actions.

---

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


---

# END OF ONE-SHOT MASTER PROMPT
