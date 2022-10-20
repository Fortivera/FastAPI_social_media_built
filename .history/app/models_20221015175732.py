from email import contentmanager
from turtle import title
from typing import Counter
import sqlalchemy


from sqlalchemy import TIME, Column, Integer, String, Boolean
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base

# ___this is our SQLalchemy model___
# it defines the columns of postrgresql table, used for query, create, delete, update entries within the database


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class User(Base):
    __tablename__ = 'users'
    id
