# easydsi 1.0.6

<p align="center">
  <img src="https://aloask.com/assets/images/icon_easydsi.png" style='width: 20%;'/>
</p>
<br /><br />

Python Library makes it easy for users to code and run data structures & algorithms without having to summarize everything.
<br /><br />

## Contains
### Array
- <b>array(size)</b> - Creates an array with size. <br />
- <b>array(elements)</b> - Creates an array with elements. <br />

### Linked List
- <b>linked_list()</b> - Creates an empty linked list. <br />
- <b>linked_list(elements)</b> - Creates an linked list with elements. <br />

### Stack
- <b>stack(size)</b> - Creates an stack with size. <br />
- <b>stack(elements)</b> - Creates an stack with elements. <br />

### Queue
- <b>queue(size)</b> - Creates an queue with size. <br />
- <b>queue(elements)</b> - Creates an queue with elements. <br />

### Double Ended Queue
- <b>double_ended_queue(size)</b> - Creates an queue with size. <br />
- <b>double_ended_queue(elements)</b> - Creates an queue with elements. <br />
<br />


## Methods
- <b>add(position, element)</b> - Add the element in the position. <br />
- <b>remove(position)</b> - Delete the element from the position. <br />
- <b>index(position)</b> - Get the element from the position. <br />
- <b>display()</b> - Display all the elements. <br />
- <b>elements()</b> - Get all the elements. <br />
- <b>length()</b> - Get the length. <br />
<br />

## Methods - Specially for Linked List, Double Ended Queue
- <b>add_first()</b> - Add the element at the first position. <br />
- <b>add_last()</b> - Add the element at the last position. <br />
- <b>remove_first()</b> - Remove the element from the first position. <br />
- <b>remove_last()</b> - Remove the element from the last position. <br />
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
import easydsi as ds
```

- Initialize the data structure.
```python
stack = ds.stack([1, 2, 3])
```

- Use the data structure.
```python
stack.display()
```
<br />

## How to build and upload to PyPI
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

<br />

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ffazil2003%2Feasydsi&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)