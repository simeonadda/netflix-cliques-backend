import models

from flask import Blueprint, request, jsonify
from flask_bcrypt import generate_password_hash, check_password_hash

from playhouse.shortcuts import model_to_dict
from flask_login import login_user, current_user, logout_user

users = Blueprint('users', 'users') # why can't I set the import name as 'user'


@users.route('/', methods=['GET'])
def test_user_route():
    return 'user route works'



# USER SIGNUP ROUTE
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


# USER LOGIN ROUTE
@users.route('/login', methods=['POST'])
def login():
    payload = request.get_json()
    payload['email'] = payload['email'].lower()

    try:
        user = models.User.get(models.User.email == payload['email'])

        user_dict = model_to_dict(user)
        good_password = check_password_hash(user_dict['password'], payload['password'])

        if (good_password):
            login_user(user)
            print(f"{current_user.username} is {current_user.name} in POST login.")
            print(model_to_dict(user))

            user_dict.pop('password')
            user_dict.pop('confirm_password')

            return jsonify(
                data = user_dict,
                message = f"Successfully logged in {user_dict['username']}",
                status = 200
            ), 200

        else:
            print("Email is no good")
            return jsonify(
                data = {},
                message = "Email or password is incorrect.",
                status = 401
            ), 401

    except models.DoesNotExist:
        print("Email not found")
        return jsonify(
            data={},
            message="Email or password is incorrect.",
            status = 401
        ), 401
