from flask import Flask, jsonify, after_this_request
from flask_cors import CORS

import os
import models
from resources.users import users # why can't I set the import name as user
from resources.cliques import cliques

DEBUG = True
PORT = 8000

app = Flask(__name__)


# CORS
CORS(users, origins=['http://localhost:3000'], supports_credentials=True)
CORS(cliques, origins=['http://localhost:3000'], supports_credentials=True)

app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(cliques, url_prefix='/api/v1/cliques')


# this needs to be after blueprint
@app.before_request # use this decorator to cause a function to run before reqs
def before_request():

    """Connect to the db before each request"""
    print("you should see this before each request") # optional -- to illustrate that this code runs before each request -- similar to custom middleware in express.  you could also set it up for specific blueprints only.
    models.DATABASE.connect()

    @after_this_request # use this decorator to Executes a function after this request
    def after_request(response):
        """Close the db connetion after each request"""
        print("you should see this after each request") # optional -- to illustrate that this code runs after each request
        models.DATABASE.close()
        return response # go ahead and send response back to client


# ROUTES FOR FLASK
@app.route('/')
def index():
    return 'sup'






# ADD THESE THREE LINES -- because we need to initialize the
# tables in production too!
if os.environ.get('FLASK_ENV') != 'development':
  print('\non heroku!')
  models.initialize()




if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)