import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

start = time.perf_counter()

bubble_sort(arr)

end = time.perf_counter()

print("\nSorted Array:", arr)
print("Execution Time:", end - start, "seconds")
print("Time Complexity: Best = O(n), Average = O(n^2), Worst = O(n^2)")
print("Space Complexity: O(1)")
