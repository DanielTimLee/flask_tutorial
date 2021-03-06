import datetime

from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import TIMESTAMP, INTEGER

from app import db


class UserModel(db.Model):
    __tablename__ = 'users'
    __table_args__ = {
        'mysql_charset': 'utf8'
    }

    id = Column(
        INTEGER(20, unsigned=True),
        primary_key=True
    )
    username = Column(
        String(80),
        unique=True,
        nullable=False
    )
    password = Column(
        String(80),
        nullable=False
    )
    name = Column(
        String(80),
        nullable=False
    )
    nickname = Column(
        String(80),
        unique=True,
        nullable=False
    )
    email = Column(
        String(120),
        unique=True,
        nullable=False
    )
    created_date = Column(
        TIMESTAMP,
        default=datetime.datetime.utcnow()
    )
