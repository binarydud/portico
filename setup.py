from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md')) as f:
    long_description = f.read()


setup(
    name="portico",
    version='1.2.0',
    description='decorator library for aws lambda functions',
    long_description=long_description,
    url='https://github.com/binarydud/portico',
    author='Matt George',
    author_email='mgeorge@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=[
        'structlog==16.1.0'
    ],
)
