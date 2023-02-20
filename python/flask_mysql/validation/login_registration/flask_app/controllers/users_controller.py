from flask import render_template, request, redirect, session, url_for, flash
from flask_app import app
from flask_app.models.users_model import User

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
        flash('Success! You are logged in!')
        return redirect('/dashboard')
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    if User.validate(request.form):
        User.create(request.form)
        session['uid'] = User.create(request.form).id
        flash("Success! You are now registered!")
        return redirect('/dashboard')
    return redirect('/')

@app.route('/dashboard')
def dashboard():
    if not 'uid' in session:
        flash('Please log in first!')
        return redirect('/')
    logged_in_user = User.get_user_by_id(session['uid'])
    return render_template('dashboard.html', user=logged_in_user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')