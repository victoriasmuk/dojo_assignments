from flask import Flask, render_template, request, redirect, session, url_for
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process' , methods=['POST'])
def get_info():
    lang = request.form.getlist('lang')
    sep='\t'
    language = ""
    for i in range(0, len(lang)):
        language += sep + lang[i] + sep
    session['name'] = request.form['name']
    session['gender'] = request.form['gender']
    session['location'] = request.form['location']
    session['language'] = language
    session['file'] = request.form['file']
    session['comments'] = request.form['comments']
    return redirect('/result')

@app.route('/result')
def show_info():
    return render_template('results.html')


if __name__ == "__main__":
    app.run(debug=True)