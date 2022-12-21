from flask import redirect

from application import app


@app.route('/')
@app.route('/index')
def index():
    return redirect('goods')
