from flask import Flask
from flask_restful import Api
from endPoints.subscribe import Subscribe
from flask_sqlalchemy import SQLAlchemy
from Models import Subscriber

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = '.\database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
db = SQLAlchemy(app)

# For the first time --- Database and models
db.init_app(app)

api.add_resource(Subscribe, '/')

if __name__ == '__main__':
    app.run(debug=True)