from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    signup_datetime = Column(DateTime)

class Forum(Base):
    __tablename__ = "forums"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class Thread(Base):
    __tablename__ = "threads"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    creator =



