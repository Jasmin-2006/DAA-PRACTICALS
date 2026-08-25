# Function to heapify a subtree rooted at index i
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Swap if root is not the largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# Heap Sort Function
def heap_sort(arr):
    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)


# Main Program
n = int(input("Enter the number of elements: "))

arr = []
print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

heap_sort(arr)

print("\nSorted Array:")
print(arr)

print("\nTime Complexity:")
print("Best Case   : O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case  : O(n log n)")

print("\nSpace Complexity:")
print("Auxiliary Space : O(1)")
print("Recursive Stack : O(log n)")
print("Overall Space   : O(1)")
