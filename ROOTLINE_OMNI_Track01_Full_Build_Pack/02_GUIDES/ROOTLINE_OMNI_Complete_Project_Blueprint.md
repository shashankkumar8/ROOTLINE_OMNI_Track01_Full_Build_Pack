# ROOTLINE OMNI --- Complete Project Blueprint

`<box gap={2}>`{=html}
`<AsyncImage query="cinematic premium dark SRE incident intelligence command center UI with interactive microservice dependency graph, glowing cyan and violet nodes, incident root cause evidence panel, before after graph simulation, enterprise software product design" aspectRatio="16:9" width="100%" radius="xl" />`{=html}
```{=html}
<title size="2xl">
```
ROOTLINE OMNI
```{=html}
</title>
```
`<text color="secondary" size="sm">`{=html}Graph-native incident
intelligence, counterfactual investigation, and engineering
memory`</text>`{=html} **Tagline:** Investigate the incident. Challenge
the hypothesis. Change the graph. Prove the difference.
`<row gap={2} wrap="wrap">`{=html}
`<badge color="success">`{=html}Primary track: Track 01`</badge>`{=html}
`<badge>`{=html}Potential Track 02`</badge>`{=html}
`<badge>`{=html}Potential Track 03`</badge>`{=html} `</row>`{=html}
`</box>`{=html}

This document brings together the product concept, problem statement,
technical architecture, graph model, investigation algorithm, Live Graph
Surgery, memory, user interface, safety, testing, competitive
positioning, limitations, and judging strategy.

It is a full blueprint for the project. The proposed behavior and the
previously reported implementation status are distinguished where
appropriate; the blueprint itself does not prove that every feature in
the latest ZIP has passed testing.

# 1. Executive summary

**Rootline Omni is a graph-native incident investigation system that
helps engineers identify plausible root causes of software failures by
reasoning over connected service dependencies, operational evidence,
ownership information, runbooks, and previous investigations.**

Traditional incident investigation often requires engineers to jump
between dashboards, logs, deployment histories, architecture documents,
and team knowledge. A symptom may appear in one service while the
underlying failure originates several dependency hops away.

Rootline Omni represents this engineering context in FalkorDB. It
traverses the dependency graph, retrieves relevant evidence, ranks
candidate causes using documented deterministic rules, explains the
evidence behind each candidate, and identifies related operational
knowledge.

Its signature feature is **Live Graph Surgery**, a controlled
counterfactual experiment. An investigator changes a dependency edge in
an isolated copy of the graph, reruns the investigation, and compares
the actual outputs against the baseline.

The goal is not to make an AI answer sound authoritative. It is to make
the investigation **traceable, challengeable, reproducible, and
graph-dependent**.

## The core promise

-   Understand how a failure may propagate through a system.
-   Explain why one cause ranks above another.
-   Show evidence against the leading hypothesis.
-   Demonstrate what changes when a dependency changes.
-   Preserve investigation history for future engineers.
-   Return an inconclusive result when the evidence is insufficient.

## One-sentence pitch

Rootline Omni is an AI-assisted incident investigation platform powered
by FalkorDB that traces service dependencies, evaluates competing
root-cause hypotheses, and proves how graph changes affect the
investigation.

# 2. The problem Rootline solves

Imagine an e-commerce platform where checkout requests begin returning
HTTP 504 errors.

The on-call engineer sees three clues:

-   Checkout latency is increasing.
-   The payment service was deployed recently.
-   The Redis connection pool is exhausted.

The recent payment deployment is an obvious suspect. But it may be a red
herring. Redis might be the underlying bottleneck, and the failure might
reach checkout through several connected services.

The engineer must answer five questions:

1.  Where does the failure appear?
2.  Which connected services could explain it?
3.  What evidence supports or contradicts each hypothesis?
4.  Which users or downstream services may be affected?
5.  Who owns the relevant component, and what should the engineer
    inspect next?

Without connected context, the investigation is fragmented. A language
model may summarize the available text but cannot safely infer a
dependency that is not actually present in the system.

Rootline Omni connects these facts into a graph that can be queried and
experimentally changed.

## Problem versus solution

  -----------------------------------------------------------------------
  Existing challenge                  Rootline Omni response
  ----------------------------------- -----------------------------------
  Service relationships are difficult Multi-hop dependency traversal
  to follow                           

  A symptom has several possible      Candidate ranking and evidence
  causes                              comparison

  Recent deployments create           Supporting and contradictory
  misleading correlations             evidence

  The failure may affect multiple     Blast-radius analysis
  downstream services                 

  Ownership and remediation           Graph-backed Company Brain
  instructions are scattered          

  Previous incident knowledge is      Persistent investigation memory
  forgotten                           

  AI conclusions are difficult to     Evidence provenance and explicit
  challenge                           graph paths

  Graph visualizations do not prove   Live Graph Surgery with
  database necessity                  before/after comparison
  -----------------------------------------------------------------------

A critical distinction: a dependency path is evidence of a possible
propagation route, not proof of causality. Rootline must combine graph
connectivity with operational evidence and uncertainty handling.

# 3. Who uses it?

`<box gap={3}>`{=html} `<row align="start" gap={3}>`{=html}
`<AsyncImage query="site reliability engineer monitoring production service incident dashboard multiple screens" aspectRatio="4:3" maxWidth="112px" radius="lg" />`{=html}
`<box flex="1" gap={1}>`{=html} **SRE and on-call engineers**

      Investigate failures, compare candidate causes, inspect dependency paths, and identify the next useful check.
    </box>

`</row>`{=html} `<row align="start" gap={3}>`{=html}
`<AsyncImage query="backend software engineer reviewing microservice architecture diagram on monitor" aspectRatio="4:3" maxWidth="112px" radius="lg" />`{=html}
`<box flex="1" gap={1}>`{=html} **Backend and platform engineers**

      Understand service relationships, ownership, architecture decisions, and downstream impact.
    </box>

`</row>`{=html} `<row align="start" gap={3}>`{=html}
`<AsyncImage query="engineering incident commander reviewing incident response dashboard with team" aspectRatio="4:3" maxWidth="112px" radius="lg" />`{=html}
`<box flex="1" gap={1}>`{=html} **Incident commanders and engineering
leads**

      Review the evidence, uncertainty, investigation history, and decisions made during an incident.
    </box>

`</row>`{=html} `</box>`{=html}

The first version should focus on one user: **the engineer investigating
a production-like incident**. This keeps the product coherent and the
demo focused.

# 4. The product experience

The following six capabilities form one incident investigation workflow,
not six separate products.

`<box gap={3}>`{=html} `<row align="start" gap={3}>`{=html}
`<AsyncImage query="dark enterprise SRE incident war room dashboard incident severity status affected service cards interactive dependency graph" aspectRatio="4:3" maxWidth="136px" radius="lg" />`{=html}
`<box flex="1" gap={1}>`{=html} **01. Incident War Room**

      Select an incident, inspect its severity and affected service, run an investigation, and explore the dependency topology.
    </box>

`</row>`{=html} `<divider color="subtle" />`{=html}
`<row align="start" gap={3}>`{=html}
`<AsyncImage query="premium dark incident evidence comparison dashboard competing root cause hypotheses supporting contradicting telemetry evidence score cards" aspectRatio="4:3" maxWidth="136px" radius="lg" />`{=html}
`<box flex="1" gap={1}>`{=html} **02. Evidence Court**

      Compare candidate causes, score components, supporting observations, contradictory observations, and graph paths. A candidate can lose rank when relevant evidence contradicts it.
    </box>

`</row>`{=html} `<divider color="subtle" />`{=html}
`<row align="start" gap={3}>`{=html}
`<AsyncImage query="dark interactive graph editor comparing baseline and simulated microservice dependency paths removed edge dashed red highlighted rerouted path amber" aspectRatio="4:3" maxWidth="136px" radius="lg" />`{=html}
`<box flex="1" gap={1}>`{=html} **03. Live Graph Surgery**

      Remove a dependency in a simulation, rerun the same investigation, and visualize the difference in paths, candidate ranking, and affected services.
    </box>

`</row>`{=html} `<divider color="subtle" />`{=html}
`<row align="start" gap={3}>`{=html}
`<AsyncImage query="dark developer operations workflow trace dashboard stages with actual tool execution timing status and result panels" aspectRatio="4:3" maxWidth="136px" radius="lg" />`{=html}
`<box flex="1" gap={1}>`{=html} **04. Investigation Trace**

      Display the actual backend operations that produced the result, including their outputs, status, and measured durations.
    </box>

`</row>`{=html} `<divider color="subtle" />`{=html}
`<row align="start" gap={3}>`{=html}
`<AsyncImage query="dark enterprise engineering knowledge graph showing service ownership teams runbook documents and architecture decision records" aspectRatio="4:3" maxWidth="136px" radius="lg" />`{=html}
`<box flex="1" gap={1}>`{=html} **05. Company Brain**

      Retrieve service owners, runbooks, and architecture decisions from graph relationships.
    </box>

`</row>`{=html} `<divider color="subtle" />`{=html}
`<row align="start" gap={3}>`{=html}
`<AsyncImage query="dark incident history dashboard saved investigation timeline previous decisions graph connected memory records" aspectRatio="4:3" maxWidth="136px" radius="lg" />`{=html}
`<box flex="1" gap={1}>`{=html} **06. Investigation Memory**

      Save an investigation and its human-reviewed decision, then retrieve relevant historical knowledge during a later investigation.
    </box>

`</row>`{=html} `</box>`{=html}

## Suggested user journey

1.  Select `INC-2026-101`.
2.  Click **Investigate**.
3.  Inspect the dependency graph and ranked candidates.
4.  Open the leading candidate to see its evidence and owner.
5.  Run Live Graph Surgery on a selected dependency.
6.  Compare the baseline and simulated results.
7.  Save a decision.
8.  Open investigation history and retrieve the saved result.

This is the central end-to-end story that the product should deliver
reliably.

# 5. System architecture

`<box border radius="xl" padding={3} gap={2} align="center">`{=html}
`<box background="surface-secondary" radius="lg" padding={3} width="100%" align="center" gap={1}>`{=html}
`<icon name="monitor" size="xl" />`{=html} **React + Vite frontend**
`<text color="secondary" size="sm" textAlign="center">`{=html}War Room ·
Evidence Court · Surgery · Company Brain · History`</text>`{=html}
`</box>`{=html}
`<icon name="arrow-down" color="secondary" size="lg" />`{=html}
`<box border radius="lg" padding={3} width="100%" align="center" gap={1}>`{=html}
`<icon name="workflow" size="xl" />`{=html} **FastAPI application**
`<text color="secondary" size="sm" textAlign="center">`{=html}Request
validation · investigation orchestration · response
contracts`</text>`{=html} `</box>`{=html}
`<icon name="arrow-down" color="secondary" size="lg" />`{=html}
`<grid columns={2} gap={2}>`{=html} `<grid-item>`{=html}
`<box background="surface-secondary" radius="lg" padding={3} align="center" gap={1}>`{=html}
`<icon name="git-branch" size="lg" />`{=html} **Graph query layer**
`<text size="xs" color="secondary" textAlign="center">`{=html}Dependencies
· ownership · evidence · history`</text>`{=html} `</box>`{=html}
`</grid-item>`{=html} `<grid-item>`{=html}
`<box background="surface-secondary" radius="lg" padding={3} align="center" gap={1}>`{=html}
`<icon name="scale" size="lg" />`{=html} **Reasoning engine**
`<text size="xs" color="secondary" textAlign="center">`{=html}Scoring ·
uncertainty · guardrails`</text>`{=html} `</box>`{=html}
`</grid-item>`{=html} `</grid>`{=html}
`<icon name="arrow-down" color="secondary" size="lg" />`{=html}
`<box background="rgba(40,170,150,0.10)" border={{size:1,color:"rgba(40,170,150,0.45)"}} radius="lg" padding={3} width="100%" align="center" gap={1}>`{=html}
`<icon name="database" size="xl" />`{=html} **FalkorDB**
`<text color="secondary" size="sm" textAlign="center">`{=html}Engineering
graph · investigations · decisions · simulation state`</text>`{=html}
`</box>`{=html} `</box>`{=html}

### Component responsibilities

  -----------------------------------------------------------------------
  Component                           Responsibility
  ----------------------------------- -----------------------------------
  React frontend                      Renders incidents, graph paths,
                                      evidence, simulation comparisons,
                                      and memory

  FastAPI                             Validates requests, orchestrates
                                      tools, and returns structured
                                      results

  Query layer                         Executes reviewed Cypher queries
                                      and handles graph operations

  Investigation engine                Collects context and ranks
                                      candidates using deterministic
                                      rules

  Simulation engine                   Creates an isolated graph copy,
                                      changes its topology, reruns the
                                      investigation, and cleans up

  FalkorDB                            Supplies connected context and
                                      persistent graph records

  Optional LLM                        Explains structured results if
                                      implemented; not required for the
                                      core ranking
  -----------------------------------------------------------------------

The graph is supposed to be a core computational component. This aligns
with the official hackathon requirement that FalkorDB must perform
essential work rather than merely render a visualization.
`<Cite refs={["turn340215search0","turn340215search6"]}/>`{=html}

# 6. Graph data model

The graph model represents the operational environment and the
investigation history.

The exact labels and relationship names must match the actual code. The
following is a conceptual reference schema; do not rename the existing
schema simply to match this document.

## Core entities

  -----------------------------------------------------------------------
  Entity                  Purpose                 Example
  ----------------------- ----------------------- -----------------------
  `Incident`              A production-like       Checkout 504s
                          failure                 

  `Service`               A software component    `checkout-web`

  `Evidence`              An operational          Connection-pool
                          observation             exhaustion

  `Deployment`            A version change        Payment API v2.4

  `Team`                  Service ownership       Payments team

  `Runbook`               Operational procedure   Redis failover

  `ADR`                   Architecture decision   Cache connection policy
                          record                  

  `Investigation`         A completed             Candidate rankings and
                          investigation           outcome

  `Simulation`            An audit record of a    Edge removal and result
                          what-if experiment      comparison
  -----------------------------------------------------------------------

## Example relationships

`<box border radius="lg" padding={3} gap={2}>`{=html}
`<box background="surface-secondary" radius="md" padding={2} align="center">`{=html}
**Incident** `</box>`{=html} `<row justify="center">`{=html}
`<icon name="arrow-down" size="lg" color="secondary" />`{=html}
`</row>`{=html}
`<box border radius="md" padding={2} align="center">`{=html} **Affected
Service** `</box>`{=html} `<row justify="center">`{=html}
`<icon name="arrow-down" size="lg" color="secondary" />`{=html}
`</row>`{=html}
`<box background="surface-secondary" radius="md" padding={2} align="center">`{=html}
**Dependency → Evidence → Deployment** `</box>`{=html}
`<divider />`{=html}
`<text size="sm" color="secondary">`{=html}Additional connected
context`</text>`{=html} `<grid columns={2} gap={2}>`{=html}
`<grid-item>`{=html}
`<box border radius="md" padding={2} align="center">`{=html}Service →
Team`</box>`{=html} `</grid-item>`{=html} `<grid-item>`{=html}
`<box border radius="md" padding={2} align="center">`{=html}Service →
Runbook`</box>`{=html} `</grid-item>`{=html} `<grid-item>`{=html}
`<box border radius="md" padding={2} align="center">`{=html}Service →
ADR`</box>`{=html} `</grid-item>`{=html} `<grid-item>`{=html}
`<box border radius="md" padding={2} align="center">`{=html}Investigation
→ Simulation`</box>`{=html} `</grid-item>`{=html} `</grid>`{=html}
`</box>`{=html}

A possible Cypher model is:

``` cypher
(:Incident)-[:REPORTED_ON]->(:Service)
(:Service)-[:DEPENDS_ON]->(:Service)
(:Service)-[:EXHIBITS]->(:Evidence)
(:Service)-[:HAD_DEPLOYMENT]->(:Deployment)
(:Team)-[:MAINTAINS]->(:Service)
(:Runbook)-[:APPLIES_TO]->(:Service)
(:ADR)-[:GOVERNS]->(:Service)
(:Investigation)-[:INVESTIGATED]->(:Incident)
```

The exact direction of every relationship must be documented and used
consistently in queries.

### Why graph relationships matter

Suppose:

``` text
checkout-web → payments-api → cache-redis
inventory-service ───────────→ cache-redis
```

If checkout depends on payments, which depends on Redis, there is a
possible path from the cache to checkout's symptoms.

If the inventory-to-cache edge is removed, the checkout path can still
remain through payments. This is precisely the type of redundancy that
makes Live Graph Surgery interesting.

# 7. The investigation algorithm

The engine should be deterministic for the same graph, evidence, and
rules version.

`<list marker="number" gap={2}>`{=html} `<list-item>`{=html}**Load
incident context.** Retrieve the incident, affected service, and current
status.`</list-item>`{=html} `<list-item>`{=html}**Traverse
dependencies.** Find relevant multi-hop paths through the
graph.`</list-item>`{=html} `<list-item>`{=html}**Collect evidence.**
Retrieve observations, deployments, and connected service
evidence.`</list-item>`{=html} `<list-item>`{=html}**Identify
candidates.** Build the set of plausible causes from relevant connected
data.`</list-item>`{=html} `<list-item>`{=html}**Evaluate evidence.**
Separate supporting facts from contradictory facts and missing
information.`</list-item>`{=html} `<list-item>`{=html}**Rank
candidates.** Apply a documented scoring function.`</list-item>`{=html}
`<list-item>`{=html}**Calculate blast radius.** Identify affected
dependent services using the correct edge
direction.`</list-item>`{=html} `<list-item>`{=html}**Resolve
operational context.** Retrieve owners, runbooks, and architecture
decisions.`</list-item>`{=html} `<list-item>`{=html}**Retrieve
historical knowledge.** Look up relevant prior investigations and
decisions.`</list-item>`{=html} `<list-item>`{=html}**Return the
result.** Include evidence paths, score components, uncertainty, and
suggested next checks.`</list-item>`{=html} `</list>`{=html}

## Scoring model

A simple illustrative heuristic is:

\[ S(c)=`\sum`{=tex}\_i w_i e_i(c)-`\sum`{=tex}\_j v_j d_j(c) \]

Where:

-   \(c\) is a candidate cause.
-   (e_i(c)) is supporting evidence for the candidate.
-   (d_j(c)) is contradictory evidence.
-   (w_i) and (v_j) are documented weights.

The actual implementation should define evidence freshness, duplicate
handling, missing information, and the meaning of each weight.

**A score is a ranking, not proof of causality.** Do not display it as a
calibrated probability unless you have validated it against appropriate
labeled data.

## Handling uncertainty

The system should distinguish:

-   **Strongly supported candidate:** multiple relevant signals support
    it and major contradictions are absent.
-   **Plausible candidate:** some support exists, but important
    questions remain.
-   **Inconclusive:** evidence is insufficient or conflicting.
-   **Investigation failed:** a technical failure prevented a reliable
    result.

An inconclusive answer is different from an API error. This distinction
makes the product more trustworthy.

# 8. Live Graph Surgery: the flagship feature

This is the strongest technical demonstration in the product.

## What it does

The user chooses a dependency edge to remove in an isolated simulation
graph. The application reruns the same investigation against the
simulated topology and compares the outputs.

It answers:

> If this relationship did not exist, would the investigation reach the
> same conclusion?

## Execution flow

`<box border radius="lg" padding={3} gap={2} align="center">`{=html}
`<box background="surface-secondary" radius="md" padding={3} width="100%" align="center">`{=html}
**1. Capture baseline**
`<text color="secondary" size="sm" textAlign="center">`{=html}Paths ·
rankings · topology`</text>`{=html} `</box>`{=html}
`<icon name="arrow-down" color="secondary" />`{=html}
`<box border radius="md" padding={3} width="100%" align="center">`{=html}
**2. Copy the graph**
`<text color="secondary" size="sm" textAlign="center">`{=html}Create
isolated simulation state`</text>`{=html} `</box>`{=html}
`<icon name="arrow-down" color="secondary" />`{=html}
`<box border radius="md" padding={3} width="100%" align="center">`{=html}
**3. Mutate one edge**
`<text color="secondary" size="sm" textAlign="center">`{=html}Validate
the selected relationship`</text>`{=html} `</box>`{=html}
`<icon name="arrow-down" color="secondary" />`{=html}
`<box border radius="md" padding={3} width="100%" align="center">`{=html}
**4. Rerun investigation**
`<text color="secondary" size="sm" textAlign="center">`{=html}Use the
same query and scoring rules`</text>`{=html} `</box>`{=html}
`<icon name="arrow-down" color="secondary" />`{=html}
`<box background="rgba(40,170,150,0.10)" border={{size:1,color:"rgba(40,170,150,0.45)"}} radius="md" padding={3} width="100%" align="center">`{=html}
**5. Compare and clean up**
`<text color="secondary" size="sm" textAlign="center">`{=html}Diff the
results, verify baseline, delete simulation`</text>`{=html}
`</box>`{=html} `</box>`{=html}

## Three important experiments

  -----------------------------------------------------------------------
  Experiment                          Expected behavior
  ----------------------------------- -----------------------------------
  Remove a relevant edge              The relevant path or investigation
                                      result changes if that edge
                                      participates in the query

  Remove a redundant edge             The result may remain unchanged
                                      because another path exists

  Remove an unrelated edge            The investigation should remain
                                      stable if the changed relationship
                                      is genuinely irrelevant
  -----------------------------------------------------------------------

A good demo uses all three cases. It shows that the system responds to
meaningful graph changes without inventing a difference when nothing
relevant has changed.

## Safety requirements

-   Never mutate the production or baseline graph for a what-if
    experiment.
-   Validate the source node, target node, and relationship.
-   Use an isolated copy with a unique simulation identifier.
-   Ensure the simulation is deleted after success or failure.
-   Report cleanup status separately from baseline verification.
-   Compare the actual dependency-edge set before and after.
-   Do not claim the entire database is unchanged if an audit record was
    deliberately added.
-   Fail clearly if the configured FalkorDB version does not support the
    required graph-copy operation.

The project should not silently fall back to an incomplete clone that
omits previous investigations or evidence.

# 9. Company Brain and investigation memory

These two features complement the investigation engine.

## Company Brain

For a candidate cause, the application should retrieve:

-   The owning team.
-   The relevant runbook.
-   Any applicable architecture decision.
-   The relationship connecting each item to the affected service.

A runbook should contain actual, readable synthetic instructions. A dead
placeholder URL should not be presented as a working integration.

For example, a Redis runbook might instruct an engineer to inspect
connection-pool saturation, validate Redis health, compare request
latency with pool utilization, and follow the team's approved failover
procedure.

It should not execute a dangerous remediation command automatically.

## Investigation memory

Memory stores previous investigations and human-reviewed decisions in
FalkorDB.

A later investigation can retrieve relevant history, but a previous
decision is not automatically correct for a new incident. The system
should preserve its timestamp, incident context, and decision status.

The key test is simple:

1.  Save a decision.
2.  Start another investigation.
3.  Retrieve the previous decision through graph queries.
4.  Display the source and explain its relevance.

A history page that only reads browser state is not equivalent to
persistent graph-backed memory.

# 10. The AI-agent question

The hackathon is about agents with graph context, so the implementation
must be precise about what is autonomous and what is deterministic.

A deterministic investigation workflow is useful, but renaming its
functions to `TopologyAgent`, `EvidenceAgent`, and `ArbiterAgent` does
not create autonomous agents.

A genuine agent-style implementation would have a coordinator that
chooses among approved tools based on the current state and returned
evidence. For example:

-   If the dependency path is missing, inspect related services.
-   If two candidates have similar scores, collect additional evidence.
-   If a relevant path is broken, inspect alternative paths.
-   If evidence remains insufficient, return an inconclusive result.
-   If a prior decision is retrieved, check its context before using it.

These transitions must exist in code and be testable.

The LLM, if used, should not invent graph paths, owners, evidence, or
scores. It may explain structured facts or select an approved next tool
under defined constraints.

**Recommended description until autonomous selection is verified:**
"Graph-backed incident investigation with a deterministic orchestration
workflow."

That is more defensible than an unsupported multi-agent claim.

# 11. Technical stack and repository structure

The proposed stack is:

  Technology                           Purpose
  ------------------------------------ ------------------------------------------
  React + Vite                         Interactive frontend
  Existing styling system / Tailwind   Consistent visual design
  Python + FastAPI                     Backend API and orchestration
  FalkorDB                             Primary graph database
  Cypher                               Graph traversal, retrieval, and mutation
  Deterministic Python logic           Ranking and guardrails
  pytest                               Backend tests
  Frontend build/tests                 UI integration and release verification

A clean repository should make the architecture easy to inspect. For
example:

``` text
rootline/
├── backend/
│   ├── main.py
│   ├── queries.py
│   ├── investigator.py
│   ├── surgery.py
│   ├── seed.py
│   └── ...
├── frontend/
│   ├── src/
│   ├── package.json
│   └── ...
├── docs/
│   ├── graph-model.md
│   ├── runbooks.md
│   └── BUILD_STATUS.md
├── tests/
├── README.md
├── requirements.txt
└── requirements-dev.txt
```

This is an illustrative structure; retain the actual repository
structure if it already works.

# 12. Test strategy

A serious submission needs tests that prove behavior, not merely
successful imports.

## Graph correctness

-   Seed data can be loaded reproducibly.
-   Multi-hop paths are correct.
-   Blast-radius traversal respects edge direction.
-   Missing incidents return controlled responses.

## Ranking

-   Identical inputs produce identical rankings.
-   Supporting evidence affects the appropriate candidate.
-   Contradictory evidence is handled as documented.
-   Missing evidence can result in an inconclusive outcome.

## Graph Surgery

-   A relevant edge changes the expected result.
-   A redundant edge does not necessarily change the result.
-   An unrelated edge does not change an unrelated investigation.
-   The baseline topology is preserved.
-   A failed simulation does not leave a temporary graph behind.

## Memory and Company Brain

-   Saved decisions survive the relevant persistence boundary.
-   Prior decisions can be retrieved in a later investigation.
-   Owners and runbooks come from graph relationships.
-   Missing records are shown as missing rather than invented.

## Application reliability

-   Invalid inputs are rejected.
-   Database errors are handled.
-   Failed API requests do not crash the UI.
-   Frontend text is rendered safely.
-   No database credentials are shipped to the browser.

The reported 31-test result is encouraging, but a fresh test run on the
actual target environment remains necessary before claiming final
verification.

# 13. UI and design specification

Use a polished, restrained command-center design rather than an
overloaded dashboard.

`<box gap={2}>`{=html} `<row align="center" gap={2}>`{=html}
`<box background="surface-secondary" radius="md" padding={2}>`{=html}
`<icon name="layout-dashboard" size="lg" />`{=html} `</box>`{=html}
`<box flex="1" gap={1}>`{=html} **Left navigation**

      Incidents, investigations, Company Brain, and history.
    </box>

`</row>`{=html} `<row align="center" gap={2}>`{=html}
`<box background="surface-secondary" radius="md" padding={2}>`{=html}
`<icon name="network" size="lg" />`{=html} `</box>`{=html}
`<box flex="1" gap={1}>`{=html} **Central canvas**

      Dependency topology with selectable nodes, labeled edges, and clear visual distinction between baseline and simulation.
    </box>

`</row>`{=html} `<row align="center" gap={2}>`{=html}
`<box background="surface-secondary" radius="md" padding={2}>`{=html}
`<icon name="list-check" size="lg" />`{=html} `</box>`{=html}
`<box flex="1" gap={1}>`{=html} **Evidence panel**

      Ranked candidates, score breakdown, supporting and contradictory evidence, owner, and runbook.
    </box>

`</row>`{=html} `<row align="center" gap={2}>`{=html}
`<box background="surface-secondary" radius="md" padding={2}>`{=html}
`<icon name="git-compare" size="lg" />`{=html} `</box>`{=html}
`<box flex="1" gap={1}>`{=html} **Simulation panel**

      Edge selector, run simulation, path comparison, result diff, and cleanup status.
    </box>

`</row>`{=html} `</box>`{=html}

The application should include loading, error, empty, inconclusive, and
simulation-failure states. Use real graph layout logic or stable
coordinates based on actual node data, not fixed positions that break
when the topology changes.

# 14. Pros and cons

## Pros

-   The incident-investigation problem naturally depends on connected
    data.
-   FalkorDB can materially affect the investigation, not just the
    visualization.
-   Graph Surgery provides a distinctive, observable experiment.
-   Evidence paths and score components improve explainability.
-   Persistent investigation memory helps preserve operational
    knowledge.
-   The deterministic core can work without paid LLM APIs.
-   The same architecture can later support additional incident
    categories and telemetry integrations.

## Cons and limitations

  -----------------------------------------------------------------------
  Limitation              Why it matters          Mitigation
  ----------------------- ----------------------- -----------------------
  Graph data can be       A missing dependency    Track data freshness
  incomplete              can hide a real failure and missing
                          path                    relationships

  Synthetic incidents are The demo does not prove Disclose the data
  simplified              production accuracy     source and test against
                                                  real authorized
                                                  incidents later

  Heuristic ranking is    A high score can still  Show evidence,
  not causality           be wrong                uncertainty, and
                                                  limitations

  Graph copying is        Simulation can fail on  Verify the actual
  version-dependent       a target environment    FalkorDB deployment and
                                                  fail safely

  Memory can become stale Historical decisions    Preserve timestamps and
                          may no longer apply     context

  Agent behavior may be   A deterministic         Implement genuine tool
  limited                 workflow may not        selection or describe
                          satisfy every           the current
                          interpretation of an    architecture honestly
                          agent track             

  Production security is  An incident platform    Add authentication,
  not automatic           may expose sensitive    authorization, and
                          operational information audit controls before
                                                  real deployment

  Scope can expand        More integrations and   Keep the core workflow
  indefinitely            agents may delay a      small and complete
                          working submission      
  -----------------------------------------------------------------------

These limitations can be managed, but they cannot all be eliminated by
design alone.

# 15. Competitive positioning

The broader graph-agent field is competitive. Public Graph Hacks
examples include projects focused on graph-backed episodic memory,
multi-agent coordination, and company knowledge.
`<Cite refs={["turn340215search1","turn340215search5","turn340215search8"]}/>`{=html}

Rootline's strongest positioning is not "we use AI and a graph." It is:

> **We can experimentally challenge an incident investigation by
> changing the graph and observing the actual difference in the
> result.**

That positioning is defensible only if the demonstration shows real
backend results and the graph-copy safety checks work.

Do not claim that no competing project has graph mutation, what-if
analysis, or related techniques without a comprehensive comparison. A
public search is useful for competitive context, not proof of
uniqueness.

# 16. Alignment with the Graph Hacks tracks

The official rules require FalkorDB to be central to the product, a
public repository, a README containing setup and the graph model,
relevant Cypher queries or algorithms, a demo video, deployment or local
setup instructions, track declarations, and AI-assistance disclosure.
`<Cite refs={["turn340215search0","turn340215search6"]}/>`{=html}

  -----------------------------------------------------------------------
  Track                   Fit                     What must be
                                                  demonstrated
  ----------------------- ----------------------- -----------------------
  Track 01: Agents That   **Primary**             Graph-dependent
  Act on Connected Data                           investigation,
                                                  multi-hop paths,
                                                  evidence-based
                                                  decisions, and actual
                                                  tool orchestration

  Track 02: Agent Memory  Conditional             Retrieval of saved
  and Coordination                                investigations or
                                                  decisions in later
                                                  sessions, with real
                                                  memory use

  Track 03: Company Brain Conditional             Graph-backed ownership,
                                                  runbooks, and
                                                  architecture decisions
                                                  that answer meaningful
                                                  questions
  -----------------------------------------------------------------------

My recommendation remains **Track 01 as primary**. Add Tracks 02 and 03
only if the implementation supports them and you can defend the
additional claims.

# 17. Final three-minute demo

The video should follow a single investigation from beginning to end.

`<list marker="number" gap={2}>`{=html} `<list-item>`{=html}**0:00--0:25
--- Problem.** Show checkout errors and multiple plausible
causes.`</list-item>`{=html} `<list-item>`{=html}**0:25--1:00 ---
Investigation.** Run the query and show the real path, candidate
ranking, contradictory evidence, and relevant
owner.`</list-item>`{=html} `<list-item>`{=html}**1:00--1:40 --- Graph
Surgery.** Remove a relevant dependency, rerun, and show the changed
result.`</list-item>`{=html} `<list-item>`{=html}**1:40--2:05 ---
Negative case.** Remove an irrelevant dependency and show that the
result stays stable. Verify the baseline remains
unchanged.`</list-item>`{=html} `<list-item>`{=html}**2:05--2:25 ---
Memory.** Retrieve a saved investigation or decision and show its
graph-backed source.`</list-item>`{=html}
`<list-item>`{=html}**2:25--3:00 --- Technical proof.** Show the graph
model, relevant Cypher, test output, setup instructions, and
limitations.`</list-item>`{=html} `</list>`{=html}

Use only working interactions and actual measured results. Do not claim
production accuracy, calibrated confidence, or a particular performance
number unless it has been verified.

# 18. Final implementation priorities

`<box gap={3}>`{=html} `<row align="start" gap={3}>`{=html}
`<badge color="success">`{=html}P0`</badge>`{=html}
`<box flex="1" gap={1}>`{=html} **Must work** - Graph-backed
investigation and correct paths - Evidence ranking and uncertainty -
Reversible graph simulation - Baseline isolation and cleanup -
Persistent decisions and graph-dependent memory - README, tests, and
reproducible setup `</box>`{=html} `</row>`{=html}
`<divider color="subtle" />`{=html} `<row align="start" gap={3}>`{=html}
`<badge>`{=html}P1`</badge>`{=html} `<box flex="1" gap={1}>`{=html}
**Polish if time permits** - Clear before/after topology visualization -
In-app runbook and ADR details - Strong loading and error states -
Accurate stage trace - Improved graph layout and keyboard accessibility
`</box>`{=html} `</row>`{=html} `<divider color="subtle" />`{=html}
`<row align="start" gap={3}>`{=html} `<badge>`{=html}P2`</badge>`{=html}
`<box flex="1" gap={1}>`{=html} **Future work** - Real telemetry
integrations - Calibrated ranking evaluation - Authentication and
role-based permissions - Genuine LLM-driven tool selection - Additional
incident categories and advanced graph algorithms `</box>`{=html}
`</row>`{=html} `</box>`{=html}

Do not expand the scope until the P0 path is verified end to end.

# 19. Final conclusion

Rootline Omni is a compelling project direction because it combines a
real engineering problem with a testable graph-native mechanism.

Its most important capability is not the number of dashboard panels or
the number of AI agents. It is the ability to run an investigation,
change the graph in a controlled simulation, and show how the actual
result changes---or remains stable---because of the connected data.

That gives the project a clear technical story:

**Investigate → trace evidence → challenge the hypothesis → change the
graph → rerun → compare → preserve the decision.**

This is the version I would defend before judges. It is ambitious enough
to be memorable, but its credibility depends on correct graph behavior,
safe simulation, honest agent claims, and a reliable end-to-end demo.

The final principle is simple: **make every major claim observable in
the running application.** If a feature cannot be demonstrated or
explained from the code, label it as future work rather than presenting
it as complete.
