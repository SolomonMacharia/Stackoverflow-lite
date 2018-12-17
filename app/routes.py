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

@app.route('/questions', methods=['POST'])
def post_question():
    title = request.json['title']
    description = request.json['description']
    if not request.json or not 'title' in request.json:
        abort(400, "Error: Invalid titile format!!")
    elif not title.strip(' '):
        abort(400, "Error :Title cannot be empty!!")
    elif not request.json or not 'description' in request.json:
        abort(400, "Error: Invalid description format!!")
    elif not description.strip(' '):
        abort(400, "Description cannot be empty!!")
    else:
        new_question = {
            'id': all_questions[-1]['id'] + 1,
            'title': title,
            'description': description
        }
        all_questions.append(new_question)
        return jsonify({'question': new_question}), 201
    
@app.route('/questions/<int:questionId>', methods=['DELETE'])
def delete_question(questionId):
    question = [question for question in all_questions if question['id'] == questionId]
    if len(question) == 0:
        abort(404, "Error: Question {} doesn't exist!!".format(questionId))
    all_questions.remove(question[0])
    return jsonify('Question {} deleted!'.format(questionId))