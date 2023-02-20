from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models import books, users



@app.route('/books')
def get_all():
    book =books.Books.get_all()
    return render_template('newbook.html', book=book)



@app.route('/create/book', methods=['post'])
def create_book():
    data = {
        "title": request.form["title"],
        'num_of_pages' : request.form['num_of_pages']
    }
    books.Books.save(data)
    return redirect('/books')

@app.route('/book/<int:book_id>')
def show_book(book_id):
    data ={
        'id':book_id
    }
    user = books.Books.not_liked(data)
    book=books.Books.get_books_with_users(data)
    print(user)
    return render_template('books.html',book = book,user=user)

@app.route('/create/relationship1', methods=['post'])
def book_likes():
    book =request.form['book']
    data ={
        'user_id' : request.form['user'],
        'book_id' : book
    }
    users.Users.save_relationship(data)
    return redirect(f'/book/{book}')

