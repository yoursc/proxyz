#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Version    : 0.0.1
@File       : login.py
@CreateTime : 2020/9/4 16:11
@Author     : Ven
@Maintainer : Ven
@Software   : PyCharm
"""
from flask_login import LoginManager, UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

login_manager = LoginManager()



class User(UserMixin):
    def is_authenticated(self):
        print('user is_authenticated')
        self.authenticated

    def is_active(self):
        print('user is_active')
        return True

    def is_anonymous(self):
        print('user is_anonymous')
        False

    def get_id(self):
        print('user get_id')
        return self.user_id


@login_manager.user_loader
def user_loader(user_id):
    print(f'user_loader:{user_id}')
    db = get_db()
    q = db.execute(
        'SELECT * FROM user WHERE id = ?', (user_id,)
    ).fetchone()
    if q is None:
        return
    print(q['username'])
    user = User()
    user.user_id = user_id
    return user


@login_manager.request_loader
def request_loader(request):
    print('request_loader')
    username = request.form.get('username')
    password = request.form.get('password')
    if username is None or password is None:
        print('empyt u | p')
        return
    db = get_db()
    q = db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()
    if q is None:
        print('user not exist')
        return
    user = User()
    user.username = username
    user.is_authenticated = check_password_hash(q['password'], password)
    return user

@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

def init_app(app):
    login_manager.init_app(app)
