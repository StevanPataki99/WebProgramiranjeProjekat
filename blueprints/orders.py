import flask

from flask.blueprints import Blueprint

from utils.db import mysql

orders_blueprint = Blueprint("orders_blueprint", __name__)

@orders_blueprint.route("/order", methods=['POST'])
def create_order():
    db = mysql.get_db()
    cursor = db.cursor()

    response = flask.request.json
    temp = None
    print(response)

    cursor.execute("INSERT INTO country(country_name) VALUES(%(country_name)s)", response)
    db.commit() 

    cursor.execute("SELECT country_id FROM country WHERE country_name=%(country_name)s", response)
    temp = cursor.fetchall()
    response["country_name"] = temp[0]["country_id"]


    cursor.execute("INSERT INTO city(city_name, country_country_id) VALUES(%(city_name)s, %(country_name)s)", response)
    db.commit()

    cursor.execute("SELECT city_id FROM city WHERE city_name=%(city_name)s", response)
    temp = cursor.fetchall()
    response["city_name"] = temp[0]["city_id"]

    cursor.execute("INSERT INTO adress(adress_street_name, adress_street_number, city_city_id) VALUES(%(adress_street)s, %(adress_number)s, %(city_name)s)", response)
    db.commit()

    cursor.execute("SELECT adress_id FROM adress WHERE adress_street_name=%(adress_street)s", response)
    temp = cursor.fetchall()
    response["adress_street"] = temp[0]["adress_id"]

    print(response)
    cursor.execute("INSERT INTO orders (order_price, order_date, order_status, user_user_id, adress_adress_id, adress_city_city_id) VALUES(%(order_price)s, %(order_date)s, %(order_status)s, %(user_id)s, %(adress_street)s, %(city_name)s)", response)
    db.commit()

    cursor.execute("SELECT LAST_INSERT_ID()")
    last_order_id =  cursor.fetchone()
    response["order_status"] = last_order_id['LAST_INSERT_ID()']

    cursor.execute("SELECT part_stock FROM pc_parts WHERE part_id=%(part_id)s ", response)
    temp =  cursor.fetchall()
    temp = temp[0]['part_stock']
    response['pices'] = temp - response['pices']

    cursor.execute("UPDATE pc_parts SET part_stock = %(pices)s WHERE part_id=%(part_id)s;", response)
    db.commit()

    cursor.execute("INSERT INTO orders_has_pc_parts (orders_order_id, orders_user_user_id, orders_adress_adress_id, orders_adress_city_city_id, pc_parts_part_id) VALUES(%(order_status)s, %(user_id)s, %(adress_street)s, %(city_name)s, %(part_id)s)", response)
    db.commit()

    print("IZVRSENO")

    return flask.jsonify(flask.request.json), 201

@orders_blueprint.route("/order", methods=['GET'])
def get_all_valid_order():
    db = mysql.get_db()
    cursor = db.cursor()

    query = {"order_status" : "ORDERD"}

    cursor.execute("SELECT * FROM orders WHERE order_status=%(order_status)s", query)
    orders = cursor.fetchall()

    print(orders)

    

    return flask.jsonify(orders)

@orders_blueprint.route("/order/<int:user_id>", methods=['GET'])
def get_valid_order(user_id):
    db = mysql.get_db()
    cursor = db.cursor()

    query = {"user_id" : user_id, "order_status" : "ORDERD"}

    cursor.execute("SELECT * FROM orders WHERE user_user_id=%(user_id)s AND order_status=%(order_status)s", query)
    orders = cursor.fetchall()

    print(orders)

    

    return flask.jsonify(orders)

@orders_blueprint.route("/orderDone/<int:user_id>", methods=['GET'])
def get_done_order(user_id):
    db = mysql.get_db()
    cursor = db.cursor()

    query = {"user_id" : user_id, "order_status" : "DONE"}

    cursor.execute("SELECT * FROM orders WHERE user_user_id=%(user_id)s AND order_status=%(order_status)s", query)
    orders = cursor.fetchall()

    print(orders)

    

    return flask.jsonify(orders)

@orders_blueprint.route("/order_adress/<int:adress_id>", methods=['GET'])
def get_adress_order(adress_id):
    db = mysql.get_db()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM adress WHERE adress_id=%s", (adress_id))
    adress = cursor.fetchall()
    print(adress)

    cursor.execute("SELECT * FROM city WHERE city_id=%s", (adress[0]["city_city_id"]))
    adress = adress + cursor.fetchall()


    cursor.execute("SELECT * FROM country WHERE country_id=%s", (adress[1]["country_country_id"]))
    adress = adress + cursor.fetchall()

    print(adress)

    return flask.jsonify(adress)

@orders_blueprint.route("/order_parts/<int:order_id>", methods=['GET'])
def get_parts_order(order_id):
    db = mysql.get_db()
    cursor = db.cursor()
    
    cursor.execute("SELECT pc_parts_part_id FROM orders_has_pc_parts WHERE orders_order_id=%s", (order_id))
    part_id = cursor.fetchall()

    cursor.execute("SELECT order_price FROM orders WHERE order_id=%s", (order_id))
    part = cursor.fetchall()

    cursor.execute("SELECT * FROM pc_parts WHERE part_id=%s", (part_id[0]["pc_parts_part_id"]))
    part = part + cursor.fetchall()

    return flask.jsonify(part)

@orders_blueprint.route("/order/<int:order_id>", methods=['DELETE'])
def delete_order(order_id):
    db = mysql.get_db()
    cursor = db.cursor()

    cursor.execute("SELECT order_price FROM orders WHERE order_id=%s", (order_id))

    order_price = cursor.fetchall()

    print(order_price)

    cursor.execute("SELECT pc_parts_part_id FROM orders_has_pc_parts WHERE orders_order_id=%s", (order_id))

    part_id = cursor.fetchall()

    cursor.execute("SELECT part_price FROM pc_parts WHERE part_id=%s", (part_id[0]['pc_parts_part_id']))

    part_price = cursor.fetchall()

    print(part_price)

    order_part_number =int(order_price[0]['order_price'] / part_price[0]['part_price'])

    print(order_part_number)

    cursor.execute("SELECT part_stock FROM pc_parts WHERE part_id=%s", (part_id[0]['pc_parts_part_id']))

    part_stock = cursor.fetchall()

    part_stock = part_stock[0]['part_stock'] + order_part_number

    print(part_stock)
    
    cursor.execute("DELETE FROM orders_has_pc_parts WHERE orders_order_id=%s", (order_id))

    cursor.execute("DELETE FROM orders WHERE order_id=%s", (order_id))

    db.commit()

    update_part = {"part_stock": part_stock, "part_id": part_id[0]['pc_parts_part_id']}

    print(update_part)

    cursor.execute("UPDATE pc_parts SET part_stock=%(part_stock)s WHERE part_id=%(part_id)s", update_part)

    db.commit()

    return "", 204

@orders_blueprint.route("/order_complete/<int:order_id>", methods=['PUT'])
def complete_order(order_id):
    db = mysql.get_db()
    cursor = db.cursor()

    cursor.execute("UPDATE orders SET order_status='DONE' WHERE order_id=%s", (order_id))

    cursor.execute("DELETE FROM orders_has_pc_parts WHERE orders_order_id=%s", (order_id))

    db.commit()

    return "", 204
