from flask import redirect, render_template, abort, g, current_app as app, Blueprint, request, url_for, flash
from app.forms.url import UrlForm
from app.models.network import Network
from app.models.url import URL, Custom_URL, generate_random_string
from app.core.db import db

from app.utils.kernel import validate_url, url_exist

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index/', methods=['GET', 'POST'])
def index():
    # status = request.args.get('status')
    _ip = request.access_route[0] or request.remote_addr
    ip = Network.query.filter(Network.ip == _ip).first()
    if ip is None:
        ip = Network()
        ip.ip = _ip
        # ip.created_user_id = 4
        db.session.add(ip)
        try:
            db.session.commit()
            g.ip_id = ip.id
        except Exception as e:
            print(e)
            db.session.rollback()
            #TODO add logger
            return abort(500)
    form = UrlForm()
    if form.validate_on_submit():
        url = validate_url(form.url.data)
        if url is False:
            flash(f'URL: {form.url.data} inválida', category='danger')
            return redirect(url_for('main.index'))
        if url_exist(url.geturl()).status_code == 200:
            obj_url = URL()
            obj_url.url = url.geturl()
            if obj_url.url is False:
                flash('Url já cadastrada', category='danger')
                return redirect(url_for('main.index'))
            obj_url.is_on = True
            obj_url.url_network_id = ip.id
            obj_url.url_short = generate_random_string(app.config['_URL_SHORT_SIZE'])
            while obj_url.url_short is False:
                obj_url.url_short = generate_random_string(app.config['_URL_SHORT_SIZE'])
            db.session.add(obj_url)
            db.session.commit()
            return render_template('index.html', status=True, url=obj_url.get_url())
        else:
            flash(f'URL: {form.url.data} inválida, com status code {url_exist(url.geturl()).status_code}', category='danger')
            return redirect(url_for('main.index'))

    return render_template('index.html', form=form)


@bp.route('/list/', methods=['GET'])
def list():
    return 'none'