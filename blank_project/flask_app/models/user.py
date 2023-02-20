from flask_app.config.mysqlconnection import connectToMySQL
from flask import  flash, request
import re
from datetime import date
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mydb ="users_login_reg"



class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password =data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users_login_reg;"

        results = connectToMySQL(mydb).query_db(query)

        users = []

        for user in results:
            users.append( cls(user))
        return users

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users_login_reg ( first_name , last_name , email, password) VALUES ( %(first_name)s , %(last_name)s ,%(email)s,%(password)s );"

        return connectToMySQL(mydb).query_db( query, data )
                    

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM users_login_reg WHERE id = %(id)s'

        results = connectToMySQL(mydb).query_db( query, data )
        return results
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM users_login_reg where id = %(id)s"

        results = connectToMySQL(mydb).query_db(query,data)


        return cls(results[0])
    
    @classmethod
    def save_update(cls,data):
        query = "UPDATE users_login_reg SET first_name =%(first_name)s , last_name=%(last_name)s, email=%(email)s, updated_at=NOW() where id = %(id)s;"
        results= connectToMySQL(mydb).query_db( query, data )



    @staticmethod
    def validate_user(user):
        is_valid = True
        if user['first_name'].isalpha() ==False:
            flash('Only alphanumeric Charachters are allowed', 'regError')
            is_valid=False
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters.", 'regError')
            is_valid = False
        if user['last_name'].isalpha() ==False:
            flash('Only alphanumeric Charachters are allowed', 'regError')
            is_valid=False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters.", 'regError')
            is_valid = False
        if len(user['password']) < 8:
            flash('Password must be atleast 8 charachters', 'regError')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash('Passwords dont match', 'regError')
            is_valid = False
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'regError')
            is_valid = False
        query ='''
        Select * FROM users_login_reg where email =%(email)s
        '''
        results= connectToMySQL(mydb).query_db( query,{'email':user['email']} )
        if len(results) >= 1:
            flash("Please use a different email.", 'regError')
            is_valid = False
        return is_valid

    # @staticmethod
    # def age(birthdate):
    #     today = date.today()
    #     age = today.year - int(birthdate[0]) - ((today.month, today.day) < (int(birthdate[5]), int(birthdate[6])))
    #     print(birthdate)
    #     print(int(birthdate[0]))
    #     print(int(birthdate[1]))
    #     print(int(birthdate[3]))
    #     print(date.today())
    #     print(today.year)
    #     print(today.month)
    #     print(today.day)
    #     print(age)
    #     return age

    @classmethod
    def get_by_email(cls,data):
        query = "SELECT * FROM users_login_reg WHERE email = %(email)s;"
        result = connectToMySQL(mydb).query_db(query,data)
        if len(result) < 1:
            return False
        return cls(result[0])
