from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import band,user, users_bands


@app.route('/create/band/save', methods = ['post'])
def create_band_save():
    if 'user_id' not in session:
        return redirect('/')
    if band.Band.validate_user(request.form):
            data ={
                'name': request.form['name'],
                'genre': request.form['genre'],
                'city': request.form['city'],
                'user_id': session['user_id']
            }
            band.Band.save(data)
            return redirect('/dashboard')
    return redirect('/create/band')

@app.route('/create/band')
def create_band():
    if 'user_id' not in session:
        return redirect('/')
    current_user =user.User.get_by_id({'id':session['user_id']})
    return render_template('newBand.html',user=current_user)

@app.route('/delete/band/<int:id>')
def delete_car(id):
    if 'user_id' not in session:
        return redirect('/')
    band.Band.delete({'id':id})
    return redirect('/dashboard')

@app.route('/update/band/<int:id>')
def update_car(id):
    if 'user_id' not in session:
        return redirect('/')
    oneband= band.Band.get_by_id({'id':id})
    return render_template('updateBand.html', c= oneband )

@app.route('/update/band/save/<int:id>', methods=['post'])
def update_car_save(id):
    if 'user_id' not in session:
        return redirect('/')
    if band.Band.validate_user(request.form) == True:
        data ={
            "id":id,
            'name': request.form['name'],
            'genre':request.form['genre'],
            'city':request.form['city'],
        }
        band.Band.save_update(data)
        return redirect('/dashboard')
    return redirect (f'/update/band/{id}')

@app.route('/create/relationship/<int:id>')
def create_relationship(id):
    if 'user_id' not in session:
        return redirect('/')
    data ={
        'band_id': id,
        'user_id': session['user_id']
    }
    users_bands.USER_BANDS.save(data)
    return redirect('/dashboard')

@app.route('/destroy/relationship/<int:id>')
def destroy(id):
    if 'user_id' not in session:
        return redirect('/')
    users_bands.USER_BANDS.delete({'id':id})
    return redirect('/dashboard')


@app.route('/mybands/<int:id>')
def my_bands(id):
    if 'user_id' not in session:
        return redirect('/')
    bands=band.Band.get_by_user_id({'id':id})
    user1 =user.User.get_by_id({'id':id})
    return render_template('mybands.html',bands=bands,user=user1)
