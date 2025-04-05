from flask import Flask, jsonify, request, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def json(self):
        return {'id': self.id, 'username': self.username, 'email': self.email}

db.create_all()

# Create a test route
@app.get('/test')
def test():
    return jsonify(message="The server is running.")

# Create a user
@app.post('/api/flask/users')
def create_user():
    try:
        data = request.get_json()
        new_user = User(username=data['username'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({
            'id' : new_user.id,
            'username' : new_user.username,
            'email' : new_user.email
        }), 201
    
    except Exception as e:
        return make_response(jsonify({'message' : 'Error creating user', 'error' : str(e)}), 500)
    

# GET ALL USERS
@app.get('/api/flask/users')
def get_users():
    try:
        users = User.query.all()
        users_data = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
        return jsonify(users_data)
    
    except Exception as e:
        return make_response(jsonify({'message' : 'Error fetching users', 'error' : str(e)}), 500)
    
# GET A USER BY ID
@app.get('/api/flask/users/<id>')
def get_user(id):
    try:
        user = User.query.filter_by(id=id).first()      # get the first user with the given id
        if user:
            return make_response(jsonify({'user' : user.json()}), 200)
        return make_response(jsonify({'message' : 'User not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message' : 'Error fetching user', 'error' : str(e)}), 500)
        
# UPDATE A USER BY ID
@app.put('/api/flask/users/<id>')
def update_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            data = request.get_json()
            user.username = data['username']
            user.email = data['email']
            db.session.commit()
            return make_response(jsonify({'message' : 'User updated successfully', 'user' : user.json()}), 200)
        return make_response(jsonify({'message' : 'User not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message' : 'Error updating user', 'error' : str(e)}), 500)
    
# DELETE A USER BY ID
@app.delete('/api/flask/users/<id>')
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        if user:
            db.session.delete(user)
            db.session.commit() 
            return make_response(jsonify({'message' : 'User deleted successfully'}), 200)
        return make_response(jsonify({'message' : 'User not found'}), 404)
    except Exception as e:
        return make_response(jsonify({'message' : 'Error deleting user', 'error' : str(e)}), 500)