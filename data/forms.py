import datetime

from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, IntegerField,\
    PasswordField, BooleanField, DateTimeField, SelectField, \
    SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class UserForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    sex = SelectField('Пол', choices=['Мужской', 'Женский'], validators=[DataRequired()])
    position = StringField('Должность', validators=[DataRequired()])
    speciality = StringField('Специальность', validators=[DataRequired()])
    email = EmailField('Электронная почта', validators=[DataRequired()])
    password = PasswordField('Пароль (не от почты)', validators=[DataRequired()])
    pwc = PasswordField('Повторите пароль', validators=[DataRequired()])
    submit = SubmitField('Зарегистрироваться')

class JobsForm(FlaskForm):
    job = StringField('Задание', validators=[DataRequired()])
    tl = IntegerField('ID ответственного', validators=[DataRequired()])
    loc = StringField('ID членов команды (через ", ")', validators=[DataRequired()])
    start = DateTimeField('Дата начала (по умолч. сейчас)', default=datetime.datetime.now())
    duration = IntegerField('Продолжительность, ч', validators=[DataRequired()])
    submit = SubmitField('Добавить')