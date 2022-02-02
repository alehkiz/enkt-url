from app.core.db import db
from flask_security import UserMixin, RoleMixin
import datetime

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True, nullable=False)
    email = db.Column(db.String(256), unique=True, nullable=False)
    _password = db.Column(db.String(512), nullable=False)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow())
    active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    created_network_id = db.Column(db.Integer, db.ForeignKey('network.id'), nullable=False)
    last_login_at = db.Column(db.DateTime, default=datetime.utcnow())
    last_login_network_id = db.Column(db.Integer, db.ForeignKey('network.id'))
    current_login_at = db.Column(db.DateTime, nullable=True)
    current_login_network_id = db.Column(db.Integer, db.ForeignKey('network.id'))
    confirmed_network_id = db.Column(db.Integer, db.ForeignKey('network.id'))
    confirmed_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    login_count = db.Column(db.Integer, nullable=True, default=0)




class Role(RoleMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    level = db.Column(db.Integer, unique=False, nullable=False)
    name = db.Column(db.String(128), nullable=False, unique=True)
    description = db.Column(db.String(255), nullable=True)
