from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    import random
    if 'value' in session:
        session['value'] = session['value']
        session['count'] += 1
    else:
        session['value'] = random.randint(1, 100)
        session['count'] = 0
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['guess'])
    return redirect('/')

@app.route('/leaderboard', methods=['POST'])
def show_leaders():
    session['name'] = request.form['user']
    return render_template('leaders.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)