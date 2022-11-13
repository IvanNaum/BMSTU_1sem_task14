import os

from flask import render_template, abort, redirect, url_for
from flask_login import current_user
from werkzeug.datastructures import MultiDict
from werkzeug.utils import secure_filename

from app import app, db
from forms import GoodsForm
from models import Good


@app.route('/goods')
def goods_view():
    goods = Good.query.all()
    return render_template('goods.html', goods=goods)


@app.route('/goods/<int:good_id>')
def good_view(good_id):
    good = Good.query.filter_by(id=good_id).first()
    print(good.photo)
    print(url_for('static', filename='photos/{}'.format(good.photo)))
    good.photo = f'photos/{good.photo}'

    return render_template('good.html', good=good, title=good.name)


@app.route('/goods/<int:good_id>/edit', methods=['GET', 'POST'])
def edit_good_view(good_id):
    if not current_user.is_admin:
        abort(403)

    good = Good.query.filter_by(id=good_id).first()
    form = GoodsForm()

    if form.is_submitted():
        good.name = form.name.data
        good.description = form.description.data
        good.category = form.category.data
        good.manufacturer = form.manufacturer.data
        good.price = form.price.data

        photo = form.photo.data
        if photo:
            filename = secure_filename(photo.filename)
            photo.save(os.path.join(
                app.config['UPLOAD_FOLDER'], 'photos', filename
            ))

            good.photo = filename

        db.session.commit()

        return redirect(url_for('good_view', good_id=good_id))

    data = {
        'name': good.name,
        'description': good.description,
        'category': good.category,
        'manufacturer': good.manufacturer,
        'price': good.price,
    }
    form = GoodsForm(formdata=MultiDict(data))

    return render_template('edit_good.html', form=form, title=f'Изменить товар {good.name}')


@app.route('/goods/<int:good_id>/delete')
def delete_good_view(good_id):
    if not current_user.is_admin:
        abort(403)

    good = Good.query.filter_by(id=good_id).first()
    db.session.delete(good)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/add_good', methods=['GET', 'POST'])
def add_good_view():
    if not current_user.is_admin:
        abort(403)

    form = GoodsForm()

    if form.is_submitted():
        name = form.name.data
        description = form.description.data
        category = form.category.data
        manufacturer = form.manufacturer.data
        price = form.price.data
        photo = form.photo.data

        filename = secure_filename(photo.filename)
        photo.save(os.path.join(
            app.config['UPLOAD_FOLDER'], 'photos', filename
        ))

        Good.add(name, description, category, manufacturer, price, filename)
        return redirect(url_for('index'))

    return render_template("add_good.html", form=form, title="Добавить товар")

# TODO AJAX get category
