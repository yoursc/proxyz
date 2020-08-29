#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Version    : 0.0.1
@File       : __init__.py
@CreateTime : 2020/8/28 17:43
@Author     : Ven
@Maintainer : Ven
@Software   : PyCharm
"""
import os

from flask import Flask, escape, request, redirect, url_for, abort, make_response, render_template
from . import db, auth, blog, error


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='key',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite')
    )

    if test_config is None:
        app.config.from_pyfile(filename='config.py', silent=True)
    else:
        app.config.from_pyfile(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    error.init_app(app)
    app.register_blueprint(auth.bp)
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    @app.route('/user/<username>')
    def profile(username):
        return '{}\'s profile'.format(escape(username))

    return app


if __name__ == '__main__':
    create_app()
