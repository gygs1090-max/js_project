from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    db.init_app(app)

    from . import models
    from .views import answer_views, main_views, question_views

    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    with app.app_context():
        db.create_all()
        if models.Question.query.count() == 0:
            q1 = models.Question()
            q1.subject = '안녕하세요'
            q1.content = '가입 인사드립니다 ^^'
            q1.create_date = datetime.now()

            q2 = models.Question()
            q2.subject = '두 번째 글'
            q2.content = '내용입니다'
            q2.create_date = datetime.now()

            q3 = models.Question()
            q3.subject = '나는 김원일 입니다.'
            q3.content = '나는 힘듭니다ㅎㅎ'
            q3.create_date = datetime.now()

            db.session.add_all([q1, q2, q3])
            db.session.commit()

    return app
