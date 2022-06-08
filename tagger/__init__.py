import os
from . import db_stuff

from flask import Flask, request, send_from_directory


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


    from . import api
    app.register_blueprint(api.bp)
    from . import login
    app.register_blueprint(login.bp)


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app


#os.environ['PYTHONPATH'] = os.getcwd()
app = create_app()
