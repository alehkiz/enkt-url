from app.core.db import  db
from datetime import datetime

class URL(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    _url = db.Column(db.Text(), nullable=False, unique=True)
    _url_short = db.Column(db.String(32), nullable=False, unique=True)
    _url_custom = db.Column(db.String(64), nullable=True, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_on = db.Column(db.Boolean)
    url_network_id = db.Column(db.Integer, db.ForeignKey('network.id'), nullable=False)

    def __repr__(self) -> str:
        return f'URL(id:{self.id}, short:{self._url_short}'
    