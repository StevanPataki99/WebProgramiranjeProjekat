import flask
from flask.blueprints import Blueprint
import json

from utils.db import mysql

user_blueprint = Blueprint("user_blueprint", __name__)

@user_blueprint.route("/user", methods=['POST'])
def user_register():
    db = mysql.get_db()
    cursor = db.cursor()

    response = flask.request.json
    print(response)

    temp = None

    # cursor.execute("SELECT * FROM user WHERE user_email=%(email)s", response)
    # temp = cursor.fetchall()
    # if temp != None:
    #     print("NIJE NONE")
    # print("JESTE NONE")

    cursor.execute("INSERT INTO country(country_name) VALUES(%(country)s)", response)
    db.commit() 

    cursor.execute("SELECT country_id FROM country WHERE country_name=%(country)s", response)
    temp = cursor.fetchall()
    response["country"] = temp [0]["country_id"]
    print(response["country"])

    cursor.execute("INSERT INTO city(city_name, country_country_id) VALUES(%(city)s, %(country)s)", response)
    db.commit()

    cursor.execute("SELECT city_id FROM city WHERE city_name=%(city)s", response)
    temp = cursor.fetchall()
    response["city"] = temp [0]["city_id"]
    print(response["city"])

    cursor.execute("INSERT INTO adress(adress_street_name, adress_street_number, city_city_id) VALUES(%(streetName)s, %(streetNumber)s, %(city)s)", response)
    db.commit()

    cursor.execute("SELECT adress_id FROM adress WHERE adress_street_name=%(streetName)s", response)
    temp = cursor.fetchall()
    response["streetName"] = temp [0]["adress_id"]
    print(response["streetName"])

    cursor.execute("INSERT INTO user(user_name, user_email, user_phonenumber, user_password, user_admin, adress_adress_id, adress_city_city_id) VALUES(%(name)s, %(email)s, %(phonenumber)s, %(password)s, 0, %(streetName)s, %(city)s)", response)
    db.commit()

    cursor.execute("SELECT * FROM user WHERE user_name=%(name)s", response)
    temp = cursor.fetchall()
    print(temp)

    return flask.jsonify(flask.request.json), 201

@user_blueprint.route("/userLogIn", methods=['POST'])
def user_log_in():
    db = mysql.get_db()
    cursor = db.cursor()

    print(flask.request.json)
    cursor.execute("SELECT * FROM user WHERE user_email=%(email)s AND user_password=%(password)s", flask.request.json)
    user = cursor.fetchone()
    print(user)

    if user is not None:
        flask.session['user'] = user['user_id']
        return "", 202
    else:
        return "", 404


    db.commit() 

    return flask.jsonify(flask.request.json), 201

@user_blueprint.route("/logout", methods=["GET"])
def logout():
    flask.session.pop("user", None)
    return "", 200

@user_blueprint.route("/currentUser", methods=["GET"])
def current_user():
    return flask.jsonify(flask.session.get("user")), 200

@user_blueprint.route("/user/<int:user_id>", methods=["GET"])
def getUser(user_id):
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM user WHERE user_id=%s",(user_id))
    
    user = cursor.fetchall()

    cursor.execute("SELECT adress_street_name, adress_street_number FROM adress WHERE adress_id=%s",(user[0]['adress_adress_id']))
    user = user + cursor.fetchall()

    cursor.execute("SELECT city_name, country_country_id FROM city WHERE city_id=%s",(user[0]['adress_city_city_id']))
    user = user + cursor.fetchall()

    cursor.execute("SELECT country_name FROM country WHERE country_id=%s",(user[2]['country_country_id']))
    user = user + cursor.fetchall()

    print(user)
    if user is not None:
        return flask.jsonify(user)
    else:
        return "", 404

@user_blueprint.route("/user/<int:user_id>", methods=["PUT"])
def editUser(user_id):
    print("USO USO USO USP")
    db = mysql.get_db()
    cursor = db.cursor()
    data = flask.request.json
    print(data)

    country = {"country_id" : data[2]['country_country_id'], "country_name" : data[3]['country_name']}

    city = {"city_id" : data[0]['adress_city_city_id'], "city_name" : data[2]['city_name']}

    adress = {"adress_id" : data[0]['adress_adress_id'], "adress_street_name" : data[1]['adress_street_name'], "adress_street_number" : data[1]['adress_street_number']}

    user = {"user_id" : data[0]['user_id'], "user_email" : data[0]['user_email'], "user_name" : data[0]['user_name'], "user_password" : data[0]['user_password'], "user_phonenumber" : data[0]['user_phonenumber']}

    cursor.execute("UPDATE country SET country_name=%(country_name)s WHERE country_id=%(country_id)s", country)

    cursor.execute("UPDATE city SET city_name=%(city_name)s WHERE city_id=%(city_id)s", city)

    cursor.execute("UPDATE adress SET adress_street_name=%(adress_street_name)s, adress_street_number=%(adress_street_number)s WHERE adress_id=%(adress_id)s", adress)

    cursor.execute("UPDATE user SET user_name=%(user_name)s, user_email=%(user_email)s, user_password=%(user_password)s, user_phonenumber=%(user_phonenumber)s WHERE user_id=%(user_id)s", user)

    db.commit()

    return "", 200
