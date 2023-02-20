from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import users



@app.route('/')
def homepage():
    user=users.Users.get_all()
    return render_template('allorders.html', user=user)

@app.route('/create/order')
def show_form():
    return render_template('neworder.html')

@app.route('/create/order/save', methods=['post'])
def create():
    if users.Users.validate_user(request.form):
        data = {
            "name": request.form["name"],
            "cookie": request.form["cookie"],
            "boxes":request.form['num']
        }
        users.Users.save(data)
        return redirect('/')
    return redirect('/create/order')



@app.route('/edit/order/<int:user_id>')
def show_edit_form(user_id):
    user= users.Users.get_by_id({'id':user_id})
    return render_template('editorder.html',user=user)

@app.route('/update/order/save', methods=['post'])
def update():
    id =request.form['id']
    if users.Users.validate_user(request.form):
        data = {
            "name": request.form["name"],
            "cookie": request.form["cookie"],
            "boxes":request.form['num'],
            'id': id
        }
        users.Users.update(data)
        return redirect('/')
    return redirect(f'/edit/order/{id}')





