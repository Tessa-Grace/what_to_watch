<<<<<<< HEAD
from flask_wtf.file import FileAllowed, MultipleFileField
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length
=======
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, MultipleFileField
from wtforms import StringField, SubmitField, TextAreaField, URLField
from wtforms.validators import DataRequired, Length, Optional
>>>>>>> 31e6075bf6b15c07b2bcf139bf6353ed248401b9


class OpinionForm(FlaskForm):
    title = StringField(
        'Введите название фильма',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, 128)]
    )
    text = TextAreaField(
        'Напишите мнение',
        validators=[DataRequired(message='Обязательное поле')]
    )
    source = URLField(
        'Добавьте ссылку на подробный обзор фильма',
        validators=[Length(1, 256), Optional()]
    )
<<<<<<< HEAD
    # Добавьте новое поле в форму.
    images = MultipleFileField()
    submit = SubmitField('Добавить')
=======
>>>>>>> 31e6075bf6b15c07b2bcf139bf6353ed248401b9
    images = MultipleFileField(
        validators=[
            FileAllowed(
                # Список разрешенных расширений для файлов.
<<<<<<< HEAD
                ['jpg', 'jpeg', 'png', 'gif', 'bmp'], 
=======
                ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
>>>>>>> 31e6075bf6b15c07b2bcf139bf6353ed248401b9
                # Сообщение, в случае если расширение не совпадает.
                message=(
                    'Выберите файлы с расширением '
                    '.jpg, .jpeg, .png, .gif или .bmp'
                )
            )
        ]
<<<<<<< HEAD
    ) 
=======
    )
    submit = SubmitField('Добавить')
>>>>>>> 31e6075bf6b15c07b2bcf139bf6353ed248401b9
