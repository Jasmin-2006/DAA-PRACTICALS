import time

# Iterative Method
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result


# Recursive Method
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


# Main Program
n = int(input("Enter a number: "))

# Iterative Method Time Analysis
start = time.perf_counter()
iterative_result = factorial_iterative(n)
iterative_time = time.perf_counter() - start

# Recursive Method Time Analysis
start = time.perf_counter()
recursive_result = factorial_recursive(n)
recursive_time = time.perf_counter() - start


# Display Results
print("\n--- Factorial Results ---")
print("Factorial using Iterative Method:", iterative_result)
print("Factorial using Recursive Method:", recursive_result)

print("\n--- Execution Time ---")
print("Iterative Execution Time:", iterative_time, "seconds")
print("Recursive Execution Time:", recursive_time, "seconds")

print("\n--- Complexity Analysis ---")
print("Iterative Time Complexity: O(n)")
print("Iterative Space Complexity: O(1)")
print("Recursive Time Complexity: O(n)")
print("Recursive Space Complexity: O(n)")
