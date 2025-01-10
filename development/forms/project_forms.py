from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length

class ProjectForm:
    project_name = StringField('Project Name', validators=[
        DataRequired(),
        Length(min=3, max=100)
    ])
    project_description = TextAreaField('Project Description', validators=[
        DataRequired(),
        Length(min=10, max=500)
    ])

class TaskForm(FlaskForm):
    task_name = StringField('Task Name', validators=[
        DataRequired(),
        Length(min=3, max=100)
    ])
    task_description = TextAreaField('Task Description', validators=[
        DataRequired(),
        Length(min=10, max=500)
    ])
