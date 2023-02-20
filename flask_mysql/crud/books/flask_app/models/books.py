from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import users


class Books:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages =data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users=[]


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results =  connectToMySQL('books_schema').query_db(query)
        books =[]
        for row in results:
            books.append(cls(row))
        print(books)
        return books


    @classmethod
    def save(cls,data):
        query = "INSERT INTO books (title,num_of_pages,created_at) VALUES (%(title)s,%(num_of_pages)s,NOW())"
        return connectToMySQL('books_schema').query_db(query,data)
    

    @classmethod
    def get_books_with_users( cls , data ):
        query = "SELECT * FROM books LEFT JOIN favorites ON favorites.book_id = books.id LEFT JOIN users ON favorites.user_id = users.id WHERE books.id= %(id)s;"
        results = connectToMySQL('books_schema').query_db( query , data )
        book = cls( results[0] )
        for row_from_db in results:
            user_data = {
                "id" : row_from_db["user_id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db['updated_at']
            }
            book.users.append( users.Users( user_data ) )
        return book


    @classmethod
    def not_liked(cls,data):
        query ="SELECT * FROM users Where NOT exists (select * from books_schema.favorites where users.id = favorites.user_id and favorites.book_id=%(id)s);"
        results = connectToMySQL('books_schema').query_db( query , data )
        print (results)
        user = []
        for row_from_db in results:
            user_data = {
                "id" : row_from_db["id"],
                "first_name" : row_from_db["first_name"],
                "last_name" : row_from_db["last_name"],
                "created_at" : row_from_db["created_at"],
                "updated_at" : row_from_db['updated_at']
            }
            user.append(user_data)
        return user