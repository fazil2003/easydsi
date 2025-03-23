# 📌 easydsi 1.2.2

<p align="center">
  <img src="./assets/logo-rounded.png" style='width: 40%'/>
</p>

🚀 **easydsi** is a Python library designed to simplify data structures and algorithms, allowing users to focus on coding without worrying about implementation details.

---

## 📂 Features
- **Heap**
  - `min_heap()`
  - `max_heap()`
- **Queue**
- **Stack**
- **Tree**
  - `binary_tree()`
  - `binary_search_tree()`

---

## 🔢 Heap
### 🛠️ Initialization
- **`heap()`** or **`heap([list])`** - Creates a min heap.
- **`min_heap()`** or **`min_heap([list])`** - Creates a min heap.
- **`max_heap()`** or **`max_heap([list])`** - Creates a max heap.

### ✨ Methods
- `add(element)` - Add an element.
- `remove()` - Remove an element.
- `get_max(n)` - Get `n` maximum elements.
- `get_min(n)` - Get `n` minimum elements.
- `display()` - Display all elements.
- `get_elements()` - Return all elements.

---

## Stack

- `reverse_stack()`  
  Reverses the order of elements in a stack.  

- `sort_stack()`  
  Sorts a stack in ascending order.  

- `duplicate_stack()`  
  Creates a duplicate of a stack without modifying the original.  

- `sum_stack()`  
  Computes the sum of all elements in a stack.  

- `max_in_stack()`  
  Finds the maximum value in a stack.  

- `min_in_stack()`  
  Finds the minimum value in a stack.  

- `merge_stacks()`  
  Merges two stacks into one, maintaining order.  

- `is_balanced()`  
  Checks if a given expression has balanced parentheses.  

- `remove_duplicates()`  
  Removes duplicate elements from a stack while maintaining order.  


## 📦 Queue
### 🛠️ Initialization
- **`queue()`** or **`queue([list])`** - Creates a queue.

This module provides utility functions for performing various operations on a `Queue` object, including retrieving statistics, sorting, reversing, and clearing the queue.

### 📌 Methods and Descriptions

- `get_max(queue, visualize=False)`  
  Returns the maximum numerical value in the queue.  

- `get_min(queue, visualize=False)`  
  Returns the minimum numerical value in the queue.  

- `get_sum(queue, visualize=False)`  
  Computes the sum of all numerical values in the queue.  

- `get_avg(queue, visualize=False)`  
  Computes the average of all numerical elements in the queue.  

- `reverse_queue(queue, inplace=False, visualize=False)`  
  Reverses the order of elements in the queue.  

- `sort_queue(queue, descending=False, inplace=False, visualize=False)`  
  Sorts the queue in ascending order by default. Use `descending=True` for descending order.  

- `clear_queue(queue, visualize=False)`  
  Removes all elements from the queue.  

- `contains(queue, item, visualize=False)`  
  Checks if a specific item exists in the queue.  

---

## 🌳 Tree
### 🛠️ Initialization
- **`tree()`** or **`tree([list])`** - Creates a binary tree.
- **`binary_tree()`** or **`binary_tree([list])`** - Creates a binary tree.
- **`binary_search_tree()`** or **`binary_search_tree([list])`** - Creates a binary search tree.

### ✨ Methods
- `add(element)` - Add an element.
- `remove(value)` - Delete an element with a specific value.
- `get_elements()` - Return all elements.
- `get_nodes()` - Return all nodes.
- `display()` - Display all elements.
- `inorder()` - Get in-order traversal.
- `preorder()` - Get pre-order traversal.
- `postorder()` - Get post-order traversal.
- `levelorder()` - Get level-order traversal.
- `get_size()` - Get total number of elements.
- `get_height()` - Get the tree's height.
- `get_properties()` - Get tree properties.

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
import easydsi as dsi
```

### 🎯 Working with Queue
#### 🔹 Initialize a queue
```python
queue = dsi.queue([1, 2, 3])
queue.display()
```
**Output:**
```
[1, 2, 3]
```

#### 🔹 Add an element
```python
queue.add(4)
queue.display()
```
**Output:**
```
[1, 2, 3, 4]
```

#### 🔹 Remove an element
```python
queue.remove()
queue.display()
```
**Output:**
```
[2, 3, 4]
```

---

## 📊 Statistics
[![PyPI Downloads](https://static.pepy.tech/badge/easydsi)](https://pepy.tech/projects/easydsi)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ffazil2003%2Feasydsi&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
