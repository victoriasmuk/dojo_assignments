from flask import Flask, render_template, request, redirect, url_for
from users import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template('index.html', users=User.get_all())

@app.route('/user/new')
def new_user():
    return render_template('add_user.html')

@app.route('/user/create', methods=['POST'])
def create_user():
    User.save(request.form)
    return redirect('/')

@app.route('/user/edit/<int:id>')
def edit_user(id):
    user = User.get_one(id)
    return render_template('edit_user.html', user = user)

@app.route('/user/show/<int:id>')
def show_user(id):
    user = User.get_one(id)
    return render_template('show_user.html', user = user)

@app.route('/user/update', methods=['POST'])
def update_user():
    User.update(request.form)
    id =request.form['id']
    return redirect(url_for('show_user', id = id))

@app.route('/user/delete/<int:id>')
def delete_user(id):
    User.delete(id)
    return redirect('/')

if __name__=='__main__':
    app.run(debug = True)
