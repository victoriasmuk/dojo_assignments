from flask_app import app
from flask import redirect, render_template,request
from flask_app.models.authors_model import Author
from flask_app.models.books_model import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def home():
    authors = Author.get_all()
    return render_template('index.html', authors=authors)

@app.route('/create_author', methods=['POST'])
def create_author():
    data = {
        'name' : request.form['name']
    }
    author_id = Author.save(data)
    return redirect('/authors')

@app.route('/author/<int:id>')
def show_author(id):
    author = Author.get_by_id(id)
    print(author)
    unfavorited_books = Book.unfavorited_books(id)
    print(unfavorited_books)
    return render_template('show_author.html', author = author, unfavorited_books = unfavorited_books)

@app.route('/join_book', methods=['POST'])
def join_book():
    data ={
        'author_id' : request.form['author_id'],
        'book_id' : request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f"/author/{request.form['author_id']}")