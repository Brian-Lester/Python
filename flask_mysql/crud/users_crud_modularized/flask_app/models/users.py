from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, request
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"

        results = connectToMySQL('users').query_db(query)

        users = []

        for user in results:
            users.append( cls(user))
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email, created_at, updated_at ) VALUES ( %(fname)s , %(lname)s ,%(email)s ,NOW() , NOW() );"

        return connectToMySQL('users').query_db( query, data )
                    

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM users WHERE id = %(id)s'

        results = connectToMySQL('users').query_db( query, data )
        return results
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users where id = %(id)s"

        results = connectToMySQL('users').query_db(query,data)
        print(results)

        users =[]

        for user in results:
            users.append(cls(user))
        
        print(users)

        return users
    
    @classmethod
    def save_update(cls,data):
        query = "UPDATE users SET first_name =%(fname)s , last_name=%(lname)s, email=%(email)s, updated_at=NOW() where id = %(id)s;"
        results= connectToMySQL('users').query_db( query, data )
        print(results)


    @staticmethod
    def validate_user(user):
        is_valid = True
        email =request.form['email']
        if len(user['fname']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(user['lname']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        is_valid = True
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        query ='''
        Select * FROM users where email =%(email)s
        '''
        results= connectToMySQL('users').query_db( query, email )
        print(results)
        if results < 1:
            flash("Please use a different email.")
            is_valid = False
        return is_valid




