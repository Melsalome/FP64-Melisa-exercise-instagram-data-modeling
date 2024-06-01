import os
import sys
from sqlalchemy import TEXT, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250))

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    user_to_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    user_from = relationship(User)
    user_to = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    caption = Column(TEXT)
    user_id = Column(Integer, ForeignKey(User.id))
    user = relationship(User)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(enumerate)
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey(Post.id))
    post = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(TEXT)
    author_id = Column(Integer, ForeignKey(User.id))
    author = relationship(User)
    post_id = Column(Integer, ForeignKey(Post.id))
    post = relationship(Post)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
