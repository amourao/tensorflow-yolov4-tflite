#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tfyolo',
	version='1.0',
	description='tfyolo',
	packages=['tfyolo','tfyolo.core','tfyolo.data'],
	include_package_data=True,
	package_data={
        "tfyolo.data": ["*/*.txt", "*/*.names"],
    },
)
