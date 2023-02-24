# Time-Complexity O(E log V)
from queue import PriorityQueue

def dijkstra(graph, s):
    seen = set()
    cost = {s: 0}
    parent_path = {s: None}
    pq = PriorityQueue()
  
    pq.put((0, s))
    while not pq.empty():
        _, v = pq.get()
        seen.add(v)

        for w, distance in graph[v]:
            if w in seen: continue

            old_cost = cost.get(w, float('inf'))
            new_cost = cost[v] + distance
            
            if new_cost < old_cost:
                pq.put((new_cost, w))
                cost[w] = new_cost
                parent_path[w] = v

    return parent_path

G = {
 'A': {('C', 31)},
 'B': {('C', 15), ('J', 58)},
 'C': {('C', 60), ('G', 77), ('H', 40)},
 'E': {('C', 17), ('E', 55), ('I',  3)},
 'G': {('B', 22), ('E', 23), ('G', 31)},
 'H': {('G', 66)},
 'I': {('J', 70), ('K', 31)},
 'J': {('H',  8), ('K', 28)},
 'K': {('I', 13)}
}

parent_path = dijkstra(G, 'A')
