#!/usr/bin/python
# -*- coding: utf-8 -*-

from controller import db
class people(db.Model):
    id = db.Column('person_id', db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    password = db.Column(db.String(100))
    usertype = db.Column(db.String(100))
    def __init__(self, username, password, type ):
        self.username = username
        self.password = password
        self.usertype=type

