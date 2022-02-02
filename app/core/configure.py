from flask.cli import with_appcontext
from app.core.extensions import security, migrate, csrf, login
from app.core.db import user_datastore, db

login.login_view = 'auth.login'
login.login_message = 'Faça login para acessar a página'
login.login_message_category = 'danger'

def init(app):
    security.init_app(app, datastore=user_datastore, register_blueprint=False)
    db.init_app(app)
    csrf.init_app(app)
    login.init(app)
    login.session_protection = 'strong'

    