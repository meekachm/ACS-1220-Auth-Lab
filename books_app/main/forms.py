from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, DateField, SelectField, SubmitField
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
from wtforms.validators import DataRequired, Length, ValidationError
from books_app.models import Audience, Book, Author, Genre, User

class BookForm(FlaskForm):
    """Form to create a book."""
    title = StringField('Book Title',
        validators=[DataRequired(), Length(min=3, max=80)])
    publish_date = DateField('Date Published')
    author = QuerySelectField('Author',
        query_factory=lambda: Author.query, allow_blank=False)
    audience = SelectField('Audience', choices=Audience.choices())
    genres = QuerySelectMultipleField('Genres',
        query_factory=lambda: Genre.query)
    submit = SubmitField('Submit')


class AuthorForm(FlaskForm):
    """Form to create an author."""
    name = StringField('Author Name', 
        validators=[DataRequired(), Length(min=3, max=80)])
    biography = StringField('Biography', 
        validators=[DataRequired(), Length(min=3, max=500)])
    submit = SubmitField('Submit')

    # STRETCH CHALLENGE: Add more fields here as well as in `models.py` to
    # collect more information about the author, such as their birth date,
    # country, etc.



class GenreForm(FlaskForm):
    """Form to create a genre."""
    name = StringField('Genre Name', 
        validators=[DataRequired(), Length(min=3, max=30)])
    submit = SubmitField('Submit')


class UserForm(FlaskForm):
    """Form to create a user."""
    username = StringField('Username', 
        validators=[DataRequired(), Length(min=3, max=30)])
    password = PasswordField('Password', 
        validators=[DataRequired(), Length(min=6, max=80)])
    submit = SubmitField('Submit')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Please choose another.')