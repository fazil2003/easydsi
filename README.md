# easydsi 0.0.1

The library which helps users to implement data structres & algoithms easily without implementing everything briefly.

<br />

## Contains
### 🌟 Array
💫 array(size) - Create an array with size. <br />
💫 array(elements) - Create an array with elements. <br />
<br />

## Methods
💫 add(position, element) - Add the element in the position. <br />
💫 remove(position) - Delete the element from the position. <br />
💫 index(position) - Get the element from the position. <br />
💫 display() - Display all the elements. <br />
💫 getElements() - Get all the elements. <br />
💫 getLength() - Get the length. <br />
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

## 🌟 How to build and upload
```
pip install setuptools twine
python setup.py sdist
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```