import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

titles = Blueprint('titles', 'titles')

@titles.route('/', methods=['GET'])
def test_title_route():
    return 'title route works'
