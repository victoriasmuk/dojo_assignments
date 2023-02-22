from flask import render_template, request, redirect, session, url_for, flash
from flask_app import app
from flask_app.models.users_model import User
from flask_app.models.recipes_model import Recipe

@app.route('/')
def index():
    return redirect('/home')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    logged_in_user = User.login(request.form)
    if logged_in_user:
        session['uid'] = logged_in_user.id
        return redirect('/recipes')
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    valid_user = User.validate(request.form)
    if not valid_user:
        return redirect('/')
    new_user = User.create(request.form)
    session['uid'] = new_user.id
    return redirect('/recipes')

@app.route('/recipes')
def dashboard():
    if not 'uid' in session:
        flash('Please log in first!')
        return redirect('/')
    logged_in_user = User.get_user_by_id(session['uid'])
    recipes = Recipe.get_with_user()
    return render_template('recipes.html', user=logged_in_user, recipes = recipes)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')