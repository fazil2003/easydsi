# easydsi 0.0.9

<p align="center">
  <img src="./assets/images/logo.png" style='width: 20%;'/>
</p>
<br /><br />

Python Library makes it easy for users to code and run data structures & algorithms without having to summarize everything.
<br /><br />

## 🌟 Contains
### ✨ Array
💫 array(size) - Creates an array with size. <br />
💫 array(elements) - Creates an array with elements. <br />

### ✨ Linked List
💫 linked_list() - Creates an empty linked list. <br />
💫 linked_list(elements) - Creates an linked list with elements. <br />
<br />


## 🌟 Methods
💫 add(position, element) - Add the element in the position. <br />
💫 remove(position) - Delete the element from the position. <br />
💫 index(position) - Get the element from the position. <br />
💫 display() - Display all the elements. <br />
💫 getElements() - Get all the elements. <br />
💫 getLength() - Get the length. <br />
<br />
(Specially for Linked List) <br />
💫 addAtFirst() - Add the element at the first position. <br />
💫 addAtLast() - Add the element at the last position. <br />
💫 removeAtFirst() - Remove the element from the first position. <br />
💫 removeAtLast() - Remove the element from the last position. <br />
<br />

## 🌟 How to install
💫 Go to your command prompt and type the following command.
```
pip install easydsi
```
<br />

## 🌟 How to use
💫 Import the library in your project
```python
import easydsi
```
<br />

## 🌟 How to build and upload to PyPI
💫 Source Distribution
```
pip install setuptools twine
python setup.py sdist
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```
💫 Wheel File
```
pip install setuptools wheel
python setup.py bdist_wheel
twine upload dist/*
```