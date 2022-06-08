from . import db_stuff
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Response
)


from werkzeug.security import check_password_hash, generate_password_hash

import json

bp = Blueprint('auth', __name__, url_prefix='/auth')


def get_user_collection():
    db = db_stuff.get_db()
    return db['users']


def check_if_user_exists(collection, username):
    record = collection.find_one({"username": username})
    if record is None:
        return False
    else:
        return True

"""
@bp.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        json_str = request.get_json()
        json_obj = json.loads(json_str)
"""


@bp.route('/signin', methods=['POST'])
def signin():
    if request.method == 'POST':
        pass

        json_str = request.get_json()
        json_obj = json.loads(json_str)

        username = json_obj['username']
        password = json_obj['password']

        collection = get_user_collection()

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not check_if_user_exists(collection, username):
            error = 'User does not exist!'

        user_entry = collection.find_one({"username": username})
        if check_password_hash(user_entry[password], password):
            error = 'Incorrect password!'

        if error is None:
            session.clear()
            session['user_id'] = user_entry['id']
            return json.dumps([{'success': True}, 200, {'ContentType': 'application/json'}])

        #flash(error)

    return Response(status=403, mimetype='application/json')



