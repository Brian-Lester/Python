from flask import Flask, render_template, request, redirect, session
import random
random.randrange(1,100)
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 
x = random.randrange(1,100)

@app.route('/')
def home_page():
    if 'random' not in session:
        session ['random'] = x
    return render_template('index.html')


@app.route('/count',methods = ['post'])
def guess():
    if 'num' not in session:
        session ['num'] =int(request.form['num'])
    if 'num' in session:
        session['num'] =int(request.form['num'])
    return render_template('my_guess_is.html')

@app.route('/clear')
def clear():
    session.pop('random')
    return redirect('/')





if __name__=="__main__":   
    app.run(debug=True)   