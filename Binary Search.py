n = int(input("Enter number of elements: "))

arr = []
print("Enter sorted array elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter element to search: "))

low = 0
high = n - 1
found = -1

while low <= high:
    mid = (low + high) // 2

    if arr[mid] == key:
        found = mid
        break
    elif key < arr[mid]:
        high = mid - 1
    else:
        low = mid + 1

if found != -1:
    print("Element found at position", found + 1)
else:
    print("Element not found.")

print("\nTime Complexity:")
print("Best Case   : O(1)")
print("Average Case: O(log n)")
print("Worst Case  : O(log n)")

print("\nSpace Complexity:")
print("O(1) (Iterative Binary Search)")
