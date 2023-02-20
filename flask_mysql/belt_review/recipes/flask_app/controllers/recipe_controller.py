from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import recipe, user


@app.route('/create/recipe')
def create_recipe():
    if 'user_id' in session:
        return render_template('createRecipe.html')
    return redirect('/home')

@app.route('/save/recipe', methods= ['post'])
def save_recipe():
    if 'user_id' in session:
        if recipe.Recipe.validate_post(request.form):
            data ={
                'name': request.form['name'],
                'description': request.form['description'],
                'instructions': request.form['instructions'],
                'date': request.form['date'],
                'under_30': request.form['under_30'],
                'user_id':session['user_id'],
            }
            recipe.Recipe.save(data)
            return redirect('/dashboard')
    return redirect('/home')


@app.route('/delete/recipe/<int:id>')
def delete_recipe(id):
    if 'user_id' in session:
        recipe.Recipe.delete({'id': id})
        return redirect('/dashboard')
    return redirect('/home')

@app.route('/update/recipe/<int:id>')
def update_recipe(id):
    if 'user_id' in session:
        r = recipe.Recipe.get_by_id({'id': id})
        print(r)
        return render_template('updateRecipe.html' ,r=r)
    return redirect('/home')

@app.route('/save/recipe/<int:id>', methods= {'post'})
def save_update(id):
    if 'user_id' in session:
        if recipe.Recipe.validate_post(request.form):
            data ={
                'name': request.form['name'],
                'description': request.form['description'],
                'instructions': request.form['instructions'],
                'date': request.form['date'],
                'under_30': request.form['under_30'],
                'id':id,
            }
            recipe.Recipe.save_update(data)
            return redirect(f'/update/recipe/{id}')
        return redirect(f'/update/recipe/{id}')
    return redirect('/home')

@app.route('/show/recipe/<int:id>')
def show_recipe(id):
    if 'user_id' in session:
        r = recipe.Recipe.get_by_id({'id': id})
        current_user =user.User.get_by_id({'id':session['user_id']})
        return render_template('viewRecipe.html' ,r=r, current_user=current_user)
    return redirect('/home')

