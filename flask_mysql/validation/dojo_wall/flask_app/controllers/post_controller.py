from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import post



@app.route('/create/post', methods=['post'])
def create_post():
        if post.Post.validate_post(request.form):
                data ={
                        'content': request.form['content'],
                        'user_id': session['user_id']
                }
                print(session['user_id'])
                post.Post.save_post(data)
                return redirect('/dashboard')
        return redirect('/dashboard')
