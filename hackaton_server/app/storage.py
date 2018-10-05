from app.model.tables import Profession
from app.model.tables import Answer
from app.model.tables import Question


class storage(object):

    def __init__(self):
        sessions = {}



class DbSnapshot(object):

    def __init__(self, session):
        self.professions = {profession.id: profession.name for profession in session.query(Profession)}
        self.answer = {answer.id: answer.text for answer in session.query(Answer)}
        self.question = {question.id: question.text for question in session.query(Question)}



