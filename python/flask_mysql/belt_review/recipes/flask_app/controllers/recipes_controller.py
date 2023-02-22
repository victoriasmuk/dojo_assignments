from flask import render_template, request, redirect, session, url_for, flash
from flask_app import app
from flask_app.models.users_model import User
from flask_app.models.recipes_model import Recipe


@app.route('/recipes/new')
def new_recipe():
    if not 'uid' in session:
        flash('Please log in first!')
        return redirect('/')
    logged_in_user = User.get_user_by_id(session['uid'])
    return render_template('add_recipe.html', user=logged_in_user)

@app.route('/recipes/create', methods =['POST'])
def create_recipe():
    if not 'uid' in session:
        flash('Please log in first!')
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        return redirect('/recipes/new')
    Recipe.save(request.form)
    return redirect('/recipes')

@app.route('/recipes/edit/<int:recipe_id>')
def edit(recipe_id):
    recipe = Recipe.get_one(recipe_id)
    logged_in_user = User.get_user_by_id(session['uid'])
    ip_addr = request.remote_addr

    if not 'uid' in session:
        flash('Please log in first!')
        return redirect('/')
    
    if session['uid'] != recipe.user_id:
        flash("Naughty naughty, you can't do this!")
        flash(f"Recipe {recipe.id} isn't yours!")
        flash(f"Your ip address {ip_addr} has been recorded.")
        return render_template('error.html', user=logged_in_user)
    
    return render_template('edit_recipe.html', recipe=recipe, user=logged_in_user)

@app.route('/recipes/update', methods=['POST'])
def update_recipe():
    if not 'uid' in session:
        flash('Please log in first!')
        return redirect('/')
    if not Recipe.validate_recipe(request.form):
        recipe_id =request.form['id']
        return redirect(url_for('edit', recipe_id = recipe_id))
    Recipe.update(request.form)
    return redirect('/recipes')

@app.route('/recipes/<int:recipe_id>')
def show(recipe_id):
    if not 'uid' in session:
        flash('Please log in first!')
        return redirect('/')
    recipe = Recipe.get_one(recipe_id)
    logged_in_user = User.get_user_by_id(session['uid'])
    return render_template('show_recipe.html', recipe=recipe, user=logged_in_user)


@app.route('/recipes/delete/<int:recipe_id>')
def delete(recipe_id):
    recipe = Recipe.get_one(recipe_id)
    logged_in_user = User.get_user_by_id(session['uid'])
    ip_addr = request.remote_addr

    if not 'uid' in session:
        flash('Please log in first!')
        return redirect('/')
    if session['uid'] != recipe.user_id:
        flash("Naughty naughty, you can't do this! This recipe isn't yours!")
        return render_template('error.html', user=logged_in_user, ip = ip_addr)

    Recipe.delete(recipe_id)
    return redirect('/recipes')