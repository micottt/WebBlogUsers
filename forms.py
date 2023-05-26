from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField


##WTForm

class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()],
                          render_kw={"placeholder": "Leaving this field blank sets a default image."})
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")
    #
    # def __init__(self, *args, **kwargs):
    #     super(CreatePostForm, self).__init__(*args, **kwargs)
    #     self.img_url.default = "https://media.istockphoto.com/id/1182434606/photo/reflections-of-sunset-with-cloudscape-in-lake-water.jpg?s=612x612&w=0&k=20&c=82Y10VMTzKG2e6IZ1amcuQjgeEAhTeKqvzCpGgsytFo="
    #     self.process()


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Sign up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Log in")


class CommentForm(FlaskForm):
    comment_text = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")
