import random
from flask import Flask,render_template,redirect,session,request
app = Flask(__name__)
app.secret_key = "Keep it secret Keep it safe"
# ----------------------------------------------------------------------

@app.route('/')
def index():
    return render_template("index.html")
# --------------------------------------------
@app.route('/showResult', methods=['post'])
def showResult():
    session['number'] = request.form['inputNumber']
    session['random_number']  = 5
    if session['random_number'] == int(session['number']):
        return redirect('/win')
    elif session['random_number'] < int(session['number']) :
        session['result'] = 'Too Big'
        return render_template('gameResult.html' , numHint = session['result'])
    elif session['random_number'] > int(session['number']):
        session['result'] = 'Too Low'
        return render_template('gameResult.html' , numHint = session['result'])

@app.route('/win')
def win():
    return render_template("WinNumber.html")
# ----------------------------------------------------------------------
if __name__=='__main__':
    app.run(debug=True)