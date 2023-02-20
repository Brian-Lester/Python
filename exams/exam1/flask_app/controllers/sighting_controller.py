from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import sighting, user, like


@app.route('/create/sighting')
def create_sighting():
    if 'user_id' in session:
        current_user =user.User.get_by_id({'id':session['user_id']})
        return render_template('createSighting.html', user = current_user)
    return redirect('/home')

@app.route('/save/sighting', methods= ['post'])
def save_recipe():
    if 'user_id' in session:
        if sighting.Sighting.validate_post(request.form):
            data ={
                'location': request.form['location'],
                'description': request.form['description'],
                'date_seen': request.form['date_seen'],
                'how_many': request.form['how_many'],
                'user_id':session['user_id'],
            }
            sighting.Sighting.save(data)
            return redirect('/dashboard')
    return redirect('/create/sighting')


@app.route('/delete/sighting/<int:id>')
def delete_sighting(id):
    if 'user_id' in session:
        sighting.Sighting.delete({'id': id})
        return redirect('/dashboard')
    return redirect('/home')

@app.route('/edit/sighting/<int:id>')
def update_recipe(id):
    if 'user_id' in session:
        current_user =user.User.get_by_id({'id':session['user_id']})
        s = sighting.Sighting.get_by_id({'id': id})
        return render_template('updateSighting.html' ,s=s, user=current_user)
    return redirect('/home')

@app.route('/save/sighting/<int:id>', methods= {'post'})
def save_update(id):
    if 'user_id' in session:
        if sighting.Sighting.validate_post(request.form):
            data ={
                'location': request.form['location'],
                'description': request.form['description'],
                'date_seen': request.form['date_seen'],
                'how_many': request.form['how_many'],
                'user_id':session['user_id'],
                'id' : id
            }
            sighting.Sighting.save_update(data)
            return redirect(f'/edit/sighting/{id}')
        return redirect(f'/edit/sighting/{id}')
    return redirect('/home')

@app.route('/view/sighting/<int:id>')
def show_sighting(id):
    if 'user_id' in session:
        s = sighting.Sighting.get_by_id({'id': id})
        current_user =user.User.get_by_id({'id':session['user_id']})
        test = sighting.Sighting.get_sightings_with_users({'id': id})
        all_users =user.User.get_all()
        return render_template('viewSighting.html' ,s=s, user=current_user, test = test, all_users=all_users)
    return redirect('/home')



