import docker_database as database
import pandas
import sys


db = database.get_db()
csv_file = sys.argv[1]

csv_contents = pandas.read_csv(csv_file)

#print(csv_contents)

class compliance_run_result(object):
    def __init__(self, rule_id, message, result, provider, region):
        self.message = message
        self.result = result
        self.rule_id = rule_id
        self.provider = provider
        self.region = region
        self.entity = "DUMMY"


def insert_rule_result(db, result):
    sql = "INSERT INTO compliance_run_result (rule_id, result, message, provider, region, entity) values (%s, %s, %s, %s, %s, %s)"
    val = (result.rule_id, result.result, result.message, result.provider, result.region, result.entity)
    print(sql, val)
    db.cursor().execute(sql, val)
    db.commit()



for index, row in csv_contents.iterrows():
    result = compliance_run_result(row["TITLE_ID"], row["NOTES"], row["RESULT"], "AWS", row["REGION"])
    insert_rule_result(db, result)
