#!/usr/bin/env python

from setuptools import setup, find_packages

with open('README.rst') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

version = '0.2.1'

setup(
    name='prawoauth2',
    version=version,
    install_requires=requirements,
    author='Avinash Sajjanshetty',
    author_email='hi@avi.im',
    packages=find_packages(),
    include_package_data=True,
    test_suite='tests',
    url='https://github.com/avinassh/prawoauth2/',
    license='MIT',
    description='Library to make your life easier using OAuth2 for PRAW',
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ],
)
