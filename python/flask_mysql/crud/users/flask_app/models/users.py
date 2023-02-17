from flask_app.config.mysqlconnection import connectToMySQL

class User:
    DB = 'users'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = 'SELECT * FROM users;'
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users
    
    @classmethod
    def get_one(cls, id):
        data = {
            'id' : id,
        }
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(cls.DB).query_db(query,data)
        result = results [0]
        return cls(result)
    
    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email)
        VALUES ( %(first_name)s, %(last_name)s, %(email)s );
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def update(cls, data):
        query = """
        UPDATE users SET 
        first_name = %(first_name)s,
        last_name = %(last_name)s,
        email = %(email)s,
        updated_at = NOW()
        WHERE id = %(id)s;
        """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def delete(cls, id):
        data = {
            'id' : id,
        }
        query = "DELETE FROM users WHERE id = %(id)s;"
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
