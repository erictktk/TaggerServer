from . import db_stuff
from . import libs_dict
import flask
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, Response
)

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/request', methods=['POST'])
def update():
    if request.method == 'POST':

        lib = request.args.get('lib', type=str)
        print(lib)
        doc = request.files['doc']

        if lib in libs_dict.libs:
            db_stuff.save_to_collection(doc)
            return Response(status=200, mimetype='application/json')
        else:
            return Response(status=401, mimetype='application/json')


@bp.route('/loadnew', methods=['GET', 'POST'])
def loadnew():
    if request.method == 'POST' or request.method == 'GET':

        lib = request.args.get('lib', type=str)
        print(lib)

        if lib in libs_dict.libs:
            doc = db_stuff.get_latest_from_collection(lib)
            if doc is None:
                return Response(status=404, mimetype='application/json')
            else:
                return flask.jsonify(doc)
        else:
            return Response(status=401, mimetype='application/json')