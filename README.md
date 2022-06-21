# easyDSI 1.1.7

<p align="center">
  <img src="https://aloask.com/assets/images/icon_easydsi.png" style='width: 20%;'/>
</p>
<br /><br />

Python Library makes it easy for users to code and run data structures & algorithms without having to summarize everything.
<br /><br />

## Contains

### Queue
- <b>queue()</b> - Creates an empty queue. <br />
- <b>queue([elements])</b> - Creates an queue with elements. <br />

<br />


## Methods
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
- <b>reverse(inplace=False)</b> - Reverse the queue. <br />
- <b>sort(desc=False, inplace=False)</b> - Sort the queue. <br />

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