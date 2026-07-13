from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import AnswerForm
from pybo.models import Answer, Question

bp = Blueprint('answer', __name__, url_prefix='/answer')


@bp.route('/create/<int:question_id>', methods=('POST',))
def create(question_id):
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    if form.validate_on_submit():
        a = Answer(
            content=form.content.data,
            create_date=datetime.now(),
            question=question,
        )
        db.session.add(a)
        db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))


@bp.route('/modify/<int:answer_id>', methods=('GET', 'POST'))
def modify(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    form = AnswerForm()
    if request.method == 'POST' and form.validate_on_submit():
        answer.content = form.content.data
        db.session.commit()
        return redirect(url_for('question.detail', question_id=answer.question.id))
    if request.method == 'GET':
        form.content.data = answer.content
    return render_template('answer/answer_form.html', form=form)


@bp.route('/delete/<int:answer_id>')
def delete(answer_id):
    answer = Answer.query.get_or_404(answer_id)
    question_id = answer.question.id
    db.session.delete(answer)
    db.session.commit()
    return redirect(url_for('question.detail', question_id=question_id))
