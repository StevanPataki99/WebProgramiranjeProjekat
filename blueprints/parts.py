import flask
import os
from werkzeug import secure_filename
from flask.blueprints import Blueprint

from utils.db import mysql

parts_blueprint = Blueprint("parts_blueprint", __name__)

#! Get all Parts and Filters

@parts_blueprint.route("/parts", methods=['GET'])
def get_parts():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM pc_parts")

    parts = cursor.fetchall()
    return flask.jsonify(parts)

@parts_blueprint.route("/partsPriceUp", methods=['GET'])
def get_partsPriceUp():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM pc_parts ORDER BY part_price DESC")

    parts = cursor.fetchall()
    return flask.jsonify(parts)

@parts_blueprint.route("/partsPriceDown", methods=['GET'])
def get_partsPriceDown():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM pc_parts ORDER BY part_price ASC")

    parts = cursor.fetchall()
    return flask.jsonify(parts)

@parts_blueprint.route("/partsPriceAbc", methods=['GET'])
def get_partsPriceAbc():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM pc_parts ORDER BY part_name")

    parts = cursor.fetchall()
    return flask.jsonify(parts)
#! Get one part

@parts_blueprint.route("/part/<int:part_id>", methods=['GET'])
def get_part(part_id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM pc_parts WHERE part_id=%s",(part_id))
    
    part = cursor.fetchall()
    if part is not None:
        return flask.jsonify(part)
    else:
        return "", 404

#! Search Parts

@parts_blueprint.route("/partSearch/<part_search>", methods=['GET'])
def search_part(part_search):
    cursor = mysql.get_db().cursor()

    cursor.execute("SELECT * FROM pc_parts WHERE( part_name LIKE '%" + part_search + "%' OR part_manufacturer LIKE '%" + part_search +"%')")

    parts = cursor.fetchall()
    return flask.jsonify(parts)

#! Delete Part

@parts_blueprint.route("/part/<int:part_id>", methods=['DELETE'])
def delete_part(part_id):

    temp = None
    db = mysql.get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM orders_has_pc_parts WHERE pc_parts_part_id=%s", (part_id))

    temp = cursor.fetchall()

    print("USO USO USO")

    cursor.execute("DELETE FROM pc_parts WHERE part_id=%s", (part_id))

    db.commit()


    return "", 204

#! New Part

@parts_blueprint.route("/part", methods=['POST'])
def new_part():
    db = mysql.get_db()
    cursor = db.cursor()

    print(flask.request.json)

    cursor.execute("INSERT INTO pc_parts(part_name, part_price, part_stock, part_manufacturer, part_warranty, part_info, part_image) VALUES(%(part_name)s, %(part_price)s, %(part_stock)s, %(part_manufacturer)s, %(part_warranty)s, %(part_info)s, %(part_image)s)", flask.request.json)

    db.commit()

    return flask.jsonify(flask.request.json), 201

#! Edit Part

@parts_blueprint.route("/part/<int:part_id>", methods=['PUT'])
def edit_part(part_id):
    db = mysql.get_db()
    cursor = db.cursor()

    print(flask.request.json)

    cursor.execute("UPDATE pc_parts SET part_name=%(part_name)s, part_price=%(part_price)s, part_stock=%(part_stock)s, part_manufacturer=%(part_manufacturer)s, part_warranty=%(part_warranty)s, part_info=%(part_info)s WHERE part_id=%(part_id)s", flask.request.json[0])

    db.commit()

    return flask.jsonify(flask.request.json), 201
