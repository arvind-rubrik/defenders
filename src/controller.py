#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask ,flash, redirect, url_for, request, render_template , abort , session , json
from flask_sqlalchemy import SQLAlchemy
import os,subprocess,MySQLdb
from werkzeug import secure_filename

app = Flask(__name__)
app.secret_key='somerandstring'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#SQL_URI = "mysql://root:"+DATABASE_PASSWORD+"@localhost/"+DATABASE_NAME
#app.config['SQLALCHEMY_DATABASE_URI'] = SQL_URI
db = SQLAlchemy(app)

# SQL CONSTANT
#DATABASE_NAME = "trial"
#DATABASE_PASSWORD = "password"
from models import *

# CONSTANTS
ADMIN = "admin"

# HTML FILES 
LOGIN_VIEW = "homepage.html"
MENU_VIEW = "menu.html"
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
	return render_template(MENU_VIEW)	

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

if __name__ == '__main__':
#db.create_all()
#db.session.close()
    app.run(debug=True,host='0.0.0.0',port=4000)