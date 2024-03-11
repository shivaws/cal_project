from setuptools import setup, find_packages, Extension

# Extension for the C++ library
calculator_extension = Extension(
    'calculator',
    sources=['calculator.cpp'],
)

setup(
    name='calculator',
    version='1.0',
    packages=find_packages(),
    ext_modules=[calculator_extension],
)
