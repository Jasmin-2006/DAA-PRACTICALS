# Practical 3: Implementation of Max Heap Sort Algorithm

## Aim

To implement the Max Heap Sort algorithm in Python and sort the given elements in ascending order.

## Algorithm

1. Read the number of elements from the user.
2. Store the elements in an array.
3. Build a Max Heap from the array.
4. Swap the root element with the last element.
5. Reduce the heap size by one.
6. Heapify the root node.
7. Repeat until the array is sorted.
8. Display the sorted array.

## Time Complexity

* **Best Case:** O(n log n)
* **Average Case:** O(n log n)
* **Worst Case:** O(n log n)

## Space Complexity

* **Auxiliary Space:** O(1)
* **Recursive Call Stack:** O(log n)
* **Overall Space:** O(1)

## Sample Input

```
Enter the number of elements: 6
Enter the elements:
12
11
13
5
6
7
```

## Sample Output

```
Sorted Array:
[5, 6, 7, 11, 12, 13]

Time Complexity:
Best Case   : O(n log n)
Average Case: O(n log n)
Worst Case  : O(n log n)

Space Complexity:
Auxiliary Space : O(1)
Recursive Stack : O(log n)
Overall Space   : O(1)
```

## Conclusion

The Max Heap Sort algorithm was successfully implemented in Python. It efficiently sorts the elements using a Max Heap and has a time complexity of **O(n log n)** in all cases while sorting the array in place.
