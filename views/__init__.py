from flask import Blueprint

import views.auth
import views.goods
import views.index

my_view = Blueprint('my_view', __name__)
