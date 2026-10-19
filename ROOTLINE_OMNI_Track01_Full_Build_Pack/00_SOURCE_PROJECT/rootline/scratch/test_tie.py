from backend import graph, investigator as inv
now = 1792000000
graph.run("CREATE (i:Incident {id:'INC-SYNTH-TIE', title:'Synthetic Tie', severity:'SEV1', ts:$ts, pattern:'latency_spike', status:'open', summary:'Tie test', synthetic:true})-[:AFFECTS]->(:Service {id:'checkout-service'})", {"ts": now})
graph.run("CREATE (e1:Evidence {id:'EV-TIE-1', kind:'metric', polarity:'supports', text:'sup1', ts:$ts, synthetic:true}), (e2:Evidence {id:'EV-TIE-2', kind:'metric', polarity:'supports', text:'sup2', ts:$ts, synthetic:true}), (i:Incident {id:'INC-SYNTH-TIE'})-[:HAS_EVIDENCE]->(e1), (e1)-[:ABOUT]->(:Service {id:'payment-service'}), (i)-[:HAS_EVIDENCE]->(e2), (e2)-[:ABOUT]->(:Service {id:'order-service'})", {"ts": now})
try:
    r = inv.investigate("INC-SYNTH-TIE", persist=False)
    print("STATUS:", r["conclusion"]["status"])
    print("TOP_CAND:", r["conclusion"]["top_candidate"])
    print("NOTE:", r["conclusion"]["note"])
    for c in r["candidates"][:4]:
        print("CAND:", c["service_id"], c["score"], c["score_breakdown"])
finally:
    graph.run("MATCH (i:Incident {id:'INC-SYNTH-TIE'}) DETACH DELETE i")
    graph.run("MATCH (e:Evidence) WHERE e.id IN ['EV-TIE-1', 'EV-TIE-2'] DETACH DELETE e")
