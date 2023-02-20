from flask_app.config.mysqlconnection import connectToMySQL
from flask import  flash, request
from flask_app.models import comment
mydb ="dojo_wall"


class Post:
    def __init__( self , data ):
        self.id = data['id']
        self.content= data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id =data['user_id']
        self.creator =None
        self.comments =[]

    @staticmethod
    def validate_post(user):
        is_valid =True
        if len(user['content']) <1 :
            flash('Post cant be blank silly gosse  what are you thinking why on gods green earth would you post a blank post?????????')
            is_valid =False
        return is_valid

    @classmethod
    def save(cls, data):
        query ='''
        INSERT into posts (content, user_id) Values(%(content)s, %(user_id)s)
        '''
        return connectToMySQL(mydb).query_db( query, data )

    @classmethod
    def get_all(cls):
        query = '''
        SELECT posts.* ,users.first_name FROM posts JOIN users ON users.id= posts.user_id;
        '''
        results = connectToMySQL(mydb).query_db(query)

        posts = []

        for post in results:
            print(post)
            this_post =cls(post)
            this_post.creator =post['first_name']
            posts.append( this_post)
            print(this_post)
        return posts


