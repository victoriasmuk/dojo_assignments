from flask import render_template, request, redirect, session, url_for
from survey_app import app
from survey_app.models.dojos_model import Dojo

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process' , methods=['POST'])
def get_info():
    session['file'] = request.form['file']

    if Dojo.is_valid(request.form):
        Dojo.save(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def show_info():
    dojo = Dojo.get_most_recent()
    return render_template('results.html', dojo = dojo)