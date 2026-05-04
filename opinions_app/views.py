<<<<<<< HEAD
from . import app
from .models import Opinion
from random import randrange

from flask import render_template


def random_opinion():
    quantity = Opinion.query.count()
    if quantity:
        offset_value = randrange(quantity)
        opinion = Opinion.query.offset(offset_value).first()
        return opinion
=======
from random import randrange

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import OpinionForm
from .models import Opinion
from .dropbox import async_upload_files_to_dropbox
>>>>>>> 31e6075bf6b15c07b2bcf139bf6353ed248401b9


@app.route('/')
def index_view():
<<<<<<< HEAD
    opinion = random_opinion()
    # Если random_opinion() вернула None, значит, в БД нет записей.
    if opinion is None:
        abort(500)
=======
    quantity = Opinion.query.count()
    if not quantity:
        abort(500)
    offset_value = randrange(quantity)
    opinion = Opinion.query.offset(offset_value).first()
    return render_template('opinion.html', opinion=opinion)


@app.route('/add', methods=['GET', 'POST'])
# Допишите ключевое слово async к функции.
async def add_opinion_view():
    form = OpinionForm()
    if form.validate_on_submit():
        text = form.text.data
        if Opinion.query.filter_by(text=text).first() is not None:
            flash('Такое мнение уже было оставлено ранее!')
            return render_template('add_opinion.html', form=form)
        # Замените вызов синхронной функции на вызов асинхронной.
        # Обязательно добавьте ключевое слово await, 
        # так как функция async_upload_files_to_dropbox() асинхронная.
        urls = await async_upload_files_to_dropbox(form.images.data)
        opinion = Opinion(
            title=form.title.data, 
            text=text, 
            source=form.source.data,
            images=urls
        )
        db.session.add(opinion)
        db.session.commit()
        return redirect(url_for('opinion_view', id=opinion.id))
    return render_template('add_opinion.html', form=form)


@app.route('/opinions/<int:id>')
def opinion_view(id):
    opinion = Opinion.query.get_or_404(id)
>>>>>>> 31e6075bf6b15c07b2bcf139bf6353ed248401b9
    return render_template('opinion.html', opinion=opinion)
