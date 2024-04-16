from flask import Blueprint, render_template
from flask_login import login_user, login_required, current_user

views = Blueprint('views', __name__, url_prefix='/')

@views.route('/')
@login_required
def home():
  return render_template("home.html")