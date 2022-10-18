from sqlalchemy import Sequence, Enum
from models.base_model import BaseModel
from database import db
from helpers.tasks_status_enum import TaskStatus

USER_ID_SEQ = Sequence('task_id_seq')

class Task(BaseModel):
    id = db.Column(db.Integer, USER_ID_SEQ, primary_key=True, autoincrement=True)
    file_name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    new_format = db.Column(db.String, nullable=False)
    time_stamp = db.Column(db.DateTime, default=db.func.now())
    status = db.Column(Enum(TaskStatus), default=TaskStatus.IN_PROGRESS)

    def __init__(self, file_name: str, user_id: int, new_format: str):
        self.file_name = file_name
        self.user_id = user_id
        self.new_format = new_format
        