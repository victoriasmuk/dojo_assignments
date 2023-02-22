from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.users_model import User
from flask_app import DB
from flask import flash

class Recipe:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.instructions = data['instructions']
        self.description = data['description']
        self.under_thirty = data['under_thirty']
        self.date_cooked = data['date_cooked']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
    
    @classmethod
    def get_with_user(cls):
        query = 'SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id;'
        results = connectToMySQL(DB).query_db(query)
        list = []
        for row in results:
            recipe = cls(row)
            user_data = {
                **row,
                'id' : row['users.id'],
                'created_at' : row['created_at'],
                'updated_at' : row['updated_at']
            }
            recipe.user = User(user_data)
            list.append(recipe)
        return list
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM recipes;'
        results = connectToMySQL(DB).query_db(query)
        recipes = []
        for recipe in results:
            recipes.append( cls(recipe) )
        return recipes
    
    @classmethod
    def get_one(cls,id):
        data = {
            'id' : id,
        }
        query = 'SELECT * FROM recipes LEFT JOIN users ON recipes.user_id = users.id WHERE recipes.id = %(id)s;'
        results = connectToMySQL(DB).query_db(query,data) 
        if not results:
            return False
        result = cls(results[0])
        user_data = {
            **results[0],
            'id' : results[0]['users.id'],
            'created_at' : results[0]['users.created_at'],
            'updated_at' : results[0]['users.updated_at']
        }
        result.user = User(user_data)
        return result
    
    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO recipes (name, description, instructions, under_thirty, date_cooked, user_id)
        VALUES (%(name)s, %(description)s, %(instructions)s, %(under_thirty)s, %(date_cooked)s, %(user_id)s);
        """
        result = connectToMySQL(DB).query_db(query,data)
        return result
    
    @classmethod
    def update(cls,data):
        query = """
        UPDATE recipes SET
        name = %(name)s,
        description = %(description)s,
        instructions = %(instructions)s,
        under_thirty = %(under_thirty)s,
        date_cooked = %(date_cooked)s,
        user_id = %(user_id)s
        WHERE id = %(id)s;
        """
        result = connectToMySQL(DB).query_db(query,data)
        return result
    
    @classmethod
    def delete(cls,id):
        data = {
            'id' : id,
        }
        query = 'DELETE FROM recipes WHERE id = %(id)s;'
        result = connectToMySQL(DB).query_db(query,data)
        return result
    
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) <= 3:
            is_valid = False
            flash('Name must be at least 3 characters!')
        if len(data['instructions']) < 3:
            is_valid = False
            flash("Instructions must be at least 3 characters!")
        if len(data['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters!")
        if  data['date_cooked'] == "":
            is_valid = False
            flash("Please select a date!")
        return is_valid