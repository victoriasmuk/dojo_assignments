from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    DB = 'emails'
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM emails;'
        results = connectToMySQL(cls.DB).query_db(query)
        list = []
        for email in results:
            list.append( cls(email) )
        return list
    
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO emails (email) VALUES (%(email)s);'
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    @classmethod
    def delete(cls,id):
        data ={
            'id' : id,
        }
        query = 'DELETE FROM emails WHERE id = %(id)s;'
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @staticmethod
    def is_valid(email):
        is_valid = True
        query = 'SELECT * FROM emails WHERE email = %(email)s;'
        results = connectToMySQL(Email.DB).query_db(query,email)
        if len(results) >= 1:
            flash('This email address has already been taken.')
            is_valid = False
        if not EMAIL_REGEX.match(email['email']):
            flash("This email address is invalid.")
            is_valid = False
        return is_valid