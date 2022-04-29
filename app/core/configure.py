from flask import Flask
from flask.cli import with_appcontext
from app.core.extensions import security, migrate, csrf, login
from app.core.db import user_datastore, db
from app.blueprints import register_blueprints
from app.models.security import User, Role
from app.models.url import URL, Custom_URL
from app.models.network import Network


login.login_view = 'auth.login'
login.login_message = 'Faça login para acessar a página'
login.login_message_category = 'danger'

def init(app:Flask):
    security.init_app(app, datastore=user_datastore, register_blueprint=False)
    db.init_app(app)
    migrate.init_app(app)
    csrf.init_app(app)
    login.init_app(app)
    login.session_protection = 'strong'
    register_blueprints(app)

    @login.user_loader
    def load_user(id):
        try:
            user = User.query.get(int(id))
        except Exception as e:
            db.session.rollback()
            app.logger.error(app.config.get('_ERRORS').get('DB_COMMIT_ERROR'))
            app.logger.error(e)
            return None
        return user

    
    @app.shell_context_processor
    @with_appcontext
    def make_shell_context():
        app.config['SERVER_NAME'] = 'localhost'
        ctx = app.test_request_context()
        ctx.push()
        return dict(db=db, User=User, Role=Role, URL=URL, Custom_URL=Custom_URL, Network=Network)