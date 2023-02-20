from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import post, comment


@app.route('/create/post', methods =['post'])
def create_post():
    if post.Post.validate_post(request.form):
        data ={
            'content': request.form['content'],
            'user_id': session['user_id']
        }
        post.Post.save(data)
        return redirect('/dashboard')
    return redirect('/dashboard')

@app.route("/create/comment/<int:post_id>", methods =['post'])
def create_comment(post_id):
    if 'user_id' in session:
        if comment.Comment.validate_post(request.form):
            data ={
                'content': request.form['comment'],
                'user_id': session['user_id'],
                'post_id': post_id
            }
            comment.Comment.save(data)
            return redirect('/dashboard')
        return redirect('/dashboard')
    return('/logout')
