from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Profession(Base):
    __tablename__ = 'profession'

    id = Column(Integer, primary_key=True)
    name = Column(String)


class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True)
    text = Column(String)


class Question(Base):
    __tablename__ = 'question'

    id = Column(Integer, primary_key=True)
    text = Column(String)


class QuestionAnswer(Base):
    __tablename__ = 'question_answer'

    id = Column(Integer, primary_key=True)
    answer_id = Column(Integer)
    question_id = Column(Integer)


class Request(Base):
    __tablename__ = 'request'

    profession_id = Column(Integer, primary_key=True)
    question_id = Column(Integer, primary_key=True)
    count = Column(Integer)


class RequestAnswer(Base):
    __tablename__ = 'request_answer'

    profession_id = Column(Integer, primary_key=True)
    question_answer_id = Column(Integer, primary_key=True)
    count = Column(Integer)