# Practical 8 - Implementation of Graph and Searching using DFS and BFS

## Aim

To implement a graph using Python and perform graph traversal using:

1. Depth First Search (DFS)
2. Breadth First Search (BFS)

---

## Objectives

- To understand the concept of graphs.
- To represent a graph using an adjacency list.
- To implement Depth First Search (DFS).
- To implement Breadth First Search (BFS).
- To understand the difference between DFS and BFS.
- To analyze the time and space complexity of graph traversal algorithms.

---

## Introduction

A graph is a non-linear data structure consisting of a collection of vertices (nodes) and edges that connect pairs of vertices.

Graphs are commonly used to represent:

- Computer networks
- Social networks
- Road networks
- Web page connections
- Communication systems
- Dependency relationships

In this practical, the graph is represented using an adjacency list.

Two important graph traversal algorithms are implemented:

### Depth First Search (DFS)

DFS explores a graph by going as deep as possible along one branch before backtracking.

DFS can be implemented using recursion or a stack.

### Breadth First Search (BFS)

BFS explores a graph level by level. It visits all neighbouring vertices before moving to the next level.

BFS generally uses a queue.

---

## Graph Used

The following graph is represented using an adjacency list:

```text
A -> B, C
B -> A, D, E
C -> A, F
D -> B
E -> B, F
F -> C, E
