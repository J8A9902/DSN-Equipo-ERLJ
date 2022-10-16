from sqlalchemy import Sequence

from models.base_model import BaseModel
from database import db

USER_ID_SEQ = Sequence('user_id_seq')

class Auth(BaseModel):
    id = db.Column(db.Integer, USER_ID_SEQ, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password
