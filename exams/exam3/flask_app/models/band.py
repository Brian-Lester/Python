from flask_app.config.mysqlconnection import connectToMySQL
from flask import  flash, request
from flask_app.models import user
mydb ="exam3"


class Band:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.genre = data['genre']
        self.city = data['city']
        self.user_id =data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.Creator = None
        self.members =[]

    @classmethod
    def get_all(cls):
        query = "SELECT bands.*, users.first_name, users.last_name, users.id FROM bands JOIN users on bands.user_id = users.id;"

        results = connectToMySQL(mydb).query_db(query)

        bands = []

        for band in results:
            this_band =cls(band)
            this_band.Creator = band['first_name'] + " " + band['last_name']
            bands.append(this_band)
        return bands

    @classmethod
    def save(cls, data ):
        query = "INSERT INTO bands ( name , genre , city, user_id) VALUES ( %(name)s , %(genre)s ,%(city)s,%(user_id)s );"

        return connectToMySQL(mydb).query_db( query, data )

    @classmethod
    def delete(cls, data):
        query = 'DELETE FROM bands WHERE id = %(id)s'

        results = connectToMySQL(mydb).query_db( query, data )
        return results

    @classmethod
    def get_by_id(cls,data):
        query = "SELECT bands.*, users.first_name, users.last_name FROM bands JOIN users ON bands.user_id = users.id WHERE bands.id = %(id)s;"

        results = connectToMySQL(mydb).query_db(query,data)

        band =cls(results[0])
        band.Creator= results[0]['first_name'] + " " + results[0]['last_name']


        return band

    @classmethod
    def save_update(cls,data):
        query = "UPDATE bands SET name =%(name)s , genre=%(genre)s, city=%(city)s, updated_at=NOW() where id = %(id)s;"
        results= connectToMySQL(mydb).query_db( query, data )


    @classmethod
    def get_bands_with_users( cls ):
        query = "SELECT * FROM bands LEFT JOIN users_bands ON users_bands.band_id = bands.id LEFT JOIN users ON users_bands.user_id = users.id ;"
        results = connectToMySQL(mydb).query_db( query )
        print(results)
        bands = []

        for band in results:
            this_band =cls(band)
            user_data = {
                "id" : band["users.id"],
                "first_name" : band["first_name"],
                "last_name" : band["last_name"],
                "email" : band["email"],
                "password" : band["password"],
                "created_at" : band["users.created_at"],
                "updated_at" : band['users.updated_at']
            }
            this_band.members.append(user.User(user_data))
            bands.append(this_band)
            print(bands)
        return bands





    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['name']) < 2:
            flash("Band name must be at least 2 characters.", 'regError')
            is_valid = False
        if len(user['genre']) < 2:
            flash("Genre must be at least 2 characters.", 'regError')
            is_valid = False
        if len(user['city']) < 1:
            flash('Please enter your city', 'regError')
        return is_valid

    @classmethod
    def get_by_user_id(cls,data):
        query = "SELECT bands.*, users.first_name, users.last_name FROM bands JOIN users ON bands.user_id = users.id WHERE bands.user_id= %(id)s;"

        results = connectToMySQL(mydb).query_db(query,data)

        bands = []

        for band in results:
            this_band =cls(band)
            this_band.Creator = band['first_name'] + " " + band['last_name']
            bands.append(this_band)
        return bands

    @classmethod
    def not_liked(cls):
        query ="SELECT * FROM users Where NOT exists (select * from exam3.users_bands where users.id = users_bands.user_id);"
        results = connectToMySQL(mydb).query_db( query)
        print (results)
        user = []
        for row_from_db in results:
            user_data = {
                "id" : row_from_db["id"]
            }
            user.append(user_data)
        return user