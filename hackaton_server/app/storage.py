from app.model.tables import Profession, Answer, Question, QuestionAnswer


class storage(object):

    def __init__(self):
        sessions = {}



class DbSnapshot(object):

    def __init__(self, session):
        self.professions = {profession.id: profession.name for profession in session.query(Profession)}
        self.answer = {answer.id: answer.text for answer in session.query(Answer)}
        self.question = {question.id: question.text for question in session.query(Question)}

        self.question_answer = {question_answer.question_id: (answer.text, question_answer.id)
                                for question_answer, answer in session.query(QuestionAnswer, Answer).join(Answer)}