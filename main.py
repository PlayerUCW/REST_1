from flask import Flask
from flask_restful import Api
import user_resources
from data import db_session


app = Flask(__name__)
api = Api(app)


def main():
    db_session.global_init("db/mars.db")
    api.add_resource(user_resources.UserListResource, '/api/users')
    api.add_resource(user_resources.UserResource, '/api/users/<int:user_id>')
    app.run()


if __name__ == '__main__':
    main()