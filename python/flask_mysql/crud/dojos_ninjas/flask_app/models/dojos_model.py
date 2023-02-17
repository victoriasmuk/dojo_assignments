from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    DB = 'dojos_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM dojos;'
        results = connectToMySQL(cls.DB).query_db(query)
        dojos = []
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos
    
    @classmethod
    def get_one(cls,id):
        data = {
            'id':id,
        }
        query = 'SELECT * FROM dojos WHERE id = %(id)s;'
        results = connectToMySQL(cls.DB).query_db(query, data)
        result = results[0]
        return cls(result)
    
    @classmethod
    def save(cls,data):
        query = 'INSERT INTO dojos (name) VALUES (%(name)s);'
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result