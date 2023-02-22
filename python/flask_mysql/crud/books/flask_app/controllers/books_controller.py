from flask_app import app
from flask import redirect, render_template, request
from flask_app.models.authors_model import Author
from flask_app.models.books_model import Book

@app.route('/books')
def books():
    books = Book.get_all()
    return render_template('books.html', books=books)

@app.route('/create_book', methods=['POST'])
def create_book():
    data = {
        'title' : request.form['title'],
        'num_of_pages' : request.form['num_of_pages']
    }
    book_id = Book.save(data)
    return redirect('/books')

@app.route('/book/<int:id>')
def show_book(id):
    book = Book.get_by_id(id)
    unfavorited_authors = Author.unfavorited_authors(id)
    return render_template('show_book.html', book = book, unfavorited_authors= unfavorited_authors)

@app.route('/join_author', methods=['POST'])
def join_author():
    data = {
        'author_id' : request.form['author_id'],
        'book_id' : request.form['book_id']
    }
    Author.add_favorites(data)
    return redirect(f"/book/{request.form['book_id']}")