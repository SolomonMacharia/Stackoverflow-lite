from app import app
from flask import jsonify, abort, request
import re


users = []

all_questions = [
    {
        'id': 1,
        'title': 'The question',
        'description': 'This is the question',
        'answers': {
            'answerid': 1,
            'answer': 'This is the answer.'
        }
    },
    {
        'id': 2,
        'title': 'The question',
        'description': 'This is the question',
        'answers': {
            'answerid': 1,
            'answer': 'This is the answer.'
        }
    }
]

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
    

@app.route('/questions', methods=['GET'])
def questions():
    """ Returns all questions """
    return jsonify(all_questions)

@app.route('/questions/<int:questionId>', methods=['GET'])
def single_questions(questionId):
    """ Returns a single question with all the answers privided """
    question = [question for question in all_questions if question['id'] == questionId]
    if question == 0:
        abort(404,"Error question {} doesn't exist".format(questionId))
    return jsonify(question)