import flask
from flask import jsonify, make_response
from . import db_session
from .jobs import Jobs

blueprint1 = flask.Blueprint("news_api", __name__)


@blueprint1.route("/api/jobs", methods=["GET"])
def get_news():
    db_sess = db_session.create_session()
    jobs = db_sess.query(Jobs).all()
    if not jobs:
        return make_response(jsonify({"error": "empty"}), 400)
    return jsonify(
        {
            "jobs": [j.to_dict() for j in jobs]
        }
    )