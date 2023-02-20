from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import sighting, user


@app.route('/create/relationship/<int:id>')
def user_likes(id):
    if 'user_id' in session:
        current_user = session['user_id']
        data ={
            'user_id' : current_user,
            'sighting_id' : id  
        }
        sighting.Sighting.save_relationship(data)
        return redirect(f'/view/sighting/{id}')
    return redirect('/home')

@app.route('/delete/relationship/<int:sighting_id>/<int:user_id>')
def delete_relationship(sighting_id , user_id):
    if 'user_id' in session:
        sighting.Sighting.delete_like({'sighting_id': sighting_id,
        'user_id': user_id})
        return redirect(f'/view/sighting/{sighting_id}')
    return redirect('/home')