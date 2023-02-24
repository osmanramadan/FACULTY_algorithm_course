from collections import defaultdict
import heapq

def prims(graph, s):
    mst = defaultdict(set)
    visited = set([s])
    edges = [
        (cost, s, w)
        for w, cost in graph[s]
    ]
    heapq.heapify(edges)

    while edges:
        cost, v, w = heapq.heappop(edges)
        if w not in visited and w in graph:
            visited.add(w)
            mst[v].add(w)
            for adj, cost in graph[w]:
                if adj not in visited:
                    heapq.heappush(edges, (cost, w, adj))

    return mst

graph = {
 'A': {('C', 31)},
 'B': {('C', 15)},
 'C': {('G', 77), ('H', 40)},
 'E': {('C', 17), ('I', 3)},
 'G': {('B', 22), ('E', 23)},
 'H': {('G', 66)},
 'I': {('J', 70), ('K', 31)},
}

print(prims(graph, 'A'))