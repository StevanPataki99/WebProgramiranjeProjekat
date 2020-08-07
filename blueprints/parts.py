import flask
from flask.blueprints import Blueprint

from utils.db import mysql

parts_blueprint = Blueprint("parts_blueprint", __name__)

@parts_blueprint.route("/parts", methods=['GET'])
def get_parts():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM pc_parts")

    parts = cursor.fetchall()
    return flask.jsonify(parts)