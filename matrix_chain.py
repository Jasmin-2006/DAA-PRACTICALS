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
