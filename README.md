Sure Jas 👍 Here is the **complete `README.md` for Practical 6**, matching the format we used for Practical 5, including **Aim, Objective, Theory, Algorithm, Program, Output, Complexity, Result, and Conclusion**.

# Practical 6 – Implementation of Matrix Chain Multiplication Using Dynamic Programming

## Aim

To implement **Matrix Chain Multiplication using Dynamic Programming** and find the minimum number of scalar multiplications required to multiply a chain of matrices.

## Objective

* To understand the Matrix Chain Multiplication problem.
* To implement the problem using Dynamic Programming.
* To find the optimal order of matrix multiplication.
* To reduce the number of scalar multiplications.
* To analyze the time and space complexity of the algorithm.

## Theory

Matrix Chain Multiplication is an optimization problem where a sequence of matrices needs to be multiplied.

The order in which matrices are multiplied affects the total number of scalar multiplications. Although matrix multiplication is associative, different parenthesizations can require different computational costs.

Dynamic Programming is used to find the optimal multiplication order by dividing the problem into smaller subproblems and storing their results.

For matrices with dimensions represented by:

```text id="huw7qz"
[p0, p1, p2, ..., pn]
```

the matrices are:

```text id="y8k2r1"
A1 = p0 × p1
A2 = p1 × p2
...
An = p(n-1) × pn
```

## Problem Statement

Given a chain of matrices, determine the minimum number of scalar multiplications required to multiply all the matrices.

### Given Input

```text id="ml0c6y"
Matrix Dimensions = [10, 20, 30, 40]
```

This represents three matrices:

```text id="1i3qwy"
A1 = 10 × 20
A2 = 20 × 30
A3 = 30 × 40
```

## Algorithm

1. Start with the dimensions of the matrices.
2. Calculate the number of matrices.
3. Create a Dynamic Programming table.
4. Initialize the table with zero.
5. Consider different chain lengths.
6. For every possible matrix chain, try every possible splitting position.
7. Calculate the multiplication cost for each split.
8. Store the minimum cost in the DP table.
9. Continue until the complete matrix chain is processed.
10. Return the minimum multiplication cost.

## Program

```python id="9l2xjs"
# Practical 6
# Implementation of Matrix Chain Multiplication
# Using Dynamic Programming

def matrix_chain_order(dimensions):
    n = len(dimensions) - 1

    # Create DP table
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Chain length
    for length in range(2, n + 1):

        for i in range(n - length + 1):
            j = i + length - 1

            # Set initial value to infinity
            dp[i][j] = float('inf')

            # Try every possible split
            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + dimensions[i] * dimensions[k + 1] * dimensions[j + 1]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[0][n - 1]


# Input
dimensions = [10, 20, 30, 40]

# Calculate minimum multiplication cost
minimum_cost = matrix_chain_order(dimensions)

# Display output
print("Matrix Dimensions:", dimensions)
print("Number of Matrices:", len(dimensions) - 1)
print("Minimum Number of Scalar Multiplications:", minimum_cost)
print("Time Complexity: O(n^3)")
print("Space Complexity: O(n^2)")
```

## Output

```text id="3a0y7s"
Matrix Dimensions: [10, 20, 30, 40]
Number of Matrices: 3
Minimum Number of Scalar Multiplications: 18000
Time Complexity: O(n^3)
Space Complexity: O(n^2)
```

## Explanation of Output

The dimensions are:

```text id="h0a0h6"
[10, 20, 30, 40]
```

Therefore:

```text id="h7p8s1"
A1 = 10 × 20
A2 = 20 × 30
A3 = 30 × 40
```

There are two possible multiplication orders.

### Order 1

```text id="x8ud8h"
(A1 × A2) × A3
```

Cost:

```text id="4ibw4m"
10 × 20 × 30 = 6000
10 × 30 × 40 = 12000

Total = 18000
```

### Order 2

```text id="w5k6os"
A1 × (A2 × A3)
```

Cost:

```text id="h6v4g1"
20 × 30 × 40 = 24000
10 × 20 × 40 = 8000

Total = 32000
```

Therefore, the optimal order is:

```text id="7g5m6n"
(A1 × A2) × A3
```

and the minimum number of scalar multiplications is:

```text id="v0tq8u"
18000
```

## Complexity Analysis

### Time Complexity

**O(n³)**

Three nested loops are used to calculate the minimum multiplication cost for different matrix chains and split positions.

### Space Complexity

**O(n²)**

A two-dimensional Dynamic Programming table is used to store the minimum multiplication costs.

## Advantages

* Finds the optimal multiplication order.
* Reduces unnecessary matrix multiplication operations.
* Uses previously calculated results through Dynamic Programming.
* Useful for optimizing matrix computations.

## Limitations

* The DP table requires additional memory.
* The time complexity increases for a large number of matrices.
* It determines the optimal order but does not actually perform the matrix multiplication.

## Result

The Matrix Chain Multiplication problem was successfully implemented using Dynamic Programming. For the given matrix dimensions `[10, 20, 30, 40]`, the minimum number of scalar multiplications required is **18000**.

## Conclusion

Matrix Chain Multiplication demonstrates the effective use of **Dynamic Programming** for solving optimization problems. Instead of trying every possible multiplication order repeatedly, the algorithm stores the results of smaller subproblems and uses them to determine the optimal solution.

Thus, the **Matrix Chain Multiplication problem was successfully implemented using Dynamic Programming**, achieving a time complexity of **O(n³)** and a space complexity of **O(n²)**.
