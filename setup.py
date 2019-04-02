#!/usr/bin/env python3

#from distutils.core import setup
from setuptools import find_packages, setup
import ovopy

install_requires = [
	'requests',
	#'ujson',
]

packages = ['ovopy']

setup(
	name='ovopy',
	version=ovopy.__version__,
	description='Un-official OVOid Client for Python3',
	author='Anysz',
	url='https://github.com/anysz/ovopy',
	packages=packages,
	license='MIT License',
	install_requires=install_requires,
	classifiers=[
		"Programming Language :: Python",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.0",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities",
        "Topic :: Internet",
	]
)