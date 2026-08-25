n = int(input("Enter number of elements: "))

arr = []
print("Enter array elements:")
for i in range(n):
    arr.append(int(input()))

key = int(input("Enter element to search: "))

found = -1

for i in range(n):
    if arr[i] == key:
        found = i
        break

if found != -1:
    print("Element found at position", found + 1)
else:
    print("Element not found.")

print("\nTime Complexity:")
print("Best Case   : O(1)")
print("Average Case: O(n)")
print("Worst Case  : O(n)")

print("\nSpace Complexity:")
print("O(1) (excluding the input array)")
