from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 



@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/count', methods=['post'])
def count():
    if 'count' not in session:
        session['count'] = 1


    if 'total_count' not in session:
        session['total_count'] = 1
    elif 'total_count' in session:
        session['total_count'] +=1


    if request.form['click'] == 'plus1':
        if 'count' not in session:
            session['count'] = 1
        elif 'count' in session:
            session['count'] +=1


    if request.form['click'] == 'plus2':
        if 'count' not in session:
            session['count'] = session['count']
        elif 'count' in session:
            session['count'] +=2


    if request.form['click'] =='reset':
        return redirect('/destroy')

    return render_template('index.html')


@app.route('/plusx',methods=['post'])
def plusx():
    
    num = request.form['click1']
    session['count'] +=int(num)
    return render_template('index.html')

@app.route('/destroy')
def destroy_session():
    session.pop('count')
    return redirect('/')










if __name__=="__main__":   
    app.run(debug=True)   