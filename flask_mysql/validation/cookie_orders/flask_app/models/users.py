from flask_app.config.mysqlconnection import connectToMySQL 
from flask import request, session, flash



class Users:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.cookie =data['cookie']
        self.boxes =data['boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cookies;"
        results =  connectToMySQL('cookies').query_db(query)
        orders =[]
        print(orders)
        for row in results:
            orders.append(cls(row))
        return orders
    
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM cookies WHERE id = %(id)s"
        results =  connectToMySQL('cookies').query_db(query,data)
        orders =[]
        print(orders)
        for row in results:
            orders.append(cls(row))
        return orders


    @classmethod
    def save(cls,data):
        query = "INSERT INTO cookies (name,cookie,boxes) VALUES (%(name)s,%(cookie)s,%(boxes)s)"
        return connectToMySQL('cookies').query_db(query,data)

    @classmethod
    def update(cls,data):
        query = "UPDATE cookies SET name =%(name)s, cookie=%(cookie)s, boxes=%(boxes)s WHERE id =%(id)s"
        return connectToMySQL('cookies').query_db(query,data)



    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['name']) < 3:
            flash("First name must be at least 3 characters.",'error')
            is_valid = False
        if len(user['cookie']) < 3:
            flash("Last name must be at least 3 characters.",'error')
            is_valid = False
        if len(user['num']) <1:
            flash('Looks like you forgot to put how many you would like')
            is_valid=False
        elif int(user['num']) <1:
            flash('Must oder at least one box!', 'error')
            is_valid = False
        return is_valid
