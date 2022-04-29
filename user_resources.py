from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.__all_models import *


def abort_if_not_found(user_id):
    session = db_session.create_session()
    news = session.query(User).get(user_id)
    if not news:
        abort(404, message=f"User {user_id} not found")


parser = reqparse.RequestParser()
parser.add_argument('surname', required=True)
parser.add_argument('name', required=True)
parser.add_argument('age', required=True, type=int)
parser.add_argument('sex', required=True)
parser.add_argument('position', required=True)
parser.add_argument('speciality', required=True)
parser.add_argument('address', required=True)
parser.add_argument('email', required=True)
parser.add_argument('password', required=True)


parser2 = reqparse.RequestParser()
parser2.add_argument('id', required=True, type=int)
parser2.add_argument('surname', required=True)
parser2.add_argument('name', required=True)
parser2.add_argument('age', required=True, type=int)
parser2.add_argument('sex', required=True)
parser2.add_argument('position', required=True)
parser2.add_argument('speciality', required=True)
parser2.add_argument('address', required=True)
parser2.add_argument('email', required=True)
parser2.add_argument('password', required=True)


class UserResource(Resource):
    def get(self, user_id):
        abort_if_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        return jsonify({'users': user.to_dict()})

    def delete(self, user_id):
        abort_if_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})

    def post(self, user_id):
        abort_if_not_found(user_id)
        args = parser.parse_args()
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        user.surname = args['surname']
        user.name = args['name']
        user.age = args['age']
        user.sex = args['sex']
        user.position = args['position']
        user.speciality = args['speciality']
        user.address = args['address']
        user.email = args['email']
        user.set_password(args['password'])
        session.commit()
        return jsonify({'success': 'OK'})


class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict() for item in users]})

    def post(self):
        args = parser2.parse_args()
        session = db_session.create_session()
        user = User(
            id=args['id'],
            surname=args['surname'],
            name=args['name'],
            age=args['age'],
            sex=args['sex'],
            position=args['position'],
            speciality=args['speciality'],
            address=args['address'],
            email=args['email']
        )
        user.set_password(args['password'])
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})