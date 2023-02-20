from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import users, books



@app.route('/')
def homepage():
    user=users.Users.get_all()
    return render_template('newuser.html', user=user)



@app.route('/create/user', methods=['post'])
def create():
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
    }
    users.Users.save(data)
    return redirect('/')

@app.route('/user/<int:user_id>')
def get_user(user_id):
    user=users.Users.get_all_w_books({'id':user_id})
    book = users.Users.not_liked({'id':user_id})
    return render_template('user.html', user=user, book=book)

@app.route('/create/relationship', methods=['post'])
def user_likes():
    user =request.form['user']
    data ={
        'user_id' : user,
        'book_id' : request.form['book']  
    }
    users.Users.save_relationship(data)
    return redirect(f'/user/{user}')



