
def kruskal_algorithm(vertices, edges):
    parent = {v: v for v in vertices}
    rank = {v: 0 for v in vertices}

    def find(v):
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]

    def union(u, v):
        root_u = find(u)
        root_v = find(v)

        if root_u == root_v:
            return False

        if rank[root_u] < rank[root_v]:
            parent[root_u] = root_v
        elif rank[root_u] > rank[root_v]:
            parent[root_v] = root_u
        else:
            parent[root_v] = root_u
            rank[root_u] += 1

        return True

    mst = []
    total_weight = 0

    edges.sort(key=lambda edge: edge[2])

    for u, v, weight in edges:
        if union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    if len(mst) != len(vertices) - 1:
        print("Graph is disconnected. MST cannot be formed.")
        return

    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in mst:
        print(f"{u} - {v} : {weight}")

    print("Total weight of MST:", total_weight)


vertices = ['A', 'B', 'C', 'D']
edges = [
    ('A', 'B', 2),
    ('A', 'C', 3),
    ('B', 'C', 1),
    ('B', 'D', 4),
    ('C', 'D', 5)
]

kruskal_algorithm(vertices, edges)
