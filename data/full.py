import datetime
import sqlalchemy
#from flask_sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin
from .db_session import SqlAlchemyBase


class Full(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'full'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    photo = sqlalchemy.Column(sqlalchemy.BLOB)

