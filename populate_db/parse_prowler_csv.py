import docker_database as database
import pandas
import sys


db = database.get_db()
csv_file = sys.argv[1]


