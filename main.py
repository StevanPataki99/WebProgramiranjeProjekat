import flask
import datetime
from flask import Flask

#? Importovanje database fajla
from utils.db import mysql

#? Importovanje flas blueprint fajlova
from blueprints.parts import parts_blueprint
from blueprints.user import user_blueprint
from blueprints.orders import orders_blueprint

app = Flask(__name__, static_url_path="")

#? Povezivanje nad bazom
app.config["MYSQL_DATABASE_USER"] = "root" 
app.config["MYSQL_DATABASE_PASSWORD"] = "rootroot" 
app.config["MYSQL_DATABASE_DB"] = "pcparts_db" 
app.config["SECRET_KEY"] = "secret"

mysql.init_app(app) 

#? Dodavanje blueprintova na flask applikaciju
app.register_blueprint(parts_blueprint, url_prefix="/api")
app.register_blueprint(user_blueprint, url_prefix="/api")
app.register_blueprint(orders_blueprint, url_prefix="/api")

@app.route("/")
@app.route("/index")
def index_page():
    
    return app.send_static_file("index.html")

if __name__ == "__main__":

    app.run("0.0.0.0", 5000, threaded=True)