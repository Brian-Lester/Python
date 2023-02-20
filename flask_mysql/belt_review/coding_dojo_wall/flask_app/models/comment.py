from flask_app.config.mysqlconnection import connectToMySQL
from flask import  flash, request
mydb ="dojo_wall"


class Comment:
    def __init__( self , data ):
        self.id = data['id']
        self.content= data['content']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id =data['user_id']
        self.post_id =data['post_id']
        self.creator =None


    @staticmethod
    def validate_post(user):
        is_valid =True
        if len(user['comment']) <1 :
            flash('Post cant be blank silly gosse  what are you thinking why on gods green earth would you post a blank post?????????')
            is_valid =False
        return is_valid



    @classmethod
    def save(cls, data):
        query ='''
        INSERT into comments (content, user_id, post_id) Values(%(content)s, %(user_id)s,%(post_id)s)
        '''
        return connectToMySQL(mydb).query_db( query, data )


    @classmethod
    def get_all(cls):
        query = '''
        SELECT comments.* ,users.first_name FROM comments JOIN users ON users.id= comments.user_id ;
        '''
        results = connectToMySQL(mydb).query_db(query)

        comments = []
        for comment in results:
            this_comment =cls(comment)
            this_comment.creator =comment['first_name']
            comments.append( this_comment)
            print(this_comment)
        return comments