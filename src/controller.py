from src import app, db
from flask import Flask ,flash, redirect, url_for, request, render_template, abort , session , json, jsonify
from flask_sqlalchemy import SQLAlchemy
import os,subprocess,MySQLdb
from werkzeug import secure_filename
from src.models import Rules, ComplianceRuleResults
# SQL CONSTANT
#DATABASE_NAME = "trial"
#DATABASE_PASSWORD = "password"
from models import *

# CONSTANTS
ADMIN = "admin"

# HTML FILES 
LOGIN_VIEW = "homepage.html"
MENU_VIEW = "menu.html"
MENU2_VIEW = "menu2.html"
RUN_VIEW = ""
ADD_RULE_VIEW = ""

# MESSAGES
INCOMPLETE_FIELD = "0Please enter all the required fields"
INVALID_USER_PASS = "0Invalid username or password"
SUCCESSFUL_LOGOUT = "1Successfully logged out"
SUCCESSFUL_SIGNUP = "1You are successfully registered"
# CONTROLLER FUNCTIONS

@app.route('/')
def pseudologin():
	if session.get('logged'):
		return redirect(url_for('menu'))
	else:
		return redirect(url_for('login'))

# LOG IN PAGE
@app.route('/login',methods=['GET', 'POST'])
def login():
	if session.get('logged'):
		return redirect(url_for('menu'))

	if request.method == 'POST':
			username = request.form.get('username')
			password = request.form.get('password')
			if not username or not password:
					return render_template(LOGIN_VIEW, msg=INCOMPLETE_FIELD)
 			if username!=ADMIN or password!=ADMIN:
					return render_template(LOGIN_VIEW, msg=INVALID_USER_PASS)
			session['logged']=1
			session['username'] = username
			return redirect(url_for('menu'))
	elif request.method == 'GET':
			return render_template(LOGIN_VIEW)

# MENU PAGE
@app.route('/menu',methods=['GET','POST'])
def menu():
	if not session.get('logged'):
		return redirect(url_for('login'))
	dic = {}
	with open('menu.json') as json_file:
		data = json.load(json_file)
		for p in data:
			for r in p['rules']:
				key = p['groupId']
				if (dic.has_key(key)):
					dic[key].append(r['ruleName'])
				else:
					dic[key]= [r['ruleName']]
				print p['groupId'], r['ruleName']
	print dic
	return render_template(MENU_VIEW, mylist=dic['group-1'])	

# MENU PAGE
@app.route('/menu2',methods=['GET','POST'])
def menu2():
	if not session.get('logged'):
		return redirect(url_for('login'))
	provider = request.args.get('provider')
        region = request.args.get('region')
        groups = request.args.get('groups')
        #results = ComplianceRuleResults.query.all()
        #r = [result.toString() for result in results]
        final_result = get_run_results()
        print(final_result)
        return render_template(MENU2_VIEW, provider=provider, region=region,
                groups = groups, results=final_result['results'])	
# RUN TEST PAGE
@app.route('/run',methods=['GET','POST'])
def run():
	if not session.get('logged'):
		return redirect(url_for('login'))
	return render_template(RUN_VIEW)	

# LOG OUT PAGE
@app.route('/logout',methods=['GET','POST'])
def logout():
    if not session.get('logged'):
        return redirect(url_for('login'))
    session.pop('username')
    session.pop('logged')
    return render_template(LOGIN_VIEW,msg=SUCCESSFUL_LOGOUT)

# REGISTER PAGE - CLIENT
@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        if request.form.get('viewbutton'):
            usertype = VIEWSTRING
        elif request.form.get('configbutton'):
            usertype = CONFIGSTRING

        if not username or not password or not usertype or not confirm_password:
            return render_template(LOGIN_VIEW,msg=INCOMPLETE_FIELD)
        if password != confirm_password:
            return render_template(LOGIN_VIEW,msg=PASSWORD_DONOTMATCH)
        return render_template(LOGIN_VIEW,msg=SUCCESSFUL_SIGNUP)
    elif request.method == 'GET':
        return render_template(LOGIN_VIEW)

# ADD NEW RULE
@app.route('/add',methods=['GET','POST'])
def add_rule():
	if not session.get('logged'):
		return redirect(url_for('login'))
	return render_template(ADD_RULE_VIEW)


@app.route('/rules')
def rules():
  rules = Rules.query.all()
  r = [rule.toString() for rule in rules]

  groups = {}
  for entry in r:
  	name = entry['name']
  	for grp in entry['groups']:
  		if grp not in groups:
  			groups[grp] = {'groupId' : grp, 'rules' : {}}

  		if name not in groups[grp]['rules']:
  			groups[grp]['rules'][name] = {'severity': entry['severity'], 'provider': entry['provider'], 'name': name}


  for g in groups:
  	groups[g]['rules'] = list(groups[g]['rules'].values())

  final_rules = list(groups.values())

  return jsonify(final_rules)

def get_run_results():
  results = ComplianceRuleResults.query.all()
  r = [result.toString() for result in results]

  groups = {}
  for entry in r:
    status = 0
    if entry['result']=="PASS":
        status = 1
    grp = entry['rule']['groups'][0]
    rule = entry['rule']['name']
    if grp not in groups:
        groups[grp] = {'group_name': grp, 'rules' : {}}

    if rule not in groups[grp]['rules']:
        groups[grp]['rules'][rule]= {'name': rule, 'stats': {'pass' : 0, 'fail' : 0}, 'messages': []}

    if status:
        groups[grp]['rules'][rule]['stats']['pass']+=1
    else:
        groups[grp]['rules'][rule]['stats']['fail']+=1

    groups[grp]['rules'][rule]['messages'].append({'message' : entry['message'], 'status': entry['result'], 'region':entry['region']})

  for g in groups:
      groups[g]['rules'] = list(groups[g]['rules'].values())
  final_result = {'results': list(groups.values())}
  return final_result



@app.route('/rule_results')
def rule_results():
#   print(json.dumps(final_result))
  final_result = get_run_results()
  return jsonify(meta = "success", result = final_result)

if __name__ == '__main__':
#db.create_all()
#db.session.close()
    app.run(debug=True,host='0.0.0.0',port=4000)
