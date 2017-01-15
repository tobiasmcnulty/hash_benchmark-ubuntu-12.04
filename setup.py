#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# NOTE: To update PyPI, tag the current release:
#
# First increment cache_tools/__init__.py
# Then:
# > git tag x.y.z -m "Version bump for PyPI"
# > git push --tags origin master
# Then:
# > python setup.py sdist upload
#

from setuptools import setup, find_packages
from hash_benchmark import __version__


INSTALL_REQUIRES = [
    'django>=1.6',
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Programming Language :: Python :: 2.7',
]

setup(
    name='hash_benchmark',
    version=__version__,
    description="Simple management commands for benchmarking a Django "
                "project's hash settings",
    author='Martin Koistinen',
    author_email='mkoistinen@gmail.com',
    url='https://github.com/mkoistinen/hash_benchmark',
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False,
)
