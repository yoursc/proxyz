#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@Version    : 0.0.1
@File       : db.py
@CreateTime : 2020/8/29 2:11
@Author     : Ven
@Maintainer : Ven
@Software   : PyCharm
"""
import sqlite3

import click
import uuid
from flask import Flask, current_app, g
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()


@click.command('init')
@with_appcontext
def init_db_command():
    db = get_db()
    click.echo('Init database')
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    click.echo('Init root user')
    db.execute(
        'INSERT INTO user (id, username, password) VALUES (?, ?, ?)',
        (0, 'root', generate_password_hash('root'))
    )

    my_uuid = str(uuid.uuid4())
    click.echo(f'Init my-uuid: {my_uuid}')
    db.execute(
        'INSERT INTO config (k, v) VALUES (?, ?)',
        ('my-uuid', my_uuid)
    )
    db.commit()
    click.echo('Initialized success.')


def init_app(app: Flask):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
