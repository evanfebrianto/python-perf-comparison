from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("sum_of_squares.pyx"),
)
