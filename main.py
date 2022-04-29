from flask import Flask
from flask_restful import Api
import user_resources
import job_resources
from data import db_session


app = Flask(__name__)
api = Api(app)


def main():
    db_session.global_init("db/mars.db")
    api.add_resource(user_resources.UserListResource, '/api/users')
    api.add_resource(user_resources.UserResource, '/api/users/<int:user_id>')
    api.add_resource(job_resources.JobListResource, '/api/jobs')
    api.add_resource(job_resources.JobResource, '/api/jobs/<int:job_id>')
    app.run()


if __name__ == '__main__':
    main()