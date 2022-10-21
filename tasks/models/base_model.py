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
    def get_by_uploaded(cls):
        return cls.query.filter_by(status=TaskStatus.UPLOADED.value).all()

    @classmethod
    def limit_get_all(cls, max: int, order: int):
        return cls.query.limit(max).all()
