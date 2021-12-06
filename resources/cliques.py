import models

from flask import Blueprint, request, jsonify
from flask_login import current_user

from playhouse.shortcuts import model_to_dict

cliques = Blueprint('cliques', 'cliques')

# GET CLIQUES ROUTE FOR USER
@cliques.route('/', methods=['GET'])
def cliques_index():
    result = models.Clique.select()
    print("")
    print('result of clique select query')

    current_user_cliques_dicts = [model_to_dict(clique) for clique in current_user.cliques]

    for clique_dict in current_user_cliques_dicts:
        clique_dict['owner'].pop('password')
        clique_dict['owner'].pop('confirm_password')
        clique_dict['owner'].pop('email')

    return jsonify({
        'data': current_user_cliques_dicts,
        'message': f"Successfully found {len(current_user_cliques_dicts)} cliques for {current_user.name}.",
        'status': 200
    }), 200

# CREATE CLIQUE ROUTE FOR USER
@cliques.route('/new_clique', methods=['POST'])
def create_clique():
    payload = request.get_json()
    print(payload)

    new_clique = models.Clique.create(name=payload['name'], owner=current_user.id, members=0)
    print(new_clique)

    clique_dict = model_to_dict(new_clique)
    clique_dict['owner'].pop('password')
    clique_dict['owner'].pop('confirm_password')
    clique_dict['owner'].pop('email')

    return jsonify(
        data = clique_dict,
        message = f"Successfully created {clique_dict['name']} for {clique_dict['owner']}",
        status = 201,
    ), 201

# SHOW ROUTE FOR CLIQUE
@cliques.route('/<id>', methods=['GET'])
def get_one_clique(id):
    clique = models.Clique.get_by_id(id)

    clique_dict = model_to_dict(clique)
    clique_dict['owner'].pop('password')
    clique_dict['owner'].pop('confirm_password')
    clique_dict['owner'].pop('email')

    print(clique_dict)
    return jsonify(
        data = clique_dict,
        message = "Success! 🎉",
        status = 200
    ), 200
