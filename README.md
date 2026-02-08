# Heap-Sort-Binary-Search
This repository contains a first-principles implementation of two fundamental algorithms in Computer Science: Heap Sort and Binary Search. As a Mathematics and Statistics graduate, I developed these implementations to demonstrate an understanding of memory-efficient data structures and logarithmic complexity.
## Mathematics of Heap Sort
A Binary Heap is a complete binary tree stored within a flat array. I implemented the navigation logic manually using index-based arithmetic:
- Left Child: $2i + 1$
- Right Child: $2i + 2$
- Parent: $(i - 1) // 2$

\
By using a Max-Heap structure, the script ensures that the largest element is always at the root, allowing for an in-place sort with a time complexity of $O(n \log n)$ and space complexity of $O(1)$.
## Search Optimisation
The project includes a Binary Search algorithm. Unlike a linear search ($O(n)$), this implementation utilizes a "divide and conquer" approach to achieve $O(\log n)$ retrieval. This is a critical optimization for handling large-scale datasets typical in quantitative analysis.

## Technical Features
- Encapsulation
- Error Handling
- Randomised Testing
## How To Run
1. Ensure you have Python and Numpy installed 
2. Run the script: `python heap_sort_binary_search.py`
