from flask_app import app
from flask import Flask, render_template, request, redirect, url_for
from flask_app.models.dojos_model import Dojo
from flask_app.models.ninjas_model import Ninja

@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template('index.html', dojos=Dojo.get_all())


@app.route('/dojo/create', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/')

@app.route('/dojo/show/<int:id>')
def show_dojo(id):
    dojo = Dojo.get_one(id)
    ninjas = Ninja.get_ninja(id)
    return render_template('show_dojo.html', dojo = dojo, ninjas=ninjas)

