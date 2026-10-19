# ROOTLINE OMNI — Research and Event Reference Index

This file separates papers and official technical references from ROOTLINE-specific implementation recommendations. Read the papers and docs themselves before claiming that a feature reproduces a published method.

## Event / Track
- WeMakeDevs × FalkorDB Graph Hacks: https://www.wemakedevs.org/hackathons/falkordb
- Event resources: https://www.wemakedevs.org/hackathons/falkordb/resources
- Organizer article, *How to Build an Agent That Reasons Over a Graph*: https://www.wemakedevs.org/blogs/how-to-build-an-agent-that-reasons-over-a-graph
- Event reference PDF: `Graph_Hacks_Context_for_AI_Agents_WeMakeDevs.pdf` in this folder.

## Research papers

### Think-on-Graph (ToG), ICLR 2024
Jiashuo Sun et al., *Think-on-Graph: Deep and Responsible Reasoning of Large Language Model on Knowledge Graph*.
- Official ICLR page: https://proceedings.iclr.cc/paper_files/paper/2024/hash/10a6bdcabbd5a3d36b760daa295f63c1-Abstract-Conference.html
- Implementation idea: iterative graph exploration / beam search, traceable reasoning paths and evidence-based pruning.
- Boundary: ROOTLINE's deterministic loop is a design adaptation unless the full algorithm and evaluation are reproduced.

### Reasoning on Graphs (RoG), ICLR 2024
Linhao Luo, Yuan-Fang Li, Reza Haffari, Shirui Pan, *Reasoning on Graphs: Faithful and Interpretable Large Language Model Reasoning*.
- Official ICLR page: https://proceedings.iclr.cc/paper_files/paper/2024/hash/3e2aeb66481dd63a32421bf032b70384-Abstract-Conference.html
- Official implementation: https://github.com/RManLuo/reasoning-on-graphs
- Implementation idea: plan/retrieve using valid graph relation paths; ground claims in retrieved facts.
- Boundary: do not claim ROOTLINE is a faithful implementation of the trained RoG pipeline unless it actually is.

### MicroRCA, IEEE/IFIP NOMS 2020
Li Wu, Johan Tordsson, Erik Elmroth, Odej Kao, *MicroRCA: Root Cause Localization of Performance Issues in Microservices*.
- IEEE page: https://ieeexplore.ieee.org/document/9110353/
- DOI: https://doi.org/10.1109/noms47738.2020.9110353
- Reference implementation: https://github.com/elastisys/MicroRCA
- Implementation idea: root-cause localization using attributed graph relationships and anomaly propagation.
- Boundary: a ROOTLINE heuristic on synthetic data is not equivalent to MicroRCA's original method or evaluation.

## Official implementation docs
- FalkorDB Python client: https://github.com/falkordb/falkordb-py
- FalkorDB Python API docs: https://falkordb-py.readthedocs.io/en/stable/falkordb.html
- FalkorDB algorithms docs: https://falkordb.github.io/docs-staging/algorithms/
- FalkorDB shortest path docs: https://falkordb.github.io/docs-staging/algorithms/sppath/
- FalkorDB betweenness docs: https://falkordb.github.io/docs-staging/algorithms/betweenness-centrality/
- MCP tools specification (2025-06-18): https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/docs/specification/2025-06-18/server/tools.mdx
- MCP protocol schema: https://github.com/modelcontextprotocol/modelcontextprotocol/blob/2025-06-18/schema/2025-06-18/schema.ts

## Claims policy
- Record actual FalkorDB Docker image/client versions and test supported algorithm signatures.
- A cloned graph edge removal is a counterfactual topology experiment; it does not by itself prove causality.
- Heuristic scores are not probabilities unless calibrated.
- Benchmark results must be computed from actual outputs; never set a desired percentage.
- A tool registry or a single JSON-RPC route is not automatically a complete MCP server.
