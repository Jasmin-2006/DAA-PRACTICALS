# Practical 8
# Implementation of Graph and Searching using DFS and BFS
#
# Author: Your Name
# Language: Python


from collections import deque


# Graph represented using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


# Depth First Search (DFS)
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs(graph, neighbour, visited)


# Breadth First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)


# Main program
if __name__ == "__main__":

    # Display the graph
    print("Graph:")
    for vertex in graph:
        print(vertex, "->", graph[vertex])

    # DFS traversal
    print("\nDFS Traversal starting from A:")
    dfs(graph, 'A')

    # BFS traversal
    print("\n\nBFS Traversal starting from A:")
    bfs(graph, 'A')

    print()
