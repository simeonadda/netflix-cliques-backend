import models

from flask import Blueprint, request, jsonify
from flask_login import current_user

from playhouse.shortcuts import model_to_dict

titles = Blueprint('titles', 'titles')

# GET NETFLIX TITLES ROUTE FOR USER
@titles.route('/', methods=['GET'])
def titles_index():
    result = models.Title.select()
    print("")
    print('result of title select query')

    current_user_titles_dicts = [model_to_dict(title) for title in current_user.titles]

    for title_dict in current_user_titles_dicts:
        title_dict['user'].pop('password')
        title_dict['user'].pop('confirm_password')
        title_dict['user'].pop('email')

    return jsonify({
        'data': current_user_titles_dicts,
        'message': f"Successfully found {len(current_user_titles_dicts)} titles for {current_user.name}.",
        'status': 200
    }), 200

# ADD NETFLIX TITLE ROUTE FOR USER
@titles.route('/add_title', methods=['POST'])
def add_title():
    payload = request.get_json()
    print(payload)

    title = models.Title.create(user=current_user.id, image=payload['image'], title=payload['title'], titleDetails=payload['titleDetails'], filmId=payload['filmId'])
    print(title)

    title_dict = model_to_dict(title)
    title_dict['user'].pop('password')
    title_dict['user'].pop('confirm_password')
    title_dict['user'].pop('email')

    return jsonify(
        data = title_dict,
        message = f"Successfully added {title_dict['title']} for {title_dict['user']}.",
        status = 201
    ), 201

# SHOW ROUTE FOR NETFLIX TITLE
@titles.route('/<id>', methods=['GET'])
def get_one_title(id):
    title = models.Title.get_by_id(id)

    title_dict = model_to_dict(title)
    title_dict['user'].pop('password')
    title_dict['user'].pop('confirm_password')
    title_dict['user'].pop('email')

    print(title_dict)
    return jsonify(
        data = title_dict,
        message = "Success! 🎉",
        status = 200,
    ), 200

# REMOVE ROUTE FOR NETFLIX TITLE
@titles.route('/<id>', methods=['DELETE'])
def delete_title(id):
    delete_query = models.Title.delete().where(models.Title.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)

    return jsonify(
        data = {},
        message = f"Successfuly removed {id.title}.",
        status = 200,
    ), 200
