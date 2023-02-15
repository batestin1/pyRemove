
<h1 align="center">

<img src="https://img.shields.io/static/v1?label=PYREMOVE%20POR&message=Bates&color=7159c1&style=flat-square&logo=ghost"/>

<h3> <p align="center">PYREMOVE </p> </h3>

<h3> <p align="center"> ================= </p> </h3>

>> <h3> Resume </h3>

<p> The PyRemove library is a tool that makes it possible to remove comments from your Python scripts. With this library, you can choose between two functions: <i>"pyOne(name_file)"</i> to uncomment a single file, or <i> "pyAll(name_dir)" </i> to uncomment all files in the specified directory.

It is important to note that PyRemove works exclusively with Python scripts and does not support other programming languages. If you need to remove comments from files in other languages, you will need to use other language-specific tools. </p>

>> <h3> How install </h3>

```
pip install pyRemove

```

>> <h3> How Works </h3>

```
from pyRemove import pyOne, pyAll

#to uncomment a single file
pyOne("Repositorios/teste/main copy 7.py")

#to uncomment all files in the specified directory.
pyAll("../../teste")

```
    