# Kruskal's Algorithm in Python

## Aim
To implement Kruskal's Algorithm to find the Minimum Spanning Tree (MST) of a weighted, undirected graph.

## Description
Kruskal's Algorithm is a greedy algorithm that selects edges in increasing order of weight, avoiding cycles, until the Minimum Spanning Tree is formed.

## Algorithm
1. Sort all edges in ascending order of weight.
2. Initialize each vertex as a separate set.
3. Select the smallest-weight edge.
4. Add the edge if it does not form a cycle.
5. Repeat until the MST contains V - 1 edges.

## Technologies Used
- Python 3

## How to Run
```bash
python kruskal_algorithm.py
```

## Sample Output
```text
Edges in the Minimum Spanning Tree:
B - C : 1
A - B : 2
B - D : 4
Total weight of MST: 7
```

## Time Complexity
O(E log E), where E is the number of edges.

## Space Complexity
O(V), where V is the number of vertices, excluding the input edge list.

## Conclusion
Kruskal's Algorithm successfully finds the Minimum Spanning Tree by selecting minimum-weight edges without forming cycles.
