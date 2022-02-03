from flask import render_template, abort, g, current_app as app, Blueprint

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
@bp.route('/index/')
def main():
    return 'Olá mundo'