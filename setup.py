#!/usr/bin/env python

from distutils.core import setup

setup(name='cherwell',
    version='0.3',
    author='Adinan Paiva',
    author_email='paiva.adinan@gmail.com',
    description='A Python3 library abstracting the Cherwell API',
    url='https://github.com/adinanp/cherwell_client',
    packages=['cherwell'],
    install_requires=[
        'requests==2.18.4'
    ],
)
