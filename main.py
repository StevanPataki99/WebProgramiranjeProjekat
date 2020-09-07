import flask
import datetime
import os
from flask import Flask
from werkzeug import secure_filename

#? Importovanje database fajla
from utils.db import mysql

#? Importovanje flas blueprint fajlova
from blueprints.parts import parts_blueprint
from blueprints.user import user_blueprint
from blueprints.orders import orders_blueprint

ALLOWED_EXTENSIONS = {'png'}

app = Flask(__name__, static_url_path="")

#? Povezivanje nad bazom
app.config["MYSQL_DATABASE_USER"] = "root" 
app.config["MYSQL_DATABASE_PASSWORD"] = "rootroot" 
app.config["MYSQL_DATABASE_DB"] = "pcparts_db" 
app.config["SECRET_KEY"] = "secret"

#? Podesavanje file upload
app.config['UPLOAD_EXTENSIONS'] = ['.png']
app.config['UPLOAD_PATH'] = '/Users/stevanpataki/Desktop/WebProgProjekat/static/img'

mysql.init_app(app) 

#? Dodavanje blueprintova na flask applikaciju
app.register_blueprint(parts_blueprint, url_prefix="/api")
app.register_blueprint(user_blueprint, url_prefix="/api")
app.register_blueprint(orders_blueprint, url_prefix="/api")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/imageupload", methods=['POST', 'GET'])
def image_upload():

    if flask.request.method == 'POST':
        if 'file' not in flask.request.files:
            print('No file part')
            return 'NO FILE', 500
        file = flask.request.files['file']

        if file.filename == '':
            print('No selected file')
            return 'No selected file', 500
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
            print("FILE UPLOADED")
            return "FILE UPLOADED" , 201
        else:
            print("FILE NOT UPLOADED SOMETHING WRONG")
            return "FILE NOT UPLOADED", 201


@app.route("/")
@app.route("/index")
def index_page():
    
    return app.send_static_file("index.html")

if __name__ == "__main__":

    app.run("0.0.0.0", 5000, threaded=True)