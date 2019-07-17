import docker_database as database
import pandas
import sys


db = database.get_db()
csv_file = sys.argv[1]

csv_contents = pandas.read_csv(csv_file)

print(csv_contents)

