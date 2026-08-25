# Practical 7 - Making Change Problem using Dynamic Programming

## Aim

To implement the Making Change Problem using Dynamic Programming in Python and find the minimum number of coins required to make a given target amount.

## Problem Statement

Given a set of coin denominations and a target amount, find the minimum number of coins required to make the target amount.

For example, if the available coins are:

```text
1 2 5 10
```

and the target amount is:

```text
18
```

The minimum number of coins required is:

```text
10 + 5 + 2 + 1 = 18
```

Therefore, the answer is **4 coins**.

## Algorithm

1. Read the coin denominations.
2. Read the target amount.
3. Create a DP array of size `amount + 1`.
4. Initialize all values of the DP array to infinity.
5. Set `dp[0] = 0` because zero coins are required to make amount 0.
6. For every amount from `1` to the target amount:

   * Check every available coin.
   * If the coin is less than or equal to the current amount, calculate the required number of coins.
   * Store the minimum number of coins in the DP array.
7. Return `dp[amount]`.
8. If the value remains infinity, the target amount cannot be formed using the given coins.

## Python Implementation

```python
def making_change(coins, amount):
    # dp[i] stores the minimum number of coins
    # required to make amount i
    dp = [float('inf')] * (amount + 1)

    # Base case
    dp[0] = 0

    # Calculate minimum coins for every amount
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If amount cannot be formed
    if dp[amount] == float('inf'):
        return -1

    return dp[amount]


if __name__ == "__main__":
    coins = list(map(int, input("Enter coin denominations: ").split()))
    amount = int(input("Enter amount: "))

    result = making_change(coins, amount)

    if result == -1:
        print("Change cannot be made with the given coins.")
    else:
        print("Minimum number of coins required:", result)
```

## Example Input

```text
Enter coin denominations: 1 2 5 10
Enter amount: 18
```

## Example Output

```text
Minimum number of coins required: 4
```

## Explanation

For the input:

```text
Coins = [1, 2, 5, 10]
Amount = 18
```

The Dynamic Programming algorithm calculates the minimum number of coins needed for every amount from `0` to `18`.

One optimal combination is:

```text
10 + 5 + 2 + 1 = 18
```

Therefore:

```text
Minimum number of coins = 4
```

## Dynamic Programming Approach

Dynamic Programming solves the problem by breaking it into smaller subproblems.

The value:

```text
dp[i]
```

represents the minimum number of coins required to make the amount `i`.

The recurrence relation is:

```text
dp[i] = min(dp[i], dp[i - coin] + 1)
```

The initial condition is:

```text
dp[0] = 0
```

This approach avoids calculating the same subproblems repeatedly.

## Complexity Analysis

Let:

* `n` = target amount
* `m` = number of coin denominations

### Time Complexity

For every amount from `1` to `n`, the algorithm checks all `m` coins.

Therefore:

```text
Time Complexity = O(n × m)
```

### Space Complexity

The algorithm uses a DP array of size `n + 1`.

Therefore:

```text
Space Complexity = O(n)
```

## Advantages of Dynamic Programming

* Avoids repeated calculations.
* Efficiently solves the Making Change Problem.
* Stores previously calculated results.
* Reduces the time required compared with a naive recursive approach.
* Can handle larger target amounts efficiently.

## Limitations

* Requires additional memory for the DP array.
* The time required increases when the target amount or number of coin denominations becomes large.
* The algorithm finds the minimum number of coins, not necessarily the number of different ways to make the amount.

## Applications

The Making Change Problem has applications in:

* Coin change systems.
* Vending machines.
* Cash dispensing systems.
* Payment processing.
* Optimization problems.
* Resource allocation problems.

## Conclusion

The Making Change Problem was successfully implemented using Dynamic Programming in Python. The algorithm finds the minimum number of coins required to make a given target amount by storing and reusing previously calculated results.

Dynamic Programming reduces repeated calculations and provides an efficient solution to the problem. The time complexity of the algorithm is `O(n × m)`, where `n` is the target amount and `m` is the number of coin denominations. The space complexity is `O(n)` because a DP array is used to store the results.

Thus, Dynamic Programming is an effective approach for solving the Making Change Problem efficiently.
