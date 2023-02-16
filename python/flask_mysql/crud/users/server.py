from flask import Flask, render_template, request, redirect
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
    return redirect('/users')

if __name__=='__main__':
    app.run(debug = True)
