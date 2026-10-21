# Floyd–Warshall Algorithm in Python

## Aim
To implement the Floyd–Warshall Algorithm to find the shortest paths between all pairs of vertices in a weighted graph.

## Description
The Floyd–Warshall Algorithm is a dynamic programming algorithm that calculates the shortest distances between every pair of vertices in a graph.

## Algorithm
1. Initialize the distance matrix using the graph's edge weights.
2. Consider each vertex as an intermediate vertex.
3. Update the distance between every pair of vertices if a shorter path is found through the intermediate vertex.
4. Display the final shortest distance matrix.

## Technologies Used
- Python 3

## How to Run
```bash
python floyd_warshall.py
```

## Sample Output
```text
Shortest distance matrix:
0 5 8 9
INF 0 3 4
INF INF 0 1
INF INF INF 0
```

## Time Complexity
O(V³), where V is the number of vertices.

## Space Complexity
O(V²), for the distance matrix.

## Conclusion
The Floyd–Warshall Algorithm successfully finds the shortest distances between all pairs of vertices in a weighted graph. It supports negative edge weights but does not produce valid shortest paths when a negative-weight cycle exists.
