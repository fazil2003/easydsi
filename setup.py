from setuptools import setup, find_packages
import os

# Read files safely
def read_file(filename):
    try:
        with open(filename, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""

# Package metadata
PACKAGE_NAME = "easydsi"
VERSION = "1.2.2"  # Consider keeping versioning in a single source (e.g., __version__.py)
DESCRIPTION = (
    "A Python library that helps developers implement data structures & algorithms easily "
    "without having to build everything from scratch."
)
LONG_DESCRIPTION = read_file("README.md") + "\n\n" + read_file("CHANGELOG.txt")
AUTHOR = "Mohamed Fazil"
AUTHOR_EMAIL = "mohamedfazil463@gmail.com"
URL = "https://github.com/fazil2003/easydsi"
LICENSE = "MIT"

# Dependencies
INSTALL_REQUIRES = [
    "multipledispatch==0.6.0",
    "binarytree==6.5.1"
]

# Classifiers for PyPI
CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Education",
    "Topic :: Software Development :: Libraries",
    "Topic :: Software Development :: Data Structures",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "License :: OSI Approved :: MIT License"
]

# Extra links for PyPI
PROJECT_URLS = {
    "Documentation": "https://github.com/fazil2003/easydsi/wiki",
    "Source Code": URL,
    "Issue Tracker": f"{URL}/issues"
}

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license=LICENSE,
    classifiers=CLASSIFIERS,
    keywords=[
        "data-structures", "algorithms", "data", "structures", "stack", "queue",
        "linked-list", "tree", "graph", "searching", "sorting"
    ],
    packages=find_packages(include=["easydsi", "easydsi.*"]),
    install_requires=INSTALL_REQUIRES,
    python_requires=">=3.6",
    project_urls=PROJECT_URLS,
)
