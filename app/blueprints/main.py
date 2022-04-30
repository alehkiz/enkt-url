from flask import redirect, render_template, abort, g, current_app as app, Blueprint, request, url_for, flash
from app.forms.url import UrlForm
from app.models.network import Network
from app.models.url import URL, Custom_URL, generate_random_string
from app.core.db import db

from app.utils.kernel import validate_url, url_exist
from app.utils.db import commit
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
        db.session.add(ip)
        commit()
        g.ip_id = ip.id

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
                flash('URL inválida', category='danger')
                return redirect(url_for('main.index'))
            obj_url.is_on = True
            obj_url.url_network_id = ip.id
            obj_url.url_short = generate_random_string(app.config['_URL_SHORT_SIZE'])
            while obj_url.url_short is False:
                obj_url.url_short = generate_random_string(app.config['_URL_SHORT_SIZE'])
            db.session.add(obj_url)
            commit()
            flash('Url cadastrada com sucesso!', category='success')
            return render_template('index.html', status=True, url=obj_url.get_short_url())
        else:
            flash(f'URL: {form.url.data} inválida, com status code {url_exist(url.geturl()).status_code}', category='danger')
            return redirect(url_for('main.index'))

    return render_template('index.html', form=form)

@bp.route('/<short>')
def short(short):
    url = URL.query.filter(URL.url_short == short).first_or_404()
    if url.check_status_url() is False:
        flash(f'URL {url.url} não está mais ativa', category='danger')
        return abort(404)
    url.hits += 1
    commit()
    return redirect(url.url)


@bp.route('/list')
@bp.route('/list/<int:page>')
def list(page=1):
    pages = URL.query.order_by(URL.created_at.desc()).paginate(page, 10, False)
    return render_template('list.html', list=pages)


@bp.app_errorhandler(404)
def handler_error_404(err):
    return render_template('errors/404.html')

@bp.app_errorhandler(500)
def handler_error_500(err):
    return render_template('errors/500.html')