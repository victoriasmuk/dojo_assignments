from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import users_model
from flask_app import DB
import math
from datetime import datetime

class Message:
    def __init__(self, data):
        self.id = data['id']
        self.sender_id = data['sender_id']
        self.reciever_id = data['reciever_id']
        self.sender = data['sender']
        self.content = data['content']
        self.reciever = data['reciever']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_user_messages(cls,uid):
        data = {
            'id' : uid,
        }
        query = """
        SELECT users.first_name as sender, recievers.first_name as reciever, messages.* 
        FROM users 
        LEFT JOIN messages ON users.id = messages.sender_id 
        LEFT JOIN users as recievers ON recievers.id = messages.reciever_id 
        WHERE recievers.id  =  %(id)s ORDER BY sender;
        """
        results = connectToMySQL(DB).query_db(query,data)
        messages = []
        for message in results:
            messages.append( cls(message) )
        return messages
        
    @classmethod
    def get_sender_messages(cls,uid):
        data = {
            'id' : uid,
        }
        query = 'SELECT * FROM messages WHERE sender_id =%(id)s'
        result = connectToMySQL(DB).query_db(query,data)
        return result

    @classmethod
    def save(cls,data):
        query = "INSERT INTO messages (content, sender_id, reciever_id) VALUES (%(content)s, %(sender_id)s, %(reciever_id)s);"
        result = connectToMySQL(DB).query_db(query,data)
        return result

    @classmethod
    def delete(cls, message_id):
        data = {
            'id' : message_id,
        }
        query = 'DELETE FROM messages WHERE messages.id = %(id)s;'
        result = connectToMySQL(DB).query_db(query,data)
        return result
    
    def time_span(self):
        now = datetime.now()
        delta = now - self.created_at
        print(delta.days)
        print(delta.total_seconds())
        if delta.days > 0:
            return f'{delta.days} days ago'
        elif (math.floor(delta.total_seconds() / 60)) >= 60:
            return f'{math.floor(math.floor(delta.total_seconds() / 60)/60)} hour(s) ago'
        elif delta.total_seconds() >= 60:
            return f'{math.floor(delta.total_seconds() / 60)} minutes ago'
        else:
            return f'{math.floor(delta.total_seconds())} seconds ago'