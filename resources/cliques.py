import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

cliques = Blueprint('cliques', 'cliques')


@cliques.route('/', methods=['GET'])
def test_clique_route():
    return 'clique route works'
