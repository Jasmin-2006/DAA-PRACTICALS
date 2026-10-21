
from itertools import permutations

def travelling_salesman(graph, start):
    vertices = list(range(len(graph)))
    others = [v for v in vertices if v != start]

    min_cost = float('inf')
    best_path = []

    for route in permutations(others):
        path = [start] + list(route) + [start]
        cost = 0

        for i in range(len(path) - 1):
            cost += graph[path[i]][path[i + 1]]

        if cost < min_cost:
            min_cost = cost
            best_path = path

    print("Optimal Tour:", " -> ".join(map(str, best_path)))
    print("Minimum Travel Cost:", min_cost)


graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

travelling_salesman(graph, 0)
