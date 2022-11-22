from flask import Blueprint, request, jsonify, Response



user = Blueprint('user', __name__, url_prefix= '/user')

'''http://localhost:5000/user/new'''

@user.route('/new', methods=['POST'])
def new_user():
    user = request.json['user']
    password = request.json['password']
    return Response()


@user.get('/all')
def get_users():
    return ({
        'name': 'Nicolas',
        'email': 'nicolagardo@email.com'
    })
