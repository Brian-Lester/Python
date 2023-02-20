from flask_app.config.mysqlconnection import connectToMySQL
from flask import  flash, request
import re
from datetime import date
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mydb ="recipes"


class Recipe:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.under_30 =data['under_30']
        self.user_id =data ['user_id']
        self.date_made =data['date_made']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.Creator = None


    @classmethod
    def save(cls, data ):
        query = '''INSERT INTO recipes
        ( name , description , instructions, date_made, under_30, user_id) VALUES ( %(name)s , %(description)s , %(instructions)s , %(date)s , %(under_30)s , %(user_id)s);'''

        return connectToMySQL(mydb).query_db( query, data )

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM recipes WHERE id = %(id)s'

        results = connectToMySQL(mydb).query_db( query, data )
        return results



    @classmethod
    def save_update(cls,data):
        query = "UPDATE recipes SET name =%(name)s , description=%(description)s, instructions=%(instructions)s, date_made=%(date)s, under_30=%(under_30)s, updated_at=NOW() where id = %(id)s;"
        results= connectToMySQL(mydb).query_db( query, data )
        print(results)


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT recipes.*, users.first_name FROM recipes JOIN users ON recipes.user_id = users.id Where recipes.id = %(id)s;"

        results = connectToMySQL(mydb).query_db(query,data)

        this_recipe=cls(results[0])
        this_recipe.Creator =results[0]['first_name']

        return this_recipe



    @classmethod
    def get_all_recipes(cls):
        query = "SELECT recipes.*, users.first_name FROM recipes JOIN users ON recipes.user_id = users.id ;"

        results = connectToMySQL(mydb).query_db(query)
        print(results)

        recipes =[]
        print (recipes)

        for recipe in results:
            this_recipe =cls(recipe)
            this_recipe.Creator =recipe['first_name']
            recipes.append( this_recipe)
        return recipes


    @staticmethod
    def validate_post(user):
        is_valid = True
        if len(user['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        if len(user['instructions']) < 3:
            flash('Instructions must be atleast 3 charachters')
            is_valid = False
        if len(user['date']) <1:
            flash('Please pick a date')
            is_valid = False
        if (user['under_30']) == False:
            flash('Please tell us how long your recipe takes')
            is_valid =False
        return is_valid