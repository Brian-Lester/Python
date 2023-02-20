from flask_app.config.mysqlconnection import connectToMySQL
from flask import  flash, request,session
from flask_app.models import user, comment
mydb ="dojo_wall"


class Post:
    def __init__( self , data ):
        self.id = data['id']
        self.content = data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id =data['user_id']
        self.creator = None

    @classmethod
    def get_all_posts(cls):
        query = "SELECT posts.*, users.first_name FROM posts JOIN users ON posts.user_id = users.id ;"

        results = connectToMySQL(mydb).query_db(query)
        print(results)

        posts= []

        for post in results:
            this_post =cls(post)
            this_post.creator =post['first_name']
            posts.append( this_post)
        return posts

    @classmethod
    def save_post(cls, data ):
        query = "INSERT INTO posts ( content , user_id) VALUES ( %(content)s , %(user_id)s );"

        results =connectToMySQL(mydb).query_db( query, data )
        print(data)
        print(results)

    @staticmethod
    def validate_post(data):
        is_valid = True
        if len(data['content']) < 1:
            flash('Post Cant be empty', 'post')
            is_valid = False
        return is_valid

