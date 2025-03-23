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