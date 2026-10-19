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