
import mysql.connector

host="172.18.0.2"
user="pankaj"
passwd="pankaj's password"


_db = mysql.connector.connect(host=host, user=user, passwd=passwd)

def get_db():
    return _db

