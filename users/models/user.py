from sqlalchemy import Sequence

from models.base_model import BaseModel
from database import db

USER_ID_SEQ = Sequence('user_id_seq')

class User(BaseModel):
    id = db.Column(db.Integer, USER_ID_SEQ, primary_key=True, autoincrement=True)
    username = db.Column(db.String, unique=True, nullable=False)
    

    def __init__(self, username: str):
        self.username = username
       