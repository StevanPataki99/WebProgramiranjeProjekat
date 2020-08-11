import flask
from flask.blueprints import Blueprint
import json

from utils.db import mysql

user_blueprint = Blueprint("user_blueprint", __name__)

@user_blueprint.route("/user", methods=['POST'])
def user_register():
    #TODO doadati da se korisnik uspesno upise u bazu 
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

# @user_blueprint.route("/userCountry", methods=['POST'])
# def user_register():
#     #TODO doadati da se korisnik uspesno upise u bazu 
#     db = mysql.get_db()
#     cursor = db.cursor()

#     print(flask.request.json)
#     #cursor.execute("INSERT INTO predmet(naziv, skracenica) VALUES(%(naziv)s, %(skracenica)s)", flask.request.json)

#     #db.commit() 

#     return flask.jsonify(flask.request.json), 201