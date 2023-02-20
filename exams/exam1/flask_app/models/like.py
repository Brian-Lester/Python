from flask_app.config.mysqlconnection import connectToMySQL
from flask import  flash, request
mydb ="sightings"


class Likes:
    def __init__( self , data ):
        self.id = data['id']
        self.user_id = data['user_id']
        self.sighting_id = data['sighting_id']



    
    @classmethod
    def get_all_likes(cls):
        query= 'Select * from likes'

        results = connectToMySQL(mydb).query_db(query)

        likes = []
        print(likes)

        for like in results:
            likes.append( cls(like))
        return likes

