from datetime import datetime

from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    request.form
    # for i in range(0, len(request.form)):
        # return render_template('checkout.html', test=request.form[i])
    # print(request.form)
    strawberry=request.form['strawberry']
    raspberry=request.form['raspberry']
    apple=request.form['apple']
    num = int(strawberry)+int(raspberry)+int(apple)
    firstname=request.form['first_name']
    print(f'Charging {firstname} for {num} fruits')
    return render_template("checkout.html", strawberry=strawberry,raspberry=raspberry,
    apple=apple,firstname=firstname,lastname=request.form['last_name'],
    studentid=request.form['student_id'], date =datetime.today(),num=num)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    