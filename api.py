from flask import Flask, abort
from flask_restful import Api, Resource, reqparse
import re
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\azert\Desktop\Lab\Toastmasters_magazine_subscriber\database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS '] = False
db = SQLAlchemy(app)

# For the first time --- Database and models
db.init_app(app)

##############################################
#
#      This is models part
#
##############################################

class SubscriberModel(db.Model):
    __tablename__ = 'subscriber'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    kindle_email = db.Column(db.String(120), unique=True, nullable=False)
    def add_subscriber_to_database(_name, _email, _kindle_email):
        sub = SubscriberModel(name = _name, email = _email, kindle_email = _kindle_email)
        db.session.add(sub)
        db.session.commit()
    def __repr__(self):
        return '<User %r>' % self.name


##############################################
#
#      This is Resources part
#
##############################################
# A regular expression
# for validating an Email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

class SubscribeEndPoint(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required= True, type = str)
        parser.add_argument('email', required= True, type = str)
        parser.add_argument('kindle_email', required= True, type =str)
        args = parser.parse_args()

        ##### check input data
        # 1. check wether the name is empty
        if not args["name"]:
            return abort(400, description="Name parameter is mandatory")

        # 2. check whether the email is a valid one
        if re.fullmatch(regex, args['email']) == False:
            return abort(400, description="Invalid email")

        # 2. check whether the email is a valid one
        if re.fullmatch(regex, args['kindle_email']) == False:
            return abort(400, description="Invalid kindle email")
        try:
            SubscriberModel.add_subscriber_to_database(args['name'], args['email'], args['kindle_email'])
        except IntegrityError:
            return abort(400, "User already subscribed")
        # add the subscriber to the database
        return {'msg': 'Welcome '+args['name']+' to the newsletter'} 

api.add_resource(SubscribeEndPoint, '/Subscribe')

if __name__ == '__main__':
    app.run(debug=True)