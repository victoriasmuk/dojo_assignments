from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'refresh_num' in session:
        session['refresh_num'] += 1
    else:
        session['refresh_num'] = 0
    return render_template("index.html", refresh_number=session['refresh_num'])

@app.route('/count')
def count():
    return redirect('/')

@app.route('/count_two')
def count_two():
    session['refresh_num'] = 1 + session['refresh_num']
    return redirect('/')

@app.route('/reset')
def reset():
    session['refresh_num'] = 0
    return redirect('/')

@app.route('/increment', methods=['POST'])
def increment():
    increment = int(request.form['increments'])
    if 'refresh_num' in session:
        session['refresh_num'] += increment - 1
    else:
        session['refresh_num'] = increment
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)