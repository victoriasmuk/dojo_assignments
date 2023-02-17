from flask_app import app
from flask import Flask, render_template, request, redirect, url_for
from flask_app.models.ninjas_model import Ninja
from flask_app.models.dojos_model import Dojo
from flask_app.controllers import dojos_controller

@app.route('/ninjas')
def ninjas():
    ninjas = Ninja.get_with_dojo()
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', ninjas=ninjas, dojos = dojos)

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/')