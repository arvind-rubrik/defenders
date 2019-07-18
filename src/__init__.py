#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask ,flash, redirect, url_for, request, render_template , abort , session , json
from flask_sqlalchemy import SQLAlchemy
import os,subprocess,MySQLdb
from werkzeug import secure_filename
from flask_migrate import Migrate
import logging
logging.basicConfig()
logger = logging.getLogger('logger')



app = Flask(__name__)
app.secret_key='somerandstring'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB_NAME = "compliance"
SQL_URI = "mysql://root:password@127.0.0.1/"+ DB_NAME
app.config['SQLALCHEMY_DATABASE_URI'] = SQL_URI
db = SQLAlchemy(app)
migrate = Migrate(app, db)
