from flaskext.mysql import MySQL
from flaskext.mysql import pymysql

#? Instanciranje MYsql cursora za radom nad bazom
mysql = MySQL(cursorclass=pymysql.cursors.DictCursor) 