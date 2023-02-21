from flask import Flask, session
app = Flask(__name__)

from flask_bcrypt import Bcrypt   
bcrypt = Bcrypt(app)

DB = 'private_wall'


app.secret_key = "hush now"