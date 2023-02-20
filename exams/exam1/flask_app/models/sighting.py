from flask_app.config.mysqlconnection import connectToMySQL
from flask import  flash, request
import re
from datetime import date
from flask_app.models import user
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
mydb ="sightings"


class Sighting:
    def __init__( self , data ):
        self.id = data['id']
        self.location = data['location']
        self.description = data['description']
        self.date_seen = data['date_seen']
        self.how_many =data['how_many']
        self.user_id =data ['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.Creator_first = None
        self.Creator_last = None
        self.users=[]


    @classmethod
    def save(cls, data ):
        query = '''INSERT INTO sightings
        ( location , description , date_seen, how_many, user_id) VALUES ( %(location)s , %(description)s , %(date_seen)s , %(how_many)s , %(user_id)s);'''

        return connectToMySQL(mydb).query_db( query, data )

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM sightings WHERE id = %(id)s'

        results = connectToMySQL(mydb).query_db( query, data )
        return results



    @classmethod
    def save_update(cls,data):
        query = "UPDATE sightings SET location =%(location)s , description=%(description)s, date_seen=%(date_seen)s, how_many=%(how_many)s, updated_at=NOW() where id = %(id)s;"
        results= connectToMySQL(mydb).query_db( query, data )
        print(results)


    @classmethod
    def get_by_id(cls,data):
        query = "SELECT sightings.*, users.first_name ,users.last_name FROM sightings JOIN users ON sightings.user_id = users.id Where sightings.id = %(id)s;"

        results = connectToMySQL(mydb).query_db(query,data)

        this_sighting=cls(results[0])
        this_sighting.Creator_first =results[0]['first_name']
        this_sighting.Creator_last =results[0]['last_name']

        return this_sighting


    @classmethod
    def save_relationship(cls,data):
        query = "INSERT INTO likes (sighting_id,user_id) VALUES (%(sighting_id)s,%(user_id)s)"
        return connectToMySQL(mydb).query_db(query,data)






    @classmethod
    def get_all(cls):
        query = "SELECT sightings.*, users.first_name FROM sightings JOIN users ON sightings.user_id = users.id ;"

        results = connectToMySQL(mydb).query_db(query)
        print(results)

        sightings =[]
        print (sightings)

        for sighting in results:
            this_sighting =cls(sighting)
            this_sighting.Creator =sighting['first_name']
            sightings.append( this_sighting)
        return sightings

    @classmethod
    def get_sightings_with_users( cls , data ):
        query = "SELECT * FROM sightings JOIN likes ON likes.sighting_id = sightings.id  JOIN users ON likes.user_id = users.id WHERE sightings.id= %(id)s;"
        results = connectToMySQL(mydb).query_db( query , data )
        sighting = cls( results[0] )
        for row_from_db in results:
            user_data = {
                "id" : row_from_db["users.id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "email":row_from_db['email'],
                'password': row_from_db['password'],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db['updated_at']
            }
            sighting.users.append( user.User( user_data ) )
        return sighting


    @classmethod
    def delete_like(cls, data):
        query = 'DELETE FROM likes WHERE sighting_id = %(sighting_id)s  AND  user_id =%(user_id)s '

        results = connectToMySQL(mydb).query_db( query, data )
        return results


    @staticmethod
    def validate_post(user):
        is_valid = True
        if len(user['location']) < 3:
            flash("Location must be at least 3 characters.")
            is_valid = False
        if len(user['description']) < 3:
            flash("Description must be at least 3 characters.")
            is_valid = False
        if len(user['date_seen']) <1:
            flash('Please pick a date')
            is_valid = False
        if len(user['how_many']) <1:
            flash('Dont forget to tell us how many you saw!')
            is_valid =False
        elif int(user['how_many']) <1:
            flash('Number cant be negative')
        return is_valid