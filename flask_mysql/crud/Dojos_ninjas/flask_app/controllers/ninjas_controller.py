from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import ninjas ,dojos



@app.route('/new/user')
def new_user():
    dojo =dojos.Dojos.get_all()
    return render_template('new_user.html', dojo=dojo)

@app.route("/create/user", methods=['post'])
def create_user():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "dojo_id": request.form["dojo_id"],
    }
    ninjas.Ninjas.save(data)
    return redirect('/')

@app.route('/ninjas/<int:dojo_id>')
def get_by_dojo_id(dojo_id):
    dojo=dojos.Dojos.get_dojos_with_ninjas({'id': dojo_id})
    return render_template('students.html', dojo= dojo)

@app.route('/update/ninja/<int:ninja_id>')
def update_user(ninja_id):
    user=ninjas.Ninjas.get_by_id({'id': ninja_id})
    dojo =dojos.Dojos.get_all()
    return render_template('update_user.html', user = user, dojo=dojo)

@app.route('/update/user/save/<int:ninja_id>', methods=['post'])
def save_update(ninja_id):
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        'id': ninja_id,
        'dojo_id': request.form['dojo_id']
    }
    dojo_id=request.form['dojo_id']
    ninjas.Ninjas.save_update(data)
    return redirect(f'/ninjas/{dojo_id}')


@app.route('/delete/ninja/<int:ninja_id>/<int:dojo_id>')
def delete_user(ninja_id,dojo_id):
    ninjas.Ninjas.delete({'id': ninja_id})
    dojo=dojos.Dojos.get_dojos_with_ninjas({'id': dojo_id})
    return render_template('students.html', dojo= dojo)

