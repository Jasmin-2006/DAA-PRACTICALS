# Travelling Salesman Problem in Python

## Aim
To find the minimum-cost tour that visits every city exactly once and returns to the starting city.

## Description
The Travelling Salesman Problem (TSP) is a combinatorial optimization problem. This program uses the brute-force method to examine all possible city orders and select the tour with the minimum total travel cost.

## Algorithm
1. Select a starting city.
2. Generate all permutations of the remaining cities.
3. Calculate the cost of each tour.
4. Select the tour with the minimum cost.
5. Display the optimal tour and its total cost.

## Technologies Used
- Python 3
- itertools module

## How to Run
```bash
python travelling_salesman.py
```

## Sample Output
```text
Optimal Tour: 0 -> 1 -> 3 -> 2 -> 0
Minimum Travel Cost: 80
```

## Time Complexity
O(n!), where n is the number of cities.

## Space Complexity
O(n), excluding permutation-generation overhead.

## Conclusion
The program finds the minimum-cost tour by checking all possible routes. The brute-force approach is suitable for small numbers of cities but becomes expensive for larger problems.
