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

@parts_blueprint.route("/part/<int:part_id>", methods=['GET'])
def get_part(part_id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM pc_parts WHERE part_id=%s",(part_id))
    
    part = cursor.fetchall()
    if part is not None:
        return flask.jsonify(part)
    else:
        return "", 404