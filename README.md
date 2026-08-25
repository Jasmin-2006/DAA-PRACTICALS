# Searching Algorithms in Python

## 📌 Overview

This repository contains Python implementations of two fundamental searching algorithms:

- Linear Search
- Binary Search

Both programs accept user input, search for a specified element, and display the result along with their time and space complexities.

---

## 📂 Files

- `linear_search.py` – Implements Linear Search.
- `binary_search.py` – Implements Binary Search.

---

## 🔍 Linear Search

### Description
Linear Search checks each element of the array one by one until the target element is found or the end of the array is reached.

### Features
- User input
- Works with sorted and unsorted arrays
- Displays search result
- Displays time and space complexity

### Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(1) |
| Average | O(n) |
| Worst | O(n) |

### Space Complexity

**O(1)**

---

## 🔍 Binary Search

### Description
Binary Search repeatedly divides a sorted array into two halves until the required element is found.

> **Note:** Binary Search works only on sorted arrays.

### Features
- User input
- Efficient searching
- Displays search result
- Displays time and space complexity

### Time Complexity

| Case | Complexity |
|------|------------|
| Best | O(1) |
| Average | O(log n) |
| Worst | O(log n) |

### Space Complexity

**O(1)** (Iterative Binary Search)

---

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/your-username/searching-algorithms-python.git
```

Run Linear Search:

```bash
python linear_search.py
```

Run Binary Search:

```bash
python binary_search.py
```

---

## 📚 Concepts Covered

- Searching Algorithms
- Arrays
- User Input
- Linear Search
- Binary Search
- Time Complexity
- Space Complexity

---

## 🎯 Conclusion

Linear Search is simple and suitable for both sorted and unsorted arrays but becomes slower as the dataset grows. Binary Search is significantly faster with a logarithmic time complexity; however, it requires the input array to be sorted. Understanding both algorithms provides a strong foundation for problem-solving and efficient data searching in computer science.
