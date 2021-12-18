import models

from flask import Blueprint, request, jsonify
from flask_login import current_user

from playhouse.shortcuts import model_to_dict

titles = Blueprint('titles', 'titles')

# GET NETFLIX WATCHING NOW TITLES ROUTE FOR USER
@titles.route('/watching_now', methods=['GET'])
def watching_now_titles_index():
    result = models.WatchingNowTitle.select()
    print("")
    print('result of title select query')

    current_user_watching_now_titles_dicts = [model_to_dict(title) for title in current_user.watched_titles]

    for title_dict in current_user_watching_now_titles_dicts:
        title_dict['user'].pop('password')
        title_dict['user'].pop('confirm_password')
        title_dict['user'].pop('email')

    return jsonify({
        'data': current_user_watching_now_titles_dicts,
        'message': f"Successfully found {len(current_user_watching_now_titles_dicts)} titles for {current_user.name}.",
        'status': 200
    }), 200

# GET NETFLIX FAVORITE TITLES ROUTE FOR USER
@titles.route('/favorites', methods=['GET'])
def favorites_titles_index():
    result = models.FavoritesTitle.select()
    print("")
    print('result of title select query')

    current_user_favorites_titles_dicts = [model_to_dict(title) for title in current_user.favorites_titles]

    for title_dict in current_user_favorites_titles_dicts:
        title_dict['user'].pop('password')
        title_dict['user'].pop('confirm_password')
        title_dict['user'].pop('email')

    return jsonify({
        'data': current_user_favorites_titles_dicts,
        'message': f"Successfully found {len(current_user_favorites_titles_dicts)} titles for {current_user.name}.",
        'status': 200
    }), 200

# GET NETFLIX WATCHING NEXT TITLES ROUTE FOR USER
@titles.route('/watching_next', methods=['GET'])
def watching_next_titles_index():
    result = models.WatchingNextTitle.select()
    print("")
    print('result of title select query')

    current_user_watching_next_titles_dicts = [model_to_dict(title) for title in current_user.watching_next_titles]

    for title_dict in current_user_watching_next_titles_dicts:
        title_dict['user'].pop('password')
        title_dict['user'].pop('confirm_password')
        title_dict['user'].pop('email')

    return jsonify({
        'data': current_user_watching_next_titles_dicts,
        'message': f"Successfully found {len(current_user_watching_next_titles_dicts)} titles for {current_user.name}.",
        'status': 200
    }), 200

# GET NETFLIX WATCHED TITLES ROUTE FOR USER
@titles.route('/watched', methods=['GET'])
def watched_titles_index():
    result = models.WatchedTitle.select()
    print("")
    print('result of title select query')

    current_user_watched_titles_dicts = [model_to_dict(title) for title in current_user.watched_titles]

    for title_dict in current_user_watched_titles_dicts:
        title_dict['user'].pop('password')
        title_dict['user'].pop('confirm_password')
        title_dict['user'].pop('email')

    return jsonify({
        'data': current_user_watched_titles_dicts,
        'message': f"Successfully found {len(current_user_watched_titles_dicts)} titles for {current_user.name}.",
        'status': 200
    }), 200

# ================================================================

# ADD NETFLIX WATCHING NOW TITLE ROUTE FOR USER
@titles.route('/add_watching_now_title', methods=['POST'])
def add_watching_now_title():
    payload = request.get_json()
    print(payload)

    title = models.WatchingNowTitle.create(user=current_user.id, img=payload['img'], title=payload['title'], synopsis=payload['synopsis'], year=payload['year'])
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

# ADD NETFLIX FAVORITES TITLE ROUTE FOR USER
@titles.route('/add_favorites_title', methods=['POST'])
def add_favorites_title():
    payload = request.get_json()
    print(payload)

    title = models.FavoritesTitle.create(user=current_user.id, img=payload['img'], title=payload['title'], synopsis=payload['synopsis'], year=payload['year'])
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

# ADD NETFLIX WATCHING NEXT TITLE ROUTE FOR USER
@titles.route('/add_watching_next_title', methods=['POST'])
def add_watching_next_title():
    payload = request.get_json()
    print(payload)

    title = models.WatchingNextTitle.create(user=current_user.id, img=payload['img'], title=payload['title'], synopsis=payload['synopsis'], year=payload['year'])
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

# ADD NETFLIX WATCHED TITLE ROUTE FOR USER
@titles.route('/add_watched_title', methods=['POST'])
def add_watched_title():
    payload = request.get_json()
    print(payload)

    title = models.WatchedTitle.create(user=current_user.id, img=payload['img'], title=payload['title'], synopsis=payload['synopsis'], year=payload['year'])
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

# =================================================================


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

#========================================================================

# REMOVE ROUTE FOR NETFLIX WATCHING NOW TITLE
@titles.route('/<id>', methods=['DELETE'])
def delete_watching_now_title(id):
    delete_query = models.WatchingNowTitle.delete().where(models.WatchingNowTitle.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)

    return jsonify(
        data = {},
        message = f"Successfuly removed {id.title}.",
        status = 200,
    ), 200

# REMOVE ROUTE FOR NETFLIX FAVORITES TITLE
@titles.route('/<id>', methods=['DELETE'])
def delete_favorites_title(id):
    delete_query = models.FavoritesTitle.delete().where(models.FavoritesTitle.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)

    return jsonify(
        data = {},
        message = f"Successfuly removed {id.title}.",
        status = 200,
    ), 200

# REMOVE ROUTE FOR NETFLIX WATCHING NEXT TITLE
@titles.route('/<id>', methods=['DELETE'])
def delete_watching_next_title(id):
    delete_query = models.WatchingNextTitle.delete().where(models.WatchingNextTitle.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)

    return jsonify(
        data = {},
        message = f"Successfuly removed {id.title}.",
        status = 200,
    ), 200

# REMOVE ROUTE FOR NETFLIX WATCHED TITLE
@titles.route('/<id>', methods=['DELETE'])
def delete_watched_title(id):
    delete_query = models.WatchedTitle.delete().where(models.WatchedTitle.id == id)
    nums_of_rows_deleted = delete_query.execute()
    print(nums_of_rows_deleted)

    return jsonify(
        data = {},
        message = f"Successfuly removed {id.title}.",
        status = 200,
    ), 200
