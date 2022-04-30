from email.policy import default
from app.core.db import  db
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
import validators


from app.utils.kernel import url_exist
from app.utils.db import commit
from flask import current_app as app, request

from app.utils.kernel import generate_random_string

class URL(db.Model):
    __tablename__ = 'url'
    id = db.Column(db.Integer(), primary_key=True)
    _url = db.Column(db.Text(), nullable=False, unique=False)
    _url_short = db.Column(db.String(32), nullable=False, unique=True)
    # _url_custom = db.Column(db.String(64), nullable=True, unique=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)
    url_network_id = db.Column(db.Integer, db.ForeignKey('network.id'), nullable=False)
    hits = db.Column(db.Integer, default=0)
    custom_url = db.relationship('Custom_URL', cascade='all, delete-orphan',
                            single_parent=True, backref='page', lazy='dynamic', primaryjoin='URL.id == Custom_URL.url_id')
    

    def __repr__(self) -> str:
        return f'URL(id:{self.id}, short:{self._url_short})'

    def get_short_url(self)-> str:
        return request.url_root + self.url_short

    def check_status_url(self):
        url = url_exist(self.url)
        if url.status_code == 200:
            self.status = True
            status = True
        else:
            self.status = False
            status = False
        commit()
        return status

    @hybrid_property
    def url(self):
        return self._url

    @url.setter
    def url(self, url):
        if validators.url(url) is True:
            self._url = url
        else:
            self._url = None


    @hybrid_property
    def url_short(self):
        return self._url_short

    @url_short.setter
    def url_short(self, url_short):
        q_url = URL.query.filter(URL.url_short == url_short).first()
        if q_url != None:
            self._url_short = False
        else:
            self._url_short = url_short
        # while q_url != None:
        #     url_short = generate_random_string(app.config['_URL_SHORT_SIZE'])
        #     q_url = URL.query.filter(URL.url_short == url_short).first()
        # self._url_short = url_short

class Custom_URL(db.Model):
    __tablename__ = 'custom_url'
    id = db.Column(db.Integer(), primary_key=True)
    _custom = db.Column(db.String(100), nullable=False, unique=True)
    url_id = db.Column(db.Integer, db.ForeignKey('url.id'), nullable= False)
    # url = db.relationship('URL', back_populates="custom_url", lazy='dynamic')
    def __repr__(self) -> str:
        return f'Custom_URL: {self._custom}'
    
    @hybrid_property
    def custom(self):
        return self._custom

    @custom.setter
    def custom(self, custom):
        q_custom = Custom_URL.question.query(Custom_URL.custom == custom).first()
        if not q_custom is None:
            raise Exception('Custom já cadastrada')
        self._custom = custom
