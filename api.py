import flask
from flask import jsonify
from data import db_session
from data.__all_models import *

blueprint = flask.Blueprint(
    'api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs')
def get_jobs():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).all()
    return jsonify(
        {
            'news': [item.to_dict() for item in news]
        }
    )


@blueprint.route('/api/jobs/<int:jobs_id>', methods=['GET'])
def get_one_job(jobs_id):
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs).get(jobs_id)
    if not news:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {'jobs': news.to_dict()}
    )