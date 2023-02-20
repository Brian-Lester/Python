from flask_app.config.mysqlconnection import connectToMySQL
from flask import  flash, request
mydb ="exam3"

class USER_BANDS:
    def __init__( self , data ):
        self.id =data['id']
        self.band_id = data['band_id']
        self.user_id = data['user_id']





    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users_bands ( band_id, user_id) VALUES ( %(band_id)s  ,%(user_id)s  );"

        return connectToMySQL(mydb).query_db( query, data )

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users_bands;"

        results = connectToMySQL(mydb).query_db(query)

        users = []
        for user in results:
            data ={
                'user_id': user['user_id'],
                'band_id': user['band_id']
            }
            users.append(data)
        return users

    @classmethod
    def delete(cls, data ):
        query = "Delete From users_bands WHERE id =%(id)s;"

        return connectToMySQL(mydb).query_db( query, data )