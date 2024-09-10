from flask import render_template, redirect, url_for, request, Blueprint, flash
from app import db
import app
from app.models import RecipeTable
from app.forms import RecipeForm, DeleteForm
import requests
import os

main = Blueprint('main', __name__)

@main.route('/')
def index():
    recipes = RecipeTable.query.all()
    delete_form = DeleteForm()
    return render_template('index.html', recipes=recipes, delete_form=delete_form)

@main.route('/add-recipe', methods=['GET', 'POST'])
def add_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        name = form.name.data
        instructions = form.instructions.data
        ingredients_list = form.ingredients_list.data 

        # Remove empty entires
        ingredients_list = [ingredient.strip() for ingredient in ingredients_list.split('|') if ingredient.strip()]

        if not ingredients_list:
            flash('You must add at least one ingredient.', 'danger')
            return render_template('add-recipe.html', form=form)

        # app.logger.info(f'Form Data: Name={name}, Instructions={instructions}, Ingredients={ingredients_list}')

        try:
            new_recipe = RecipeTable(
                name=name,
                ingredients='|'.join(ingredients_list),
                instructions=instructions
            )
            db.session.add(new_recipe)
            db.session.commit()
            flash('Recipe added successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            app.logger.error(f'Error: {e}')
            flash('An error occurred. Please try again.', 'danger')

        return redirect(url_for('main.index'))
    else:
        print('Validation failed')
        print(form.errors)
        
    return render_template('add-recipe.html', form=form)


@main.route('/delete-recipe/<int:recipe_id>', methods=['POST'])
def delete_recipe(recipe_id):
    recipe = RecipeTable.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('main.index'))


@main.route('/recipe/<int:recipe_id>', methods=['GET'])
def view_recipe(recipe_id):
    recipe = RecipeTable.query.get_or_404(recipe_id)
    image_url = get_image_url(recipe.name)
    return render_template('view_recipe.html', recipe=recipe, image_url=image_url)

import requests
import os

def get_image_url(query):
    api_url = "https://api.pexels.com/v1/search"
    headers = {
        "Authorization": os.getenv('PEXELS_API_KEY')
    }
    params = {
        "query": query,
        "orientation": "landscape",
        "per_page": 1
    }
    response = requests.get(api_url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        if 'photos' in data and len(data['photos']) > 0:
            image_url = data['photos'][0]['src']['medium']
            return image_url
        else:
            return "https://via.placeholder.com/600x400?text=No+Image+Available"
    else:
        return "https://via.placeholder.com/600x400?text=No+Image+Available"
