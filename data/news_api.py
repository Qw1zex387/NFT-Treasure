import flask
from flask import jsonify, make_response
from . import db_session
from .news import News

blueprint = flask.Blueprint("news_api", __name__)


@blueprint.route("/api/news", methods=["GET"])
def get_news():
    db_sess = db_session.create_session()
    news = db_sess.query(News).all()
    if not news:
        return make_response(jsonify({'error': 'Not found'}), 400)
    return jsonify(
        {
            'news': news.to_dict(only=(
                'title', 'content', 'user_id', 'is_private'))
        }
    )