# what_to_watch/opinions_app/error_handlers.py

<<<<<<< HEAD
# Новый импорт — jsonify.
from flask import jsonify, render_template

from . import app, db


class InvalidAPIUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None):
        super().__init__()
        self.message = message
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        return dict(message=self.message)


# Обработчик кастомного исключения для API.
@app.errorhandler(InvalidAPIUsage)
def invalid_api_usage(error):
    # Возвращает в ответе текст ошибки и статус-код.
    return jsonify(error.to_dict()), error.status_code


=======
from flask import render_template

from . import app, db

>>>>>>> 31e6075bf6b15c07b2bcf139bf6353ed248401b9
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

<<<<<<< HEAD

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
=======
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
>>>>>>> 31e6075bf6b15c07b2bcf139bf6353ed248401b9
