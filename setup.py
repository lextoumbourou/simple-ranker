#!/usr/bin/env python

from pip.req import parse_requirements
from setuptools import setup

parsed_reqs = parse_requirements('requirements.txt')
reqs = [str(pr.req) for pr in parsed_reqs]

setup(
    name='simple-ranker',
    version='1.0.1',
    author='Lex Toumbourou',
    author_email='lextoumbourou@gmail.com',
    description='An extremely simple, multi-value ranking module for pandas DataFrames',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'Programming Language :: Python',
    ],
    packages=['simple_ranker'],
    package_dir={'simple_ranker': 'simple_ranker'},
    url='https://github.com/lextoumbourou/simple-ranker',
    install_requires=reqs
)
