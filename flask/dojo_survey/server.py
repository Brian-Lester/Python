from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/display', methods=['post'])
def display():
    session['user'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['lang'] = request.form['lang']
    session['comment']= request.form['comment']
    return redirect('/')


@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')




if __name__=="__main__":   
    app.run(debug=True)   
