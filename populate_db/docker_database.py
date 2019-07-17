
import mysql.connector

host="172.18.0.2"
user="pankaj"
passwd="pankaj's password"
database="compliance"

_db = mysql.connector.connect(host=host, user=user, passwd=passwd, database=database)

def get_db():
    return _db

