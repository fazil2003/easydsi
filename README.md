# 📌 easyDSI 1.2.1

<p align="center">
  <img src="./assets/logo.png" style='width: 20%; background: white; border-radius: 200px; padding: 10px 20px 10px 20px;'/>
</p>

🚀 **easyDSI** is a Python library designed to simplify data structures and algorithms, allowing users to focus on coding without worrying about implementation details.

---

## 📂 Features
- **Heap**
  - `min_heap()`
  - `max_heap()`
- **Queue**
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

## 📦 Queue
### 🛠️ Initialization
- **`queue()`** or **`queue([list])`** - Creates a queue.

### ✨ Methods
- `add(element)` - Add an element at the last position.
- `add(position, element)` - Insert an element at a given position.
- `add_first()` - Add an element at the first position.
- `add_last()` - Add an element at the last position.
- `remove()` - Remove the first element.
- `remove(position)` - Remove an element at a given position.
- `remove_first()` - Remove the first element.
- `remove_last()` - Remove the last element.
- `index(position)` - Get the element at a position.
- `find(element)` - Find the index of an element.
- `display()` - Display all elements.
- `get_elements()` - Return all elements.
- `get_size()` - Get the total number of elements.
- `get_max()` - Get the maximum element.
- `get_min()` - Get the minimum element.
- `get_sum()` - Get the sum of all elements.
- `get_avg()` - Get the average of elements.
- `reverse(inplace=False)` - Reverse the queue.
- `sort(desc=False, inplace=False)` - Sort the queue.
- `map(function, inplace=False)` - Apply a function to all elements.

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
