from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.dojos_model import Dojo

class Ninja:
    DB = 'dojos_ninjas'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    @classmethod
    def get_with_dojo(cls):
        query = "SELECT * FROM ninjas LEFT JOIN dojos ON ninjas.dojo_id = dojos.id;"
        results = connectToMySQL(cls.DB).query_db(query)
        # print(results)
        group = []
        for row in results:
            ninja = cls(row)
            dojo_data = {
                **row,
                'id' : row['dojos.id'],
                'created_at' : row['dojos.created_at'],
                'updated_at' : row['dojos.updated_at']
            }
            ninja.dojo = Dojo(dojo_data)
            group.append(ninja)
        return group
    
    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM ninjas;'
        results = connectToMySQL(cls.DB).query_db(query)
        ninjas = []
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas


    @classmethod
    def get_ninja(cls,id):
        data = {
            'id' : id,
        }
        query = "SELECT * FROM ninjas WHERE dojo_id=%(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results

    @classmethod
    def save(cls,data):
        query = """
        INSERT INTO ninjas (first_name, last_name, age, dojo_id)
        VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s);
        """
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result