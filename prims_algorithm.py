
import heapq

def prims_algorithm(graph, start):
    visited = set()
    min_heap = [(0, start, None)]
    mst = []
    total_weight = 0

    while min_heap:
        weight, vertex, parent = heapq.heappop(min_heap)

        if vertex in visited:
            continue

        visited.add(vertex)
        total_weight += weight

        if parent is not None:
            mst.append((parent, vertex, weight))

        for neighbor, edge_weight in graph[vertex]:
            if neighbor not in visited:
                heapq.heappush(
                    min_heap, (edge_weight, neighbor, vertex)
                )

    if len(visited) != len(graph):
        print("Graph is disconnected. MST cannot be formed.")
        return

    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} - {v} : {weight}")

    print("Total weight of MST:", total_weight)


graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5)],
    'D': [('B', 4), ('C', 5)]
}

prims_algorithm(graph, 'A')
