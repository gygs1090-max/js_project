from datetime import datetime

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

from pybo import db
from pybo.forms import AnswerForm, QuestionForm
from pybo.models import Question

bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list')
def _list():
    page = request.args.get('page', type=int, default=1)
    query = Question.query.order_by(Question.create_date.desc())
    pagination = query.paginate(page=page, per_page=10)
    return render_template(
        'question/question_list.html',
        question_list=pagination.items,
        pagination=pagination,
        page=page,
        keyword='',
    )


@bp.route('/detail/<int:question_id>')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    form = AnswerForm()
    return render_template(
        'question/question_detail.html',
        question=question,
        form=form,
    )


@bp.route('/create', methods=('GET', 'POST'))
def create():
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit():
        q = Question(
            subject=form.subject.data,
            content=form.content.data,
            create_date=datetime.now(),
        )
        db.session.add(q)
        db.session.commit()
        return redirect(url_for('question._list'))
    return render_template('question/question_form.html', form=form)


@bp.route('/modify/<int:question_id>', methods=('GET', 'POST'))
def modify(question_id):
    question = Question.query.get_or_404(question_id)
    if request.method == 'GET':
        form = QuestionForm()
        form.subject.data = question.subject
        form.content.data = question.content
    else:
        form = QuestionForm()
        if form.validate_on_submit():
            question.subject = form.subject.data
            question.content = form.content.data
            db.session.commit()
            return redirect(url_for('question.detail', question_id=question_id))
    return render_template('question/question_form.html', form=form)


@bp.route('/search')
def search():
    keyword = request.args.get('kw', '').strip()
    page = request.args.get('page', type=int, default=1)
    query = Question.query.order_by(Question.create_date.desc())

    if keyword:
        like = f'%{keyword}%'
        query = query.filter(
            db.or_(
                Question.subject.like(like),
                Question.content.like(like),
            )
        )

    pagination = query.paginate(page=page, per_page=10)
    return render_template(
        'question/question_list.html',
        question_list=pagination.items,
        pagination=pagination,
        page=page,
        keyword=keyword,
    )


@bp.route('/delete/<int:question_id>')
def delete(question_id):
    question = Question.query.get_or_404(question_id)
    db.session.delete(question)
    db.session.commit()
    return redirect(url_for('question._list'))
