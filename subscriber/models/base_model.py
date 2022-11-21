from sqlalchemy import asc, desc
from database import db
from helpers.tasks_status_enum import TaskStatus

class BaseModel(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    @classmethod
    def get_by_id(cls, id: int):
        return cls.query.get_or_404(id)

    @classmethod
    def get_by_user_id(cls, user_id: int):
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def get_by_file_name(cls, file_name: str):
        return cls.query.filter_by(file_name=file_name).all()

    @classmethod
    def get_by_uploaded(cls):
        return cls.query.filter_by(status=TaskStatus.UPLOADED.value).all()

    @classmethod
    def limit_get_all(cls, user_id: int,  max: int, order: int):
        query = ''

        if(order == 0):
            query = cls.query.filter_by(user_id=user_id).order_by(asc(cls.id)).limit(max).all()
        else:
            query = cls.query.filter_by(user_id=user_id).order_by(desc(cls.id)).limit(max).all()
            
        return query
