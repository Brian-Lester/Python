from flask import Flask, render_template,request,redirect
from users import User
app = Flask(__name__)



@app.route('/')
def home_page():
    return render_template('create.html')

@app.route('/display')
def display():
    test= User.get_all()
    return render_template('display.html', test=test)

@app.route('/delete/user/<int:user_id>')
def delete_user(user_id):
    User.delete({'id': user_id})
    return redirect('/display')

@app.route('/display/user/<int:user_id>')
def display_user(user_id):
    user=User.get_by_id({'id': user_id})
    print(user)
    return render_template('display_user.html', user = user)


@app.route('/update/user/<int:user_id>')
def update_user(user_id):
    user=User.get_by_id({'id': user_id})
    return render_template('update_user.html', user = user)


@app.route('/update/user/save/<int:user_id>', methods=['post'])
def save_update(user_id):
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
        'id': user_id
    }
    print(data)
    User.save_update(data)
    return redirect(f'/display/user/{user_id}')


@app.route('/create', methods=['post'])
def create():
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"],
    }
    User.save(data)
    return redirect('/display')












if __name__ == "__main__":
    app.run(debug=True)