from flask_restful import Resource, reqparse
from Models.Subscriber import Subscriber
#from api import app
# from api import SubscriberModel

class Subscribe(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required= True, type = str)
        parser.add_argument('email', required= True, type = str)
        parser.add_argument('kindle_mail', required= True, type =str)
        args = parser.parse_args()
        # SubscriberModel.add_subscriber_to_database(args['name'], args['email'], args['kindle_mail'])
        # add the subscriber to the database
        Subscriber.print()
        return {'msg': 'Welcome '+args['name']}