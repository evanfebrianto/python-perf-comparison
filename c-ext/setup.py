from setuptools import setup, Extension

module = Extension('sumofsquares', sources=['sum_of_squares.c'])

setup(
    name='sumofsquares',
    version='1.0',
    description='Sum of Squares C Extension',
    ext_modules=[module]
)
