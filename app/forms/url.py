from tokenize import String
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from config.config import BaseConfig

class UrlForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired('Item obrigatório'), Length(min=10, max=BaseConfig._URL_MAX_SIZE) ])
    submit = SubmitField('Enviar')