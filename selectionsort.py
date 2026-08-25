import time

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

start = time.perf_counter()

selection_sort(arr)

end = time.perf_counter()

print("\nSorted Array:", arr)
print("Execution Time:", end - start, "seconds")
print("Time Complexity: Best = O(n^2), Average = O(n^2), Worst = O(n^2)")
print("Space Complexity: O(1)")
