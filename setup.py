#!/usr/bin/env python

from distutils.core import setup

setup(name='cherwell',
    version='0.1',
    author='Adinan Paiva',
    uthor_email='paiva.adinan@gmail.com',
    description='A Python3 library abstracting the Cherwell API',
    url='https://gitlab-devops.totvs.com.br/python/cherwell_client',
    packages=['cherwell'],
    install_requires=[
        'requests==2.18.4'
    ],
)
