import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum 
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from enum import Enum as PyEnum


Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
   
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), unique=True)

class Follower(Base):
    __tablename__ = 'Follower'
   
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer , ForeignKey('user.id'))
    user_to_id = Column(Integer , ForeignKey('user.id'))
    

class Comment(Base):
    __tablename__ = 'Comment'
    
    id = Column(Integer, primary_key=True)
    comment_text = Column(String (800))
    author_id = (Integer , ForeignKey('user.id'))
    post_id = (Integer , ForeignKey('user.id'))
    autor = relationship(User)


class Post(Base):
    __tablename__ = 'Post'
    
    id = Column(Integer, primary_key=True)
    user_id = (Integer , ForeignKey('user.id'))
    autor = relationship(User)


class MediaType (PyEnum):

    REEL = "reel"
    PICTURE = "picture" 
    STORY = "story"


class Media(Base):
    __tablename__ = 'Media'
    
    id = Column(Integer, primary_key=True)
    type = Column(Enum(MediaType))
    url = Column (String(200))
    post_id = (Integer , ForeignKey('user.id'))

    

try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
