#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Version    : 0.0.1
@File       : admin.py
@CreateTime : 2020/9/11 11:16
@Author     : Ven
@Maintainer : Ven
@Software   : PyCharm
"""
import functools
import flask_login
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db
from flaskr.login import User

bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/')
@flask_login.login_required
def index():
    return render_template('admin/console.html')

