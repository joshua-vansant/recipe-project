from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from wtforms import HiddenField

class RecipeForm(FlaskForm):
    name = StringField('Recipe Name', validators=[DataRequired()])
    # ingredients = TextAreaField('Ingredients', validators=[DataRequired()])
    instructions = TextAreaField('Instructions', validators=[DataRequired()])
    submit = SubmitField('Save Recipe')
    ingredients_list = HiddenField('Ingredients List', validators=[DataRequired()])

    def validate_ingredients_list(self, field):
        if not field.data:
            raise ValidationError('Ingredients list cannot be empty.')

class DeleteForm(FlaskForm):
    csrf_token = HiddenField()