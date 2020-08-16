import flask

from flask.blueprints import Blueprint

from utils.db import mysql

orders_blueprint = Blueprint("orders_blueprint", __name__)

@orders_blueprint.route("/order", methods=['POST'])
def create_order():
    # db = mysql.get_db()
    # cursor = db.cursor()

    response = flask.request.json
    print(response)

    return flask.jsonify(flask.request.json), 201