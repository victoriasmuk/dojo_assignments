from flask import Flask
app = Flask(__name__)

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def hello(name):
    return (f"Hi {name.capitalize()}!")

@app.route('/repeat/<int:number>/<word>')
def repeat(number, word):
    str = ""
    for i in range(number):
        str += f"<p>{word}</p>"
    return str

@app.errorhandler(404)
def not_found(e):
    return 'Sorry! No response. Try again.'

@app.route('/')
def hello_world():
    return 'Hello World!'
if __name__=="__main__":
    app.run(debug=True)




