from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime


class User(UserMixin, db.Model):
  '''Represents a user in the application'''
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key=True)
  firstname = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)
  expenses = db.relationship('Expense', backref='user', lazy=True)

  def __repr__(self):
    '''String representation of a user object. It returns
    a formated string with the name of the user'''
    return f'<User {self.firstname}>'


# Expense model definition
class Expense(db.Model):
  '''Represents an expense made by a user'''
  __tablename__ = 'expenses'
  id = db.Column(db.Integer, primary_key=True)
  category = db.Column(db.String(50), nullable=False)
  date = db.Column(db.DateTime(timezone=True), default=db.func.now())
  description = db.Column(db.String(255), nullable=False)
  amount = db.Column(db.Float(precision=2), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  def __init__(self, category, description, amount):
    self.category = category
    self.description = description
    self.amount = amount

  def __repr__(self):
    return f'<Expense {self.category}: {self.amount}>'