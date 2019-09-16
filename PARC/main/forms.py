from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SelectField, PasswordField, SelectMultipleField, SubmitField, BooleanField, TextAreaField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from PARC.models import  Post
from flask_login import current_user
from wtforms.fields.html5 import DateField
from wtforms_sqlalchemy.fields import QuerySelectField
import datetime
#Wtform permet de faire toute les validations
# taille, no empty, email pour que l'input de l'utilisateur soit ok

class PostForm(FlaskForm):
    title = StringField('Titre', validators=[DataRequired()])
    content = TextAreaField('Contenu', validators=[DataRequired()])
    picture = FileField('Image :', validators=[FileAllowed(['jpg','png','jpeg'])])
    submit = SubmitField('Post')

class AdminForm(FlaskForm):
    User = StringField('Titre', validators=[DataRequired()])
    mdp = StringField('Contenu', validators=[DataRequired()])
    submit = SubmitField('Post')
