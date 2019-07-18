import docker_database as database
import pandas
import sys
import numpy
import subprocess
import os

db = database.get_db()
csv_file = sys.argv[1]
group_dir = sys.argv[2]

csv_contents = pandas.read_csv(csv_file)


class group(object):
    def __init__(self, id, title, checks):
        self.id = id
        self.title = title.split("-")[0].strip()
        self.checks = set(checks.split(","))
    def __str__(self):
        return "{id:'%s', title:'%s'}" % (self.id, self.title)


class compliance_run_result(object):
    
    def __init__(self, rule_id, message, result, provider, region):
        self.message = message
        self.result = result
        self.rule_id = rule.get_id(rule_id)
        self.provider = provider
        self.region = region
        self.entity = "DUMMY"


class rule(object):
    
    map_to_id = {}
    
    def get_id(tid):
        x = rule.map_to_id.get(tid, len(rule.map_to_id))
        rule.map_to_id[tid] = x
        return x
        
    def __init__(self, id, title, level, groups):
        self.severity = level
        
        index = title.find("[")
        if index == -1:
            name = "----"
            description = title
        else:
            index2 = title.find("]")
            name = title[index+1:index2]
            description = title[index2+1:]
        self.name = name
        self.provider = "AWS"
        self.entity_type = "DUMMY_TYPE"
        self.group = ",".join(filter_group_ids(groups, self.name))
        self.descritpion = description
        if level == "Support":
            return
        self.id = rule.get_id(id)
    
    def __str__(self):
        return "%s -- %s -- %s" % (self.name, self.descritpion, self.severity)
    
    def persist(self, db):
        if self.severity == "Support":
            return
        sql = "INSERT INTO rules (id, name, description, severity, rgroup, entity_type, provider) values (%s, %s, %s, %s, %s, %s, %s)"
        val = (self.id, self.name, self.descritpion, self.severity, self.group, self.entity_type, self.provider)
        print(sql, val)
        db.cursor().execute(sql, val)
        db.commit()
        #print(sql, val)
    

def insert_rule_result(db, result):
    sql = "INSERT INTO compliance_run_result (rule_id, result, message, provider, region, entity) values (%s, %s, %s, %s, %s, %s)"
    val = (result.rule_id, result.result, result.message, result.provider, result.region, result.entity)
    db.cursor().execute(sql, val)
    db.commit()


def get_rules(csv, groups):
    csv.sort_values(['TITLE_ID'])
    grp = csv.groupby("TITLE_ID")["TITLE_TEXT", "LEVEL"].apply(lambda obj: obj.loc[numpy.random.choice(obj.index), :])
    t = grp.apply(lambda row: rule(row.name, row["TITLE_TEXT"], row["LEVEL"], groups), axis=1)
    return t


def insert_all(csv_contents):
    for index, row in csv_contents.iterrows():
        if row["RESULT"] != "INFO":
            result = compliance_run_result(row["TITLE_ID"], row["NOTES"], row["RESULT"], "AWS", row["REGION"])
            insert_rule_result(db, result)

def insert_rules(rules, db):
    [x.persist(db) for x in rules.tolist()]

def parse_group(filename):
    out = subprocess.check_output("cat " +filename+ " | sed -e 's/#.*$//' -e '/^$/d' -e 's/\[[^][]*\]//g'", shell=True).decode("utf8")
    lines = out.splitlines()
    m = {}
    for line in lines:
        index = line.find("=")
        if index != -1:
            key = line[:index]
            value = line[index+1:].replace("'", "")
            m[key] = value
    g = group(m["GROUP_ID"], m["GROUP_TITLE"], m["GROUP_CHECKS"])
    return g.id, g


def get_all_groups(directory):
    result = {}
    for filename in os.listdir(directory):
        id, g = parse_group(os.path.join(directory, filename))
        result[id] = g
    return result
    

def filter_group_ids(groups, ruleName):
    result = []
    for g in groups.values():
        if ruleName in g.checks:
            result.append(g.title)
    return set(result)


groups = get_all_groups(group_dir)
print(groups)
insert_rules(get_rules(csv_contents, groups), db)
insert_all(csv_contents)

