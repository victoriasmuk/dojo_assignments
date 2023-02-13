from flask  import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', row = 8, column = 8, col_one='red', col_two='black')

@app.route('/<int:x>')
def row(x):
    return render_template('index.html', row=x, column=8, col_one='red', col_two='black')

@app.route('/<int:x>/<int:y>')
def rows_columns(x,y):
    return render_template('index.html', row=x, column=y, col_one='red', col_two='black')


@app.route('/<int:x>/<int:y>/<string:col_one>/<string:col_two>')
def colors(x,y,col_one,col_two):
    return render_template('index.html', row=x, column=y, col_one=col_one, col_two=col_two)


if __name__=='__main__':
    app.run(debug=True)