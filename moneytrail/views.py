from flask import Blueprint, render_template, request, flash, redirect
from flask_login import login_user, login_required, current_user
from .models import Expense
from . import db

views = Blueprint('views', __name__, url_prefix='/')

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
  return render_template("home.html", user=current_user)

# Route to display all expenses
@views.route('/expenses', methods=['GET'])
def expenses():
    expenses = Expense.query.all()
    return render_template('expenses.html', expenses=expenses, user=current_user)


# Route to display the form for adding expenses
@views.route('/add-expense', methods=['GET'])
def add_expense_form():
    return render_template('add_expense.html', user=current_user)


# Route to handle the form submission and create a new expense
@views.route('/add-expense', methods=['POST'])
def add_expense():
    category = request.form['category']
    description = request.form['description']
    amount = float(request.form['amount'])

    # Create a new Expense object
    expense = Expense(category=category, description=description, amount=amount)

    # Add the expense to the database
    db.session.add(expense)
    db.session.commit()

    return redirect('/expenses') # Redirect to the expenses page or any other desired page


# Route to display the form for updating an expense
@views.route('/edit-expense/<int:expense_id>', methods=['GET'])
def edit_expense_form(expense_id):
    expense = Expense.query.get(expense_id)
    return render_template('edit_expense.html', expense=expense, user=current_user)


# Route to handle the form submission and update an expense
@views.route('/edit-expense/<int:expense_id>', methods=['POST'])
def edit_expense(expense_id):
    expense = Expense.query.get(expense_id)
    expense.category = request.form['category']
    expense.description = request.form['description']
    expense.amount = float(request.form['amount'])

    db.session.commit()

    return redirect('/expenses')  # Redirect to the expenses page or any other desired page


# Route to delete an expense
@views.route('/delete-expense/<int:expense_id>', methods=['POST'])
def delete_expense(expense_id):
    expense = Expense.query.get(expense_id)
    db.session.delete(expense)
    db.session.commit()

    return redirect('/expenses')  # Redirect to the expenses page or any other desired page