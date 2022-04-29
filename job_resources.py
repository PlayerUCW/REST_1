from flask import jsonify
from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.__all_models import *
import datetime


def abort_if_not_found(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"Job {job_id} not found")


parser = reqparse.RequestParser()
parser.add_argument('team_leader', required=True, type=int)
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=True, type=int)
parser.add_argument('collaborators', required=True)
parser.add_argument('start_date', required=True)
parser.add_argument('end_date', required=True)
parser.add_argument('is_finished', required=True, type=bool)

parser2 = reqparse.RequestParser()
parser2.add_argument('id', required=True, type=int)
parser2.add_argument('team_leader', required=True, type=int)
parser2.add_argument('job', required=True)
parser2.add_argument('work_size', required=True, type=int)
parser2.add_argument('collaborators', required=True)
parser2.add_argument('start_date', required=True)
parser2.add_argument('end_date', required=True)
parser2.add_argument('is_finished', required=True, type=bool)


class JobResource(Resource):
    def get(self, job_id):
        abort_if_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'jobs': job.to_dict()})

    def delete(self, job_id):
        abort_if_not_found(job_id)
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})

    def post(self, job_id):
        abort_if_not_found(job_id)
        args = parser.parse_args()
        session = db_session.create_session()
        job = session.query(Jobs).get(job_id)
        job.team_leader = args['team_leader']
        job.job = args['job']
        job.work_size = args['work_size']
        job.collaborators = args['collaborators']
        job.start_date = datetime.datetime.strptime(args['start_date'], "%m/%d/%Y, %H:%M:%S")
        job.end_date = datetime.datetime.strptime(args['end_date'], "%m/%d/%Y, %H:%M:%S")
        job.is_finished = args['is_finished']
        session.commit()
        return jsonify({'success': 'OK'})


class JobListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict() for item in jobs]})

    def post(self):
        args = parser2.parse_args()
        session = db_session.create_session()
        job = Jobs(
            id=args['id'],
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=datetime.datetime.strptime(args['start_date'], "%m/%d/%Y, %H:%M:%S"),
            end_date=datetime.datetime.strptime(args['end_date'], "%m/%d/%Y, %H:%M:%S"),
            is_finished=args['is_finished']
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})