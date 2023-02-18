from flask import render_template, request, redirect, session, url_for, flash
from flask_app import app
from flask_app.models.emails_model import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create_email():
    email = request.form['email']
    if Email.is_valid(request.form):
        Email.save(request.form)
        flash(f'The email address you entered ({email}) is a VALID email address! Thank you!')
        return redirect('/results')
    return redirect('/')

@app.route('/results')
def show_emails():
    return render_template('success.html', emails = Email.get_all())

@app.route('/delete/<int:id>')
def delete_email(id):
    Email.delete(id)
    return redirect('/results')