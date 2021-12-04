import models

# import http.client
#
# conn = http.client.HTTPSConnection("unogsng.p.rapidapi.com")
#
# headers = {
#     'x-rapidapi-host': "unogsng.p.rapidapi.com",
#     'x-rapidapi-key': "2ddf3bdb3fmsh2c7a93e3f9444adp14261cjsn73b6f6de5b56"
#     }
# 
# conn.request("GET", "/title?netflixid=81043135", headers=headers)
#
# res = conn.getresponse()
# data = res.read()
#
# print(data.decode("utf-8"))

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

titles = Blueprint('titles', 'titles')

@titles.route('/', methods=['GET'])
def test_title_route():
    return 'title route works'
