#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Version    : 0.0.1
@File       : error.py
@CreateTime : 2020/8/29 14:24
@Author     : Ven
@Maintainer : Ven
@Software   : PyCharm
"""
from flask import Flask, render_template


def error_404(code):
    return render_template('error/404.html'), 404


def init_app(app: Flask):
    app.register_error_handler(404, error_404)
