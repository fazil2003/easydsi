## 📦 Publishing `easydsi` to PyPI

### 🔧 Install Dependencies
Ensure you have the necessary tools installed:
```sh
pip install --upgrade pip setuptools wheel twine build
```

### 🏗️ Build the Package
Run the following command to create the distribution files:
```sh
python -m build
```
This generates a `dist/` folder containing `.tar.gz` and `.whl` files.

### 🧪 Test Installation Locally
Before publishing, test the package by installing it locally:
```sh
pip install ./dist/easydsi-2.0.0-py3-none-any.whl
```

### 🧪 Run the unit tests
```sh
python -m unittest discover tests
```

### ✅ Verify the Installation
Ensure the package is installed correctly:
```python
import easydsi
print(easydsi.__version__)  # Should print '2.0.0'
```

### 🚀 Upload to TestPyPI (For Testing)
Before publishing to PyPI, upload it to [TestPyPI](https://test.pypi.org/) to verify correctness:
```sh
twine upload --repository testpypi dist/*
```

#### 🏗️ Install from TestPyPI
Test the installation from TestPyPI:
```sh
pip install --index-url https://test.pypi.org/simple/ easydsi
```

### 🌍 Publish to PyPI (Official Release)
Once validated, upload the package to PyPI:
```sh
twine upload dist/*
```

### 📥 Install from PyPI
After publishing, users can install it with:
```sh
pip install easydsi
```

### 🔄 Updating the Package
To update the package on PyPI:
1. Increase the version in `setup.py` and `pyproject.toml`
2. Rebuild the package:
   ```sh
   python -m build
   ```
3. Re-upload the new version:
   ```sh
   twine upload dist/*
   ```

### 🛠️ Debugging
Check installed package details:
```sh
pip show easydsi
```

List installed files:
```sh
pip list | grep easydsi
```

Uninstall and reinstall for testing:
```sh
pip uninstall easydsi -y
pip install easydsi
```