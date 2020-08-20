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