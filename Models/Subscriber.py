from api import db

# class Subscriber(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=True)
#     kindle_email = db.Column(db.String(120), unique=True, nullable=False)


#     def add_subscriber_to_database(_name, _email, _kindle_email):
#         sub = Subscriber(name = _name, email = _email, kindle_email = _kindle_email)
#         db.session.add(sub)
#         db.session.commit()


class Subscriber():
    def print():
        print('Hello')
