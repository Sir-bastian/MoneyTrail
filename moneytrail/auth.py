from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from . import db

auth = Blueprint('auth', __name__, url_prefix='/')

@auth.route('/LogIn', methods=['GET', 'POST'])
def login():
  #Logs in the user if the username and password are correct.
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    # Checking if user's email and password are correct
    user = User.query.filter_by(email=email).first()
    if user:
      if password is not None and check_password_hash(user.password, password):
        flash('Logged in successfully!', category='success')
        login_user(user, remember=True)
        return redirect(url_for('views.home'))
      else:
        flash('Incorrect password!', category='error')
    else:
      flash('Email is not valid', category='error')
  return render_template("login.html", user=current_user)


@auth.route('/LogOut', methods=['GET', 'POST'])
@login_required
def logout():
  #Handles the logout process.
  logout_user()
  return redirect(url_for('auth.login'))


@auth.route('/SignUp', methods=['GET', 'POST'])
def signup():
  #Gets user information and saves it to the database
  if request.method == 'POST':
    email = request.form.get('email')
    firstname = request.form.get('firstname')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    #Check and validated user's input if the information is correct.
    user = User.query.filter_by(email=email).first()
    if user:
      flash('Email is already in use!', category='error')
    elif email is not None and len(email) < 5:
      flash('Email must be greater than 4 characters', category="error")
    elif firstname and len(firstname) < 2:
      flash('First name must be greater than 2 characters', category="error")
    elif password1 and len(password1) < 7:
      flash('Passwords must have at least 7 characters', category="error")
    elif password1 != password2:
      flash('Passwords do not match', category="error")
    else:
      new_user = User()
      new_user.email = email
      new_user.firstname = firstname
      if password1 is not None:
        new_user.password = generate_password_hash(password1, method='pbkdf2:sha256')
      db.session.add(new_user)
      db.session.commit()
      login_user(new_user, remember=True)
      flash('Account created successfully!', category="success")
      return redirect(url_for('views.home'))

  
  return render_template("signup.html", user=current_user)