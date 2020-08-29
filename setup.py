#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Version    : 0.0.1
@File       : setup.py
@CreateTime : 2020/8/28 17:44
@Author     : Ven
@Maintainer : Ven
@Software   : PyCharm
"""
from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)