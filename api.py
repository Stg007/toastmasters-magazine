from flask import Flask
from flask_restful import Api, Resource, reqparse

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\azert\Desktop\Lab\Toastmasters_magazine_subscriber\database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
db = SQLAlchemy(app)

# For the first time --- Database and models
db.init_app(app)

##############################################

#      This is models part

##############################################

class SubscriberModel(db.Model):
    __tablename__ = 'Subscriber'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    kindle_email = db.Column(db.String(120), unique=True, nullable=False)
    def add_subscriber_to_database(_name, _email, _kindle_email):
        sub = SubscriberModel(name = _name, email = _email, kindle_email = _kindle_email)
        db.session.add(sub)
        db.session.commit()
    def __repr__(self):
        return '<User %r>' % self.name


##############################################

#      This is Resources part

##############################################

class SubscribeEndPoint(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required= True, type = str)
        parser.add_argument('email', required= True, type = str)
        parser.add_argument('kindle_mail', required= True, type =str)
        args = parser.parse_args()
        SubscriberModel.add_subscriber_to_database(args['name'], args['email'], args['kindle_mail'])
        # add the subscriber to the database
        return {'msg': 'Welcome '+args['name']} 

api.add_resource(SubscribeEndPoint, '/')

if __name__ == '__main__':
    app.run(debug=True)