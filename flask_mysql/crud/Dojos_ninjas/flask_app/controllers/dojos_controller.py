from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import dojos



@app.route('/')
def homepage():
    dojo =dojos.Dojos.get_all()
    return render_template('index.html', dojo=dojo)



@app.route('/create/dojo', methods=['post'])
def create():
    data = {
        "name": request.form["name"],
    }
    dojos.Dojos.save(data)
    return redirect('/')

