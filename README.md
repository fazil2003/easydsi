# easyDSI 1.2.1

<p align="center">
  <img src="https://aloask.com/assets/images/icon_easydsi.png" style='width: 20%;'/>
</p>
<br /><br />

Python Library makes it easy for users to code and run data structures & algorithms without having to summarize everything.
<br /><br />

## Contains
- heap()
  - min_heap()
  - max_heap()
- queue()
- tree()
  - binary_tree()
  - binary_search_tree()

## Heap
- <b>heap()</b> or <b>heap([list])</b> - Creates a min heap.<br />
- <b>min_heap()</b> or <b>min_heap([list])</b> - Creates a min heap.<br />
- <b>max_heap()</b> or <b>max_heap([list])</b> - Creates a max heap.<br />

### Methods
- <b>add(element)</b> - Add the element at the last position. <br />
- <b>remove()</b> - Delete the element. <br />
- <b>get_max(n)</b> - Get the n maximum elements from the heap. <br />
- <b>get_min(n)</b> - Get the n minimum elements from the heap. <br />
- <b>display()</b> - Display all the elements. <br />
- <b>get_elements()</b> - Return all the elements. <br />
<br />


## Queue
- <b>queue()</b> or <b>queue([list])</b> - Creates a queue. <br />

### Methods
- <b>add(element)</b> - Add the element at the last position. <br />
- <b>add(position, element)</b> - Add the element at the position you give. <br />
- <b>add_first()</b> - Add the element at the first position. <br />
- <b>add_last()</b> - Add the element at the last position. <br />
- <b>remove()</b> - Delete the element from the first position. <br />
- <b>remove(position)</b> - Delete the element from the position. <br />
- <b>remove_first()</b> - Remove the element from the first position. <br />
- <b>remove_last()</b> - Remove the element from the last position. <br />
- <b>index(position)</b> - Get the element from the position. <br />
- <b>find(element)</b> - Get the index of the element.<br />
- <b>display()</b> - Display all the elements. <br />
- <b>get_elements()</b> - Return all the elements. <br />
- <b>get_size()</b> - Get the total number of elements. <br />
- <b>get_max()</b> - Get the maximum element from the queue. <br />
- <b>get_min()</b> - Get the minimum element from the queue. <br />
- <b>get_sum()</b> - Get the sum of the elements from the queue. <br />
- <b>get_avg()</b> - Get the average of the elements from the queue. <br />
- <b>reverse(inplace=False)</b> - Reverse the queue. <br />
- <b>sort(desc=False, inplace=False)</b> - Sort the queue. <br />
- <b>map(function, inplace=False)</b> - Map all the elements to the function. <br />
<br />

## Tree
- <b>tree()</b> or <b>tree([list])</b> - Creates a binary tree.<br />
- <b>binary_tree()</b> or <b>binary_tree([list])</b> - Creates a binary tree.<br />
- <b>binary_search_tree()</b> or <b>binary_search_tree([list])</b> - Creates a binary search tree.<br />

### Methods
- <b>add(element)</b> - Add the element. <br />
- <b>remove(value)</b> - Delete the element with the value. <br />
- <b>get_elements()</b> - Return all the elements. <br />
- <b>get_nodes()</b> - Return all the nodes. <br />
- <b>display()</b> - Display all the elements. <br />
- <b>inorder()</b> - Return the in-order traversal of the tree.<br />
- <b>preorder()</b> - Return the pre-order traversal of the tree.<br />
- <b>postorder()</b> - Return the post-order traversal of the tree.<br />
- <b>levelorder()</b> - Return the level-order traversal of the tree.<br />
- <b>get_size()</b> - Get the total number of elements.<br />
- <b>get_height()</b> - Return the height of the tree.<br />
- <b>get_properties()</b> - Return the properties of the tree.<br />
<br />

## How to install
- Open your command prompt and enter the below command.
```
pip install easydsi
```
<br />

## How to use
- Import the library in your project.
```python
import easydsi as dsi
```

- Initialize the data structure.
```python
queue = dsi.queue([1, 2, 3])
queue.display()
```
> [1, 2, 3]

- Add an element.
```python
queue.add(4)
queue.display()
```

> [1, 2, 3, 4]

- Remove an element.
```python
queue.remove()
queue.display()
```
> [1, 2, 3]

<br />

<!-- ## How to build and upload to PyPI
### Source Distribution
```
pip install setuptools twine
python setup.py sdist
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```
### Wheel File
```
pip install setuptools wheel
python setup.py bdist_wheel
twine upload dist/*
```

<br /> -->

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ffazil2003%2Feasydsi&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)