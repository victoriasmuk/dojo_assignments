from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def level_one():
    return render_template('index.html', title="Playground 1", number=3, color="#8EB7F7")

@app.route('/play/<int:num>')
def level_two(num):
    return render_template('index.html', title="Playground 2", number=num, color="#8EB7F7")

@app.route('/play/<int:num>/<col>')
def level_three(num, col):
    return render_template('index.html', title="Playground 3", number=num, color=col )


if __name__=="__main__":
    app.run(debug=True)

