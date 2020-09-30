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


@bp.route('/', methods=['GET'])
@flask_login.login_required
def index():
    return render_template('admin/page-console.html')


@bp.route('/user', methods=['GET'])
@flask_login.login_required
def user():
    return render_template('admin/page-user.html')


@bp.route('/user/list', methods=['GET'])
@flask_login.login_required
def user_list():
    db = get_db()
    query = db.execute(
        'SELECT id, username, effect FROM user'
    ).fetchall()
    data = []
    for row in query:
        data.append({
            "id": row['id']
            , "username": row['username']
            , "effect": row['effect']
        })
    return {"code": 0, "msg": "", "count": 1, "data": data}


@bp.route('/node', methods=['GET'])
@flask_login.login_required
def node():
    return render_template('admin/page-node.html')


@bp.route('/node/list', methods=['GET'])
@flask_login.login_required
def node_list():
    db = get_db()
    query = db.execute(
        'SELECT id, hostname, username, password, uuid FROM node'
    ).fetchall()
    print(query)
    data = []
    for row in query:
        data.append({
            "id": row['id']
            , "hostname": row['hostname']
            , "username": row['username']
            , "password": row['password']
            , "uuid": row['uuid']
        })
    return {"code": 0, "msg": "", "count": 1, "data": data}
