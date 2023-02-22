from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import books_model
from flask_app import DB

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        authors = []
        results = connectToMySQL(DB).query_db(query)
        for row in results:
            authors.append(cls(row))
        return authors
    
    @classmethod
    def save(cls,data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def unfavorited_authors(cls,id):
        data = {
            'id' : id,
        }
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL(DB).query_db(query,data)
        if not results:
            return False
        for row in results:
            authors.append(cls(row))
        return authors
    
    @classmethod
    def add_favorites(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def get_by_id(cls,id):
        data = {
            'id' : id,
        }
        query = """
        SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id
        LEFT JOIN books ON books.id = favorites.book_id 
        WHERE authors.id = %(id)s;
        """
        results = connectToMySQL(DB).query_db(query,data)
        if not results:
            return False
        author = cls(results[0])
        for row in results:
            if row['books.id'] == None:
                break
            book_data = {
                'id' : row['books.id'],
                'title' : row['title'],
                'num_of_pages' : row['num_of_pages'],
                'created_at' : row['books.created_at'],
                'updated_at' : row['books.updated_at']
            }
            author.favorite_books.append(books_model.Book(book_data))
        return author
