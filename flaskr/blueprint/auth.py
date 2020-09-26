#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Version    : 0.0.1
@File       : auth.py
@CreateTime : 2020/8/29 2:38
@Author     : Ven
@Maintainer : Ven
@Software   : PyCharm
"""
import json
import functools
import flask_login
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db
from flaskr.login import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/')
def index():
    return render_template('auth/index.html')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    # GET
    if request.method == 'GET':
        return render_template('auth/register.html')
    # POST
    username = request.form['username']
    password = request.form['password']
    db = get_db()
    error = None
    if not username:
        error = 'Username is required.'
    elif not password:
        error = 'Password is required.'
    elif db.execute('SELECT id FROM user WHERE username = ?', (username,)).fetchall() is not None:
        error = 'User {} is already registered.'.format(username)
    if error is not None:
        db.execute(
            'INSERT INTO user (username, password) VALUES (?, ?)',
            (username, generate_password_hash(password))
        )
        db.commit()
        return redirect(url_for('auth.login'))
    flash(error)


@bp.route('/login', methods=['GET'])
def login():
    return render_template('auth/login.html')


@bp.route('/login', methods=['POST'])
def login_api():
    data = json.loads(str(request.data, 'utf-8'))
    username = data['username']
    password = data['password']
    db = get_db()
    error = None
    q = db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()
    if q is None:
        error = 'Incorrect username.'
    elif not check_password_hash(q['password'], password):
        error = 'Incorrect password.'
    if error is None:
        user = User()
        user.user_id = q['id']
        session['user_id'] = q['id']
        flask_login.login_user(user)
        return {'status': 200, 'message': '登录成功'}
    return {'status': 300, 'message': '登录失败'}


@bp.route('/logout')
@flask_login.login_required
def logout():
    session.clear()
    flask_login.logout_user()
    return redirect(url_for('auth.login'))


@bp.route('/repassword', methods=['GET'])
@flask_login.login_required
def repassword():
    return ""


@bp.route('/repassword', methods=['POST'])
@flask_login.login_required
def repassword_api():
    return ""


@bp.route('/protected')
@flask_login.login_required
def protected():
    return 'haha'


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)

    return wrapped_view
