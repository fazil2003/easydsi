from setuptools import setup, find_packages

classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name = 'easydsi',
    version = '1.1.8',
    description = 'The library which helps developers to implement the data structures & algorithms easily without implementing everything.',
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/fazil2003/easydsi',
    author = 'Mohamed Fazil',
    author_email = 'mohamedfazil463@gmail.com',
    license = 'MIT',
    classifiers = classifiers,
    keywords = 'data-structures, algorithms, data, structures, data structures, data structure',
    packages = find_packages(),
    install_requires = ['multipledispatch==0.6.0', 'binarytree==6.5.1']
)
