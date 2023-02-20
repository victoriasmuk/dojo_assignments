from flask import Flask, session
app = Flask(__name__)

from flask_bcrypt import Bcrypt   
bcrypt = Bcrypt(app)

DB = 'login_registration'


app.secret_key = "hush now"