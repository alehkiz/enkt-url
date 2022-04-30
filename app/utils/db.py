from app.core.db import db
from flask import abort, current_app as app, flash


def commit():
    try:
        db.session.commit()
        return True
    except Exception as e:
        # flash('Ocorreu um erro ao salvar o banco de dados', category='danger')
        app.logger.error(e)
        db.session.rollback()
        return abort(500)
    # finally:
    #     db.session.close()
    