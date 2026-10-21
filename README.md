# Prim's Algorithm in Python

## Aim
To implement Prim's Algorithm to find the Minimum Spanning Tree (MST) of a weighted, undirected graph.

## Description
Prim's Algorithm is a greedy algorithm that constructs a Minimum Spanning Tree by repeatedly selecting the minimum-weight edge that connects a visited vertex to an unvisited vertex.

## Algorithm
1. Start from a selected vertex.
2. Add the vertex to the visited set.
3. Select the minimum-weight edge connecting a visited vertex to an unvisited vertex.
4. Repeat until all vertices are visited.
5. Display the MST edges and their total weight.

## Technologies Used
- Python 3
- `heapq` module

## How to Run
```bash
python prims_algorithm.py
```

## Sample Output
```text
Edges in the Minimum Spanning Tree:
A - B : 2
B - C : 1
B - D : 4
Total weight of MST: 7
```

## Time Complexity
O(E log E), where E is the number of edges.

## Space Complexity
O(V + E), where V is the number of vertices and E is the number of edges.

## Conclusion
Prim's Algorithm successfully finds the Minimum Spanning Tree of a connected, weighted, undirected graph with minimum total edge weight.
