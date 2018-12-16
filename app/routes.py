from app import app
from flask import jsonify, abort, request
import re


users = []

@app.route('/auth/signup', methods=['POST'])
def signup():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']

    email_validator = re.compile(r'[^@]+@[^@]+\.[^@]+')

    if not username.strip(' ') or not request.json or not ('username').strip(' ') in request.json:
        abort(400, "Error: username cannot be empty!!")
    if not password.strip(' ') or not request.json or not 'password' in request.json:
        abort(400, "Error: Password cannot be empty!!")
    if not email_validator.match(email):
        abort(400, "Error: Invalid email format!!")
    else:
        new_user = {
            'username': request.json['username'],
            'email': email,
            'password': request.json['password']
        }
        users.append(new_user)
    return jsonify({'Created': new_user})
    
