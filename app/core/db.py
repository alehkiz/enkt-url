from flask_sqlalchemy import SQLAlchemy
from flask_security import SQLAlchemySessionUserDatastore

db = SQLAlchemy(session_options={'autoflush': True})

from app.models.security import User, Role

user_datastore = SQLAlchemySessionUserDatastore(db, User, Role)

