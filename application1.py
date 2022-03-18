import flask
from apis11 import api1

# basic stuff here, just initializing flask app and api
app = flask.Flask(__name__)
api1.init_app(app)

# checkout apis11/__init__.py file for more details


if __name__ == '__main__':
    app.run(debug=True)


