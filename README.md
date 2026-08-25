# Practical 4: Factorial Using Iterative and Recursive Methods

## Aim

To implement and analyze the time complexity of a factorial program using iterative and recursive methods in Python.

## Objective

* Implement factorial using an iterative approach.
* Implement factorial using a recursive approach.
* Compare the execution time of both methods.
* Analyze their time and space complexity.

## Description

The factorial of a non-negative integer `n` is the product of all positive integers from `1` to `n`.

**Formula:**

`n! = n × (n-1) × (n-2) × ... × 1`

Also,

`0! = 1`

### 1. Iterative Method

The iterative method uses a loop to calculate the factorial.

**Time Complexity:** O(n)

**Space Complexity:** O(1)

### 2. Recursive Method

The recursive method calculates the factorial by repeatedly calling the same function until the base case is reached.

**Base Case:**

`0! = 1` or `1! = 1`

**Time Complexity:** O(n)

**Space Complexity:** O(n)

## Sample Output

```text
Enter a number: 5

--- Factorial Results ---
Factorial using Iterative Method: 120
Factorial using Recursive Method: 120

--- Execution Time ---
Iterative Execution Time: ... seconds
Recursive Execution Time: ... seconds

--- Complexity Analysis ---
Iterative Time Complexity: O(n)
Iterative Space Complexity: O(1)
Recursive Time Complexity: O(n)
Recursive Space Complexity: O(n)
```

## Comparison

| Method    | Time Complexity | Space Complexity |
| --------- | --------------- | ---------------- |
| Iterative | O(n)            | O(1)             |
| Recursive | O(n)            | O(n)             |

## Conclusion

The factorial program was successfully implemented using both iterative and recursive methods. Both approaches have O(n) time complexity, while the iterative method uses less additional memory than the recursive method.
