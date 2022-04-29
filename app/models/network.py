from app.core.db import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import INET

class Network(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(INET, nullable=False)
    create_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow())
    created_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    created_user = db.relationship('User', backref='created_network', lazy='dynamic', foreign_keys='[User.created_network_id]')
    last_login_user = db.relationship('User', backref='last_login_network', lazy='dynamic', foreign_keys='[User.last_login_network_id]')
    current_login_user = db.relationship('User', backref='current_login_network', lazy='dynamic', foreign_keys='[User.current_login_network_id]')
    confirmed_user = db.relationship('User', backref='confirmed_network', lazy='dynamic', foreign_keys='[User.confirmed_network_id]')
    # def __repr__(self) -> str:
    #     return f'IP: {self.ip}'