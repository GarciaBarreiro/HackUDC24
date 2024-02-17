# SPDX-FileCopyrightText: 2024 Tomás García Barreiro, Ángel Suárez Torres, Muhammad Imran
#
# SPDX-License-Identifier: MIT-0

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    db = get_db()
    error = None

    if not username:
        return jsonify({'error': 'Username is required.'}), 400
    elif not password:
        return jsonify({'error': 'Password is required.'}), 400

    try:
        db.execute(
            "INSERT INTO user (username, password) VALUES (?, ?)",
            (username, generate_password_hash(password)),
        )
        db.commit()
    except db.IntegrityError:
        return jsonify({'error': f"User {username} is already registered."}), 409
    else:
        return jsonify({'message': 'User successfully registered'}), 201


@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    db = get_db()
    error = None
    user = db.execute(
        'SELECT * FROM user WHERE username = ?', (username,)
    ).fetchone()

    if user is None:
        return jsonify({'error': 'Incorrect username.'}), 404
    elif not check_password_hash(user['password'], password):
        return jsonify({'error': 'Incorrect password.'}), 403

    session.clear()
    session['user_id'] = user['id']
    return jsonify({'message': 'Login successful'}), 200


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute('SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

@bp.route('/logut')
def logout():
    session.clear()
    return redirect(url_for('index'))

#For something that requires login 
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return jsonify({'error': 'Authentication required'}), 401
        return view(**kwargs)
    return wrapped_view
