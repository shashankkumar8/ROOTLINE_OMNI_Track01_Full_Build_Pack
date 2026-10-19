# ROOTLINE OMNI — Premium Frontend Transformation Master Prompt

## Role and objective

Act as a principal product designer, senior frontend engineer, and design-systems lead. Upgrade the EXISTING ROOTLINE OMNI application into a distinctive, production-quality, competition-ready interface. This is a redesign of the current product, not a new starter template.

The visual references supplied by the user establish these principles:
- Avoid generic “vibe-coded” styling: no harsh gradients, purple/black cliché, rainbow coloring, neon overload, gratuitous shadows, emoji icons, glassmorphism, radial orbs, dot-grid backgrounds, sparkle icons, animated arrows, pastel overload, or decorative motion.
- Avoid template patterns: three generic feature cards in a row, bento grids used without a reason, pricing tiers, fake testimonials, fake counters, generic hero copy, terminal-window decoration, and “it’s not X, it’s Y” marketing copy.
- Typography, whitespace, composition, and evidence should do the work.
- Use a real product demonstration rather than a static marketing mockup.
- A serious product needs real Privacy Policy and Terms pages, clear scope/limitations, and no fake trust signals.
- Motion should explain state changes, not merely decorate the page.

The premium website reference suggests a deliberate design process: inspect the current product, set a clear typography system, audit spacing, add purposeful interaction, frame real evidence/case studies, and conduct a trust/completeness pass.

## Non-negotiable project constraints

1. Work in the existing repository and inspect it before changing anything. Do not scaffold a replacement app or discard existing work.
2. Preserve existing APIs, routes, backend behavior, FalkorDB integration, data model, graph traversal/investigation logic, and tests unless a change is required and verified.
3. Preserve ROOTLINE OMNI’s core differentiator: **Live Graph Surgery** — run an investigation against a temporary isolated graph, remove or alter a dependency edge in that temporary graph, rerun the same investigation, compare outcomes, verify the baseline topology did not change, and clean up the temporary graph even on errors.
4. The graph is the product, not a decorative illustration. Use real API data and actual graph state. Do not replace functionality with hardcoded frontend mock data.
5. Data currently used for demonstrations is synthetic. Label it honestly and prominently enough to prevent confusion. Scores are heuristic signals, not calibrated probabilities. Do not claim production telemetry, causal certainty, automatic remediation, or enterprise adoption unless the repository contains evidence.
6. Do not fake customers, testimonials, uptime, incident counts, savings, benchmark results, live status, or security certifications.
7. No “Made with AI” badge or similar attribution tag.
8. Maintain working local development, frontend production build, API health, tests, and the submission ZIP. Do not put `.env`, credentials, API keys, `.venv`, `node_modules`, `.git`, caches, or local secrets into the ZIP.
9. Do not push to GitHub, publish, deploy publicly, or submit to the hackathon on the user’s behalf.
10. Antigravity is the code editor. Make changes directly in the current workspace, not merely in a report or plan.

## First: audit before implementation

Inspect:
- repository tree, `README`, `package.json`, Vite configuration, frontend routes/components/styles, API client/base URL, backend routes, graph operations, tests, Privacy/Terms implementation, and ZIP packaging script or instructions;
- the current app running locally, if available;
- which APIs are real, which views are connected, and which states are missing.

Create a concise baseline checklist before editing. Identify any mismatch between claims in documentation and actual implementation. In particular, verify whether `/privacy` and `/terms` are real navigable routes rather than a single disclosure modal. Do not claim a route is verified unless you open/test it.

## Visual direction: “quietly exceptional systems software”

The experience should feel like a carefully art-directed infrastructure investigation tool used by experienced engineers during a real incident. It should be calm, technical, editorial, and unmistakably designed.

### Palette
Use a restrained neutral foundation with one controlled signal accent:
- warm or cool off-white / paper-like surface for the main workspace;
- deep charcoal / ink for high-contrast text and selected dark surfaces;
- neutral grays for borders, labels, secondary copy, and inactive states;
- one restrained signal color (for example, muted amber or a disciplined blue) for focus and active investigative actions;
- reserve red for actual critical/error states, green for verified/success states, and amber for warnings.
Do not make the entire app purple/black, neon, rainbow, or gradient-led. Avoid large decorative gradients. Verify contrast rather than relying on color alone.

### Typography
- Establish a clear type scale and consistent line-height.
- Use one well-chosen sans-serif family for UI and, optionally, a restrained monospace family for IDs, timestamps, trace values, and technical metadata.
- Avoid using Inter/Geist/Space Grotesk by default just because they are fashionable. Choose fonts based on the current project’s assets and reliable loading. If using a web font, provide a sensible system fallback and avoid blocking first render.
- Use strong hierarchy, short labels, readable body copy, and tabular numerals for changing metrics.

### Layout and components
- No default three-card feature row and no bento layout unless the content genuinely requires it.
- Use consistent spacing tokens, a deliberate grid, restrained borders, and small-to-moderate radii. Do not round every element into a pill.
- Avoid gratuitous drop shadows, colored left stripes, excessive borders, and nested card-on-card layouts.
- Use one consistent icon library already installed in the repo if available. Prefer restrained line icons with labels; never use emoji as interface icons. Do not add a dependency just for decoration.
- Every component must have a reason to exist. Prefer real labels, tables, panels, and graph controls over marketing fluff.

## Information architecture and experience

Build the UI around a real investigation workflow. Keep the interface understandable without a long explanation.

### Main workspace
1. **Global shell**
   - Clear ROOTLINE OMNI identity and concise descriptor.
   - Navigation for the actual product sections that exist.
   - A visible environment/data-mode label such as “Synthetic demo data” where applicable.
   - A restrained system/connection state that comes from a real health/API check. Never show “Live” unless it is genuinely live.
   - Responsive layout, keyboard focus states, and accessible navigation.

2. **Incident selection and context**
   - Show real incidents returned by the backend.
   - Display incident title/ID, severity, current status, and timestamp only when the API supplies them.
   - Give the user a clear path from selecting an incident to inspecting its dependency graph.
   - Provide thoughtful empty, loading, error, and retry states.

3. **Dependency graph — primary visual centerpiece**
   - Allocate meaningful screen space to a legible, interactive graph.
   - Use real nodes and edges from the API/backend. Labels must remain readable; avoid excessive decoration and unnecessary animation.
   - Distinguish service types and graph relationships with a restrained, consistent visual encoding and a visible legend.
   - Support fit-to-view, zoom/pan, selection, selected-node details, and sensible graph reset if these capabilities can be implemented with the current stack.
   - Show dependency direction clearly. Keep edge labels available without cluttering every edge.
   - On narrow screens, preserve access to the graph and selected-node details rather than letting the graph overflow offscreen.
   - If graph data fails to load, show a real error state; do not silently substitute a fake graph.

4. **Investigation / evidence panel**
   - Show the selected incident, investigation findings, relevant services/dependencies, and evidence returned by the backend.
   - Separate observed evidence from inferred/heuristic conclusions.
   - Include timestamps/IDs where available.
   - Explain heuristic scores in plain language and do not label them probabilities unless they truly are calibrated probabilities.
   - Avoid generic filler text and fake certainty.

5. **Live Graph Surgery — signature interaction**
   - Make this a first-class workflow, not a tiny secondary button.
   - Clearly distinguish **Baseline** and **Isolated counterfactual** states.
   - Let the user choose a supported dependency edge/action, explain the proposed change before execution, and require an explicit confirmation.
   - Run the operation through the existing backend/API. Do not implement the graph mutation only in the browser.
   - Show operation stages with accessible status text: preparing isolated graph, applying change, rerunning investigation, comparing results, and cleanup/verification as appropriate to the real implementation.
   - Display a concise before/after comparison: affected services/findings, changed paths or reachability, and the exact evidence the backend provides.
   - Make clear this is a counterfactual experiment on an isolated temporary graph, not a production change.
   - Surface failures clearly. Never report success if the request failed or cleanup/invariant verification did not pass.
   - After completion, display the baseline-integrity verification only if the backend actually returns a verified result.
   - Ensure the UI prevents accidental duplicate submissions while a run is in progress.
   - Support a clean return to baseline and a way to inspect the comparison without losing the original context.

6. **Audit/history**
   - If the backend exposes investigation/action history, display it accurately with timestamps and details.
   - If no history endpoint exists, do not fabricate an audit log. Either omit this section or clearly label any client-only session history as local and ephemeral.

### Marketing/landing layer, only if the app already has one or needs a front door
- Lead with a specific product statement about investigating dependency failures and testing counterfactuals against an isolated graph.
- Use a short, factual subheading explaining the workflow.
- The primary CTA must open the actual working investigation experience.
- The first screen should show a real product screenshot or live product surface where feasible, not an abstract gradient orb or stock AI art.
- Do not invent logos, customers, usage metrics, case studies, testimonials, or security certifications.
- Keep marketing copy precise and evidence-led. Do not overstate impact.

## Motion and interaction quality
- Use animation only when it communicates graph selection, state transition, result comparison, or navigation.
- Keep motion brief, subtle, and consistent. Respect `prefers-reduced-motion`.
- Do not use scroll-jacking, cursor trails, sparkle effects, animated arrows, endless floating objects, or entrance animations on every element.
- Use skeleton loaders for real asynchronous loading where useful; avoid fake loading delays.
- Buttons need clear enabled/disabled/loading states and should not appear clickable when they are not.
- Add success/error feedback for meaningful operations without relying on color alone.

## Responsive, accessible, robust
- Test desktop, tablet, and mobile widths.
- Use semantic landmarks, accessible names, visible keyboard focus, logical tab order, and appropriate ARIA only where needed.
- Ensure graph controls can be reached by keyboard and that important graph information is also available in a textual/details view.
- Check text/background contrast; target WCAG AA at minimum. Do not claim AAA without actually testing all relevant elements.
- Forms need labels, useful validation, and understandable error messages.
- Prevent horizontal overflow and clipped buttons, menus, and graph panels.
- Ensure no console errors, broken assets, dead links, or placeholder `href="#"` links.

## Trust, privacy, legal, and scope
- Add actual navigable `/privacy` and `/terms` pages that match the app’s real data handling and project scope. Do not invent legal claims or imply lawyer review.
- If the app uses synthetic demo data only, say that plainly and describe what is and is not collected based on actual code. Do not claim “zero data collection” unless verified.
- Add a concise in-app “Scope & limitations” explanation:
  - demo data is synthetic if that remains true;
  - outputs/scores are heuristic and require human interpretation;
  - counterfactual graph surgery is isolated and must not mutate the baseline;
  - the application does not automatically remediate production systems.
- Footer should include working links to Privacy, Terms, scope/limitations, and the project/repository only if its URL is known and correct.
- No fake compliance badges, fake trust seals, or unverified security promises.

## Engineering requirements
- Reuse the current framework, router, styling system, graph library, and installed dependencies where practical.
- Do not replace the backend with mock JSON or a second competing implementation.
- Keep API URLs configurable for local development and production. Do not hardcode `localhost:8000` in scattered components.
- Use a central API client, typed response models where the project supports TypeScript, and explicit error handling.
- Avoid giant monolithic components. Extract coherent components/hooks, but do not over-engineer.
- Avoid adding heavy dependencies unless they provide essential functionality. Explain any new dependency.
- Keep existing test intent and update tests when UI contracts change.
- Check that frontend and backend agree on request/response schemas.
- Preserve the exact backend semantics for graph copy/isolation, cleanup, and baseline topology invariants.

## Implementation sequence — do not skip steps

### Phase 1: Inspect
- Read the repository and existing docs.
- Identify current design system, app entry points, routes, APIs, and existing test commands.
- Run baseline tests/build where feasible and record current failures separately from new failures.
- Do not edit until the current architecture is understood.

### Phase 2: Design system and shell
- Define color, typography, spacing, radius, border, and focus tokens in the existing styling approach.
- Implement the global shell/navigation, responsive layout, loading/error/empty states, and trust footer.
- Verify visual consistency before moving on.

### Phase 3: Real product workspace
- Connect the incident selector, graph, evidence panel, and node details to actual API responses.
- Make the graph visually excellent and usable, with no fake data fallbacks.
- Ensure the product works when the API is unavailable and clearly explains the issue.

### Phase 4: Live Graph Surgery
- Implement the end-to-end isolated counterfactual flow using existing backend endpoints.
- Show meaningful progress, comparison, errors, cleanup and baseline verification according to actual responses.
- Test the invariant and failure cases; do not weaken tests to make them pass.

### Phase 5: Trust and polish
- Verify `/privacy` and `/terms` as real routes.
- Fix copy, focus, contrast, keyboard operation, responsive behavior, reduced motion, and broken links.
- Remove all placeholder copy, fake metrics, decorative template elements, and unsupported claims.

### Phase 6: Verify and package
Run the project’s actual commands and report the exact results:
- backend tests;
- frontend tests, if present;
- frontend production build;
- backend health check;
- key API checks for incidents, graph data, evidence, and graph surgery;
- `/privacy` and `/terms` route checks;
- manual browser walkthrough of baseline → surgery → comparison → cleanup/invariant verification;
- mobile/responsive and keyboard spot checks;
- submission ZIP integrity and exclusion checks.

Do not claim a test passed unless you ran it and saw the result. Do not hide existing failures. If Docker/FalkorDB is unavailable, state exactly which checks could not be completed.

## Acceptance criteria
The work is complete only when:
- The app looks purpose-designed for graph-native incident investigation, not a generic SaaS template.
- The graph and Live Graph Surgery dominate the product experience in a useful way.
- The data and operations are connected to the actual backend.
- Baseline graph integrity and temporary-graph cleanup remain enforced and are visibly represented only when verified.
- No fabricated metrics, testimonials, production claims, or false “live” indicators remain.
- `/privacy` and `/terms` are real, working routes.
- Loading, empty, error, success, and disabled states are designed.
- The interface is responsive and keyboard-accessible.
- Existing tests and production build pass, or any remaining blocker is reported honestly.
- The submission archive contains the final source and documentation but no secrets or local dependency folders.

## Final response format
After implementation, provide:
1. A short summary of the actual UI changes.
2. The exact files/components changed.
3. The exact commands run and their real results.
4. Any failures, blockers, or unverified behaviors.
5. How to run the app locally.
6. The exact path/name of the updated submission ZIP.
7. A short manual demo checklist.

Start by auditing the current repository, then implement the redesign. Do not stop after writing a plan. Do not ask the user to repeat the requirements above.
