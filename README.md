# 📌 easydsi 2.0.0

<p align="center">
  <img src="./assets/logo-rounded.png" style="width: 40%"/>
</p>

🚀 **easydsi** is a Python library designed to simplify **Data Structures and Algorithms (DSA)**, allowing users to focus on coding without worrying about implementation details.

---

## 📂 Features
- **Heap**
  - `MinHeap()`
  - `MaxHeap()`
- **Queue**
- **Stack**
- **Tree**
  - `BinaryTree()`
  - `BinarySearchTree()`

---

## 📦 Heap
### 🛠️ Initialization
- **`MinHeap()`** or **`MinHeap([list])`** - Creates a MinHeap.
- **`MaxHeap()`** or **`MaxHeap([list])`** - Creates a MaxHeap.
- **`Heap(data=None, max_heap=False)`** - Creates a generic heap that can be a MinHeap or MaxHeap.

This module provides utility functions for performing various operations on a `Heap` object, including retrieving statistics, sorting, merging, and clearing the heap.

### 📌 Methods and Descriptions

- **`heapify_list(data, max_heap=False)`**  
  Converts a list into a **MinHeap** or **MaxHeap**.  

- **`merge_heaps(heap1, heap2, max_heap=False)`**  
  Merges two heaps into a new **MinHeap** or **MaxHeap**.  

- **`is_heap_sorted(heap, max_heap=False)`**  
  Checks if a given heap is sorted.  

- **`get_top_n(heap, n=1)`**  
  Retrieves the top `n` elements from a **MinHeap** or **MaxHeap**.  

- **`heap_sort(data, descending=False)`**  
  Sorts a list using **Heap Sort**.  

- **`contains(heap, element)`**  
  Checks if an element exists in the heap.  

- **`clear_heap(heap)`**  
  Removes all elements from the heap.  

- **`size(heap)`**  
  Returns the number of elements in the heap.  

- **`sum_heap(heap)`**  
  Computes the sum of all elements in the heap.  

- **`max_in_heap(heap)`**  
  Returns the **maximum** element in the heap.  

- **`min_in_heap(heap)`**  
  Returns the **minimum** element in the heap.  

---

## 📦 Stack
### 🛠️ Initialization
- **`Stack()`** - Creates a stack.

### 📌 Methods and Descriptions

- **`reverse_stack()`**  
  Reverses the order of elements in a stack.  

- **`sort_stack()`**  
  Sorts a stack in ascending order.  

- **`duplicate_stack()`**  
  Creates a duplicate of a stack without modifying the original.  

- **`sum_stack()`**  
  Computes the sum of all elements in a stack.  

- **`max_in_stack()`**  
  Finds the maximum value in a stack.  

- **`min_in_stack()`**  
  Finds the minimum value in a stack.  

- **`merge_stacks()`**  
  Merges two stacks into one, maintaining order.  

- **`is_balanced()`**  
  Checks if a given expression has balanced parentheses.  

- **`remove_duplicates()`**  
  Removes duplicate elements from a stack while maintaining order.  

---

## 📦 Queue
### 🛠️ Initialization
- **`Queue()`** or **`Queue([list])`** - Creates a queue.

This module provides utility functions for performing various operations on a `Queue` object, including retrieving statistics, sorting, reversing, and clearing the queue.

### 📌 Methods and Descriptions

- **`get_max(queue, visualize=False)`**  
  Returns the maximum numerical value in the queue.  

- **`get_min(queue, visualize=False)`**  
  Returns the minimum numerical value in the queue.  

- **`get_sum(queue, visualize=False)`**  
  Computes the sum of all numerical values in the queue.  

- **`get_avg(queue, visualize=False)`**  
  Computes the average of all numerical elements in the queue.  

- **`reverse_queue(queue, inplace=False, visualize=False)`**  
  Reverses the order of elements in the queue.  

- **`sort_queue(queue, descending=False, inplace=False, visualize=False)`**  
  Sorts the queue in ascending order by default. Use `descending=True` for descending order.  

- **`clear_queue(queue, visualize=False)`**  
  Removes all elements from the queue.  

- **`contains(queue, item, visualize=False)`**  
  Checks if a specific item exists in the queue.  

---

# 🌳 Tree  
## 🛠️ Initialization  
- **`BinaryTree()`** or **`BinaryTree(root_value)`** - Creates a Binary Tree with an optional root value.  
- **`BinarySearchTree()`** or **`BinarySearchTree(root_value)`** - Creates a Binary Search Tree with an optional root value.  

This module provides utility functions for performing various operations on a `Tree` object, including retrieving statistics, searching, traversing, and modifying the tree.

## 📌 Methods and Descriptions  

- **`contains(tree, value)`**  
  Checks if a tree contains a specific value.  

- **`sum_tree(tree)`**  
  Returns the sum of all elements in the tree.  

- **`max_in_tree(tree)`**  
  Returns the **maximum** value in the tree.  

- **`min_in_tree(tree)`**  
  Returns the **minimum** value in the tree.  

- **`count_nodes(tree)`**  
  Returns the total number of nodes in the tree.  

- **`count_leaves(tree)`**  
  Returns the number of leaf nodes in the tree.  

- **`get_height(tree)`**  
  Returns the height of the tree.  

- **`inorder(tree)`**  
  Returns the **in-order traversal** of the tree (**Left, Root, Right**).  

- **`preorder(tree)`**  
  Returns the **pre-order traversal** of the tree (**Root, Left, Right**).  

- **`postorder(tree)`**  
  Returns the **post-order traversal** of the tree (**Left, Right, Root**).  

- **`levelorder(tree)`**  
  Returns the **level-order traversal** of the tree (**Breadth-First Traversal**).  

---

## 📥 Installation
Run the following command to install:
```sh
pip install easydsi
```

---

## 🚀 Quick Start
Import the library into your project:
```python
from easydsi.tree.binary_tree import BinaryTree, BinarySearchTree
from easydsi.tree.tree_utils import max_in_tree, sum_tree
```

### 🎯 Working with Tree
#### 🔹 Initialize a tree
```python
bt = BinaryTree([3, 5, 1, 7, 2])
print(bt)
```
**Output:**
```sh
    __3
   /   \
  5     1
 / \
7   2
```

#### 🔹 Get maximum value in Binary Search Tree
```python
bst = BinarySearchTree([10, 5, 15, 2, 7])
print(max_in_tree(bst))
```
**Output:**
```sh
15
```

#### 🔹 Get all elements after adding 6
```python
bt.add(6)
print(bt.get_elements())
```
**Output:**
```sh
[3, 5, 1, 7, 2, 6]
```

---

## 📊 Statistics
[![PyPI Downloads](https://static.pepy.tech/badge/easydsi)](https://pepy.tech/projects/easydsi)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ffazil2003%2Feasydsi&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
