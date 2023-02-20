from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import user ,band,users_bands
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def homepage():
    return render_template('register.html')




@app.route('/create/user', methods = ['post'])
def create():
    if user.User.validate_user(request.form):
            pw_hash = bcrypt.generate_password_hash(request.form['password'])
            print(pw_hash)
            data ={
                'first_name': request.form['first_name'],
                'last_name': request.form['last_name'],
                'email': request.form['email'],
                'password': pw_hash
            }
            session['user_id']=user.User.save(data)
            return redirect('/dashboard')
    return redirect('/')


@app.route('/login/user', methods=['POST'])
def login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = user.User.get_by_email(data)
    if not user_in_db:
        flash("Invalid Email/Password", 'error')
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password", 'error')
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect("/dashboard")


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route("/dashboard")
def dash():
    if 'user_id' in session:
        current_user =user.User.get_by_id({'id':session['user_id']})
        bands = band.Band.get_all()
        band1 =users_bands.USER_BANDS.get_all()
        return render_template('dashboard.html',user = current_user, bands=bands, band1=band1)
    return redirect('/')
