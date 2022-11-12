import os

from flask import render_template, abort
from flask_login import current_user
from werkzeug.utils import secure_filename

from app import app
from forms import AddGoodsForm
from models import Good


@app.route('/add_good', methods=['GET', 'POST'])
def add_good():
    if not current_user.is_admin:
        abort(403)

    form = AddGoodsForm()

    if form.is_submitted():
        name = form.name.data
        description = form.description.data
        category = form.category.data
        manufacturer = form.manufacturer.data
        price = form.price.data
        photo = form.photo.data

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(
            app.instance_path, 'photos', filename
        ))

        Good.add(name, description, category, manufacturer, price, filename)

    return render_template("add_good.html", form=form, title="Добавить товар")

# TODO AJAX get category
