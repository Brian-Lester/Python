from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import books


class Users:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name =data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books =[]


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results =  connectToMySQL('books_schema').query_db(query)
        users =[]
        for row in results:
            users.append(cls(row))
        return users


    @classmethod
    def save(cls,data):
        query = "INSERT INTO users (first_name,last_name,created_at) VALUES (%(first_name)s,%(last_name)s,NOW())"
        return connectToMySQL('books_schema').query_db(query,data)

    @classmethod
    def get_all_w_books(cls,data):
        query ='''
        SELECT * FROM users LEFT JOIN cars_purchased ON cars_purchased.user_id = users.id LEFT JOIN cars ON cars_purchased.car_id = cars_purchased.id WHERE users.id = %(id)s
        '''
        results = connectToMySQL('books_schema').query_db( query,data)
        user = cls( results[0] )
        for row_from_db in results:


            book_data = {
                "id" : row_from_db["book_id"],
                "title" : row_from_db["title"],
                "num_of_pages" : row_from_db["num_of_pages"],
                'created_at': row_from_db['created_at'],
                'updated_at': row_from_db['updated_at']
            }

            user.books.append(books.Books(book_data))
        return user

    @classmethod
    def save_relationship(cls,data):
        query = "INSERT INTO favorites (book_id,user_id) VALUES (%(book_id)s,%(user_id)s)"
        return connectToMySQL('books_schema').query_db(query,data)

    
    @classmethod
    def not_liked(cls,data):
        query ="SELECT * FROM books Where NOT exists (select * from books_schema.favorites where books.id = favorites.book_id and favorites.user_id=%(id)s);"
        results = connectToMySQL('books_schema').query_db( query , data )
        print (results)
        user = []
        for row_from_db in results:
            user_data = {
                "id" : row_from_db["id"],
                "title" : row_from_db["title"],
                "num_of_pages" : row_from_db["num_of_pages"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db['updated_at']
            }
            user.append(user_data)
        return user