import datetime
import sqlalchemy
#from flask_sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Mandel(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'mandel'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    photo = sqlalchemy.Column(sqlalchemy.BLOB)

