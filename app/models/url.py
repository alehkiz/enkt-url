from app.core.db import  db
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property

class URL(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    url = db.Column(db.Text(), nullable=False, unique=False)
    _url_short = db.Column(db.String(32), nullable=False, unique=True)
    # _url_custom = db.Column(db.String(64), nullable=True, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_on = db.Column(db.Boolean)
    url_network_id = db.Column(db.Integer, db.ForeignKey('network.id'), nullable=False)

    def __repr__(self) -> str:
        return f'URL(id:{self.id}, short:{self._url_short}'
    
    @hybrid_property
    def url_short(self):
        return self._url_short

    @url_short.setter
    def url_short(self, url_short):
        q_url = URL.query.filter(URL.url_short == url_short).first()
        if not q_url is None:
            raise Exception('url_short já cadastrada')
        self._url_short = url_short
        

    
class Custom_URL(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    _custom = db.Column(db.String(100), nullable=False, unique=True)
    url_id = db.Column(db.Integer, db.ForeignKey('url.id'), nullable= False)

    def __repr__(self) -> str:
        return f'Custom_URL: {self._custom}'
    
    @hybrid_property
    def custom(self):
        return self._custom

    @custom
    def custom(self, custom):
        q_custom = Custom_URL.question.query(Custom_URL.custom == custom).first()
        if not q_custom is None:
            raise Exception('Custom já cadastrada')
        self._custom = custom


