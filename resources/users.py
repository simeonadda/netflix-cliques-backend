import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash

from playhouse.shortcuts import model_to_dict
from flask_login import login_user, current_user, logout_user

users = Blueprint('users', 'users') # why can't I set the import name as 'user'


@users.route('/', methods=['GET'])
def test_user_route():
    return 'user route works'

@users.route('/signup', methods=['POST'])
def signup():

    payload = request.get_json()

    payload['email'] = payload['email'].lower()
    payload['username'] = payload['username'].lower()
    print(payload)

    try:
        models.User.get(models.User.email == payload['email'])
        models.User.get(models.User.username == payload['username'])

        return jsonify(
            data = {},
            message = f"A user with this username or email address already exists.",
            status = 401
        ), 401

    except models.DoesNotExist:

        if (payload['confirm_password'] != payload['password']):
            return 'Passwords do not match'
        else:
            pw_hash = generate_password_hash(payload['password'])


            # CREATE USER
            created_user = models.User.create(
                name = payload['name'],
                username = payload['username'],
                email = payload['email'],
                password = pw_hash,
                confirm_password = pw_hash
            )


            # LOGIN NEWLY CREATED USER
            print(created_user)
            # login_user(created_user)

            # PRINT OUT CREATED USER IN DICTIONARY
            created_user_dict = model_to_dict(created_user)
            print(created_user_dict)

            # DROP PASSWORD FROM DICTIONARY
            created_user_dict.pop('password')
            created_user_dict.pop('confirm_password')

            return jsonify(
                data = created_user_dict,
                message = f"Successfully registered {created_user_dict['username']}.",
                status = 201
            ), 201
