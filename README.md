# easydsi 1.0.5

<p align="center">
  <img src="https://aloask.com/assets/images/icon_easydsi.png" style='width: 20%;'/>
</p>
<br /><br />

Python Library makes it easy for users to code and run data structures & algorithms without having to summarize everything.
<br /><br />

## Contains
### Array
- array(size) - Creates an array with size. <br />
- array(elements) - Creates an array with elements. <br />

### Linked List
- linked_list() - Creates an empty linked list. <br />
- linked_list(elements) - Creates an linked list with elements. <br />

### Stack
- stack(size) - Creates an stack with size. <br />
- stack(elements) - Creates an stack with elements. <br />

### Queue
- queue(size) - Creates an queue with size. <br />
- queue(elements) - Creates an queue with elements. <br />

### Double Ended Queue
- double_ended_queue(size) - Creates an queue with size. <br />
- double_ended_queue(elements) - Creates an queue with elements. <br />
<br />


## Methods
- add(position, element) - Add the element in the position. <br />
- remove(position) - Delete the element from the position. <br />
- index(position) - Get the element from the position. <br />
- display() - Display all the elements. <br />
- getElements() - Get all the elements. <br />
- getLength() - Get the length. <br />
<br />

## Methods - Specially for Linked List, Double Ended Queue
- addAtFirst() - Add the element at the first position. <br />
- addAtLast() - Add the element at the last position. <br />
- removeAtFirst() - Remove the element from the first position. <br />
- removeAtLast() - Remove the element from the last position. <br />
<br />

## How to install
- Go to your command prompt and type the following command.
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