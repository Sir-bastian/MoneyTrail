from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "moneytrail.db"

def create_app():
  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'secret'
  app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
  db.init_app(app)

  from .views import views
  from .auth import auth

  app.register_blueprint(auth, url_prefix='/')
  app.register_blueprint(views, url_prefix='/')

  from .models import User, Expense

  with app.app_context():
    if not path.exists('moneytrail/' + DB_NAME):
      db.create_all()
      print('Database created successfully!')
  '''
  Set up and configure the Flask-Login extension for
  user authentication and session management
  '''
  login_manager = LoginManager()
  login_manager.login_view = 'auth.login'
  login_manager.init_app(app)

  @login_manager.user_loader
  def load_user(id):
    return User.query.get(int(id))

  
  return app