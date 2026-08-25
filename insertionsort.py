import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

start = time.perf_counter()

insertion_sort(arr)

end = time.perf_counter()

print("\nSorted Array:", arr)
print("Execution Time:", end - start, "seconds")
print("Time Complexity: Best = O(n), Average = O(n^2), Worst = O(n^2)")
print("Space Complexity: O(1)")
