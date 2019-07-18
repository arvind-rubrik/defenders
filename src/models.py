#!/usr/bin/python
# -*- coding: utf-8 -*-

from controller import db
from sqlalchemy.orm import sessionmaker, relationship


class Rules(db.Model):
  __tablename__ = 'rules'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.String(100))
  description= db.Column(db.String(100))
  severity = db.Column(db.String(100))
  rgroup = db.Column(db.String(100))
  entity_type = db.Column(db.String(100))
  provider = db.Column(db.String(100))

  def __init__(self, name, description, severity, rgroup, entity, provider):
    self.name = name
    self.description = description
    self.severity = severity
    self.rgroup = rgroup
    self.entity = entity
    self.provider = provider

  def toString(self):
      groups = self.rgroup.split(",")
      return ({'name':self.name, 'description':self.description,
          'severity':self.severity, 'groups' : groups, 'provider':self.provider})
  def __repr__(self):
    return '<Rule {} {}>'.format(seld.id, self.name)  


class ComplianceRuleResults(db.Model):
  __tablename__ = 'compliance_rule_results'
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  ruleId = db.Column('rule_id', db.Integer, db.ForeignKey('rules.id'), nullable = False)
  provider = db.Column(db.String(100))
  region = db.Column(db.String(100))
  result = db.Column(db.String(100))
  message = db.Column(db.Text)
  timestamp = db.Column(db.Date)
  rule = relationship("Rules", backref="rules")
  
  def __init__(self, ruleId, provider, region, result, message,
          timestamp ):
    self.ruleId = ruleId
    self.provider = provider
    self.region = region
    self.result = result
    self.message = message
    self.timestamp = timestamp

  def __repr__(self):
    return '<Result {} {} {}>'.format(self.ruleId, self.result, self.message)
  
  def toString(self):
      return ({'name':self.ruleId, 'region':self.region,
          'message' : self.message, 'provider':self.provider, 'rule':
          self.rule.toString()})


