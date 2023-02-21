from flask import render_template, request, redirect, session, url_for, flash
from flask_app import app
from flask_app.models.users_model import User
from flask_app.models.messages_model import Message

@app.route('/send_message', methods=['POST'])
def send_message():
    if not 'uid' in session:
        flash('Please log in first!')
        return redirect('/')
    Message.save(request.form)
    return redirect('/dashboard')

@app.route('/delete_message/<int:message_id>')
def delete_message(message_id):
    Message.delete(message_id)
    return redirect('/dashboard')