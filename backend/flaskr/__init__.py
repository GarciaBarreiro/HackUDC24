import os
from flask import Flask, jsonify

def start_app(test_config = None):
    #Create and cofigure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = '1',
        DATABASE = os.path.join(app.instance_path, '../flaskr.sqlite')
    )
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

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return jsonify(message='Hello, World!')

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    #With the Blueprint registered in your app factory, the 
    # /upload route becomes part of your application. You don't 
    # need to manually call the upload_file function; Flask 
    # handles routing and executes the function when the /upload 
    # URL is accessed with a POST request containing a file.
    from . import upload
    app.register_blueprint(upload.bp)

    from .  import analysis
    app.register_blueprint(analysis.bp)

    return app