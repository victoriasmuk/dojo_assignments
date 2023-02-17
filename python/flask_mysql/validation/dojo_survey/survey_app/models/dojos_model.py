from survey_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Dojo:
    DB = 'dojo_survey'
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.gender = data['gender']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO dojos (name, gender, location, language, comment)
        VALUES (%(name)s, %(gender)s, %(location)s, %(language)s, %(comment)s);
        """
        return connectToMySQL(cls.DB).query_db(query,data)
    
    @classmethod
    def get_most_recent(cls):
        query = """
        SELECT * FROM dojos ORDER BY dojos.id DESC LIMIT 1;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        result = results[0]
        return cls(result)
    
    @staticmethod
    def is_valid(dojo):
        is_valid = True
        if len(dojo['name']) < 3:
            is_valid = False
            flash("Name must be at least 3 characters.")
        if len(dojo['gender']) < 3:
            is_valid = False
            flash('Must select gender.')
        if len(dojo['location']) < 3:
            is_valid = False
            flash('Must select a location.')
        if len(dojo['language']) < 2:
            is_valid = False
            flash('Must select at least one language.')
        if len(dojo['comment']) < 1:
            is_valid = False
            flash('Must leave a comment.')
        return is_valid
        
