from app.core.db import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import INET

class Network(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(INET, nullable=False)
    create_at = db.Column(db.DateTime(timezone=True), default=datetime.utcnow())

    def __repr__(self) -> str:
        return f'IP: {self.IP}'