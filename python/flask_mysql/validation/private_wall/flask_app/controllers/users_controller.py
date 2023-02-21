from flask import render_template, request, redirect, session, url_for, flash
from flask_app import app
from flask_app.models.users_model import User
from flask_app.models import messages_model

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
        return redirect('/dashboard')
    return redirect('/')

@app.route('/register', methods=['POST'])
def register():
    valid_user = User.validate(request.form)
    if not valid_user:
        return redirect('/')
    new_user = User.create(request.form)
    session['uid'] = new_user.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if not 'uid' in session:
        flash('Please log in first!')
        return redirect('/')
    logged_in_user = User.get_user_by_id(session['uid'])
    users = User.get_all()
    messages = messages_model.Message.get_user_messages(session['uid'])
    sent_messages = messages_model.Message.get_sender_messages(session['uid'])
    return render_template('dashboard.html', user=logged_in_user, users = users, messages=messages, sent = sent_messages)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')