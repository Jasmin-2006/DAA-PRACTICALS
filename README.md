# Practical 5 – Implementation of a Knapsack Problem Using Dynamic Programming

## Aim

To implement the **0/1 Knapsack Problem using Dynamic Programming** and determine the maximum profit that can be obtained without exceeding the given knapsack capacity.

## Objective

* To understand the concept of the 0/1 Knapsack Problem.
* To implement the Knapsack Problem using Dynamic Programming.
* To construct and use a Dynamic Programming table.
* To analyze the time and space complexity of the algorithm.

## Theory

The **0/1 Knapsack Problem** is an optimization problem in which we are given a set of items. Each item has a specific **weight** and **value**.

A knapsack has a limited carrying capacity. The objective is to select items such that:

* The total weight does not exceed the knapsack capacity.
* The total value of the selected items is maximum.
* Each item can either be selected completely or not selected at all.

Dynamic Programming is used to solve this problem efficiently by breaking it into smaller subproblems and storing their results.

## Problem Statement

Given `n` items with their respective weights and values, and a knapsack with a maximum capacity `W`, find the maximum value that can be obtained by selecting a subset of the items without exceeding the capacity.

### Given Input

* Weights = `[2, 3, 4, 5]`
* Values = `[3, 4, 5, 6]`
* Knapsack Capacity = `5`

## Algorithm

1. Start with the list of item weights and values.
2. Let `n` be the number of items.
3. Create a Dynamic Programming table `dp` of size `(n + 1) × (W + 1)`.
4. Initialize all values of the table to `0`.
5. For each item, consider every possible knapsack capacity.
6. If the weight of the current item is less than or equal to the current capacity:

   * Calculate the value obtained by including the item.
   * Calculate the value obtained by excluding the item.
   * Store the maximum of these two values.
7. If the item's weight is greater than the current capacity, exclude the item.
8. Continue until all items and capacities are processed.
9. The value stored in `dp[n][W]` represents the maximum profit.

## Program

```python
# Practical 5
# Implementation of a Knapsack Problem Using Dynamic Programming

def knapsack(weights, values, capacity):
    n = len(weights)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

# Calculate maximum profit
maximum_profit = knapsack(weights, values, capacity)

# Display output
print("Weights:", weights)
print("Values:", values)
print("Knapsack Capacity:", capacity)
print("Maximum Profit:", maximum_profit)
```

## Output

```text
Weights: [2, 3, 4, 5]
Values: [3, 4, 5, 6]
Knapsack Capacity: 5
Maximum Profit: 7
```

## Explanation of Output

The maximum capacity of the knapsack is `5`.

The optimal selection is:

| Item   | Weight | Value |
| ------ | ------ | ----- |
| Item 1 | 2      | 3     |
| Item 2 | 3      | 4     |

Total weight:

`2 + 3 = 5`

Total value:

`3 + 4 = 7`

Therefore, the maximum profit is **7**.

## Complexity Analysis

Let:

* `n` = number of items
* `W` = knapsack capacity

### Time Complexity

**O(n × W)**

The algorithm fills a table containing `n × W` states.

### Space Complexity

**O(n × W)**

The Dynamic Programming table requires `n × W` memory.

## Advantages

* Provides an optimal solution.
* Avoids solving the same subproblem repeatedly.
* Easy to implement using a Dynamic Programming table.
* More efficient than the basic recursive approach for larger inputs.

## Limitations

* Requires additional memory for the Dynamic Programming table.
* Time and space requirements increase as the number of items and capacity increase.
* The 0/1 Knapsack approach does not allow an item to be divided into fractions.

## Result

The **0/1 Knapsack Problem was successfully implemented using Dynamic Programming**. For the given input, the maximum profit obtained is **7** without exceeding the knapsack capacity of **5**.

## Conclusion

The Knapsack Problem demonstrates how **Dynamic Programming** can be used to solve optimization problems efficiently. By storing the solutions of previously solved subproblems in a table, repeated calculations are avoided. The algorithm considers both possibilities—selecting or not selecting each item—and chooses the option that provides the maximum value.

Thus, the **0/1 Knapsack Problem was successfully implemented using Dynamic Programming**, achieving a time complexity of **O(n × W)** and a space complexity of **O(n × W)**.
