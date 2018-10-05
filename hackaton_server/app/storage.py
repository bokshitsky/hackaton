from app.model.tables import Profession, Answer, Question, QuestionAnswer, RequestAnswer, Request


class storage(object):

    def __init__(self):
        sessions = {}



class DbSnapshot(object):

    def __init__(self, session):
        self.professions = {profession.id: profession.name for profession in session.query(Profession)}
        self.answer = {answer.id: answer.text for answer in session.query(Answer)}
        self.question = {question.id: question.text for question in session.query(Question)}

        self.session = session
        self.question_answer = {question_answer.question_id: (answer.text, question_answer.id)
                                for question_answer, answer in session.query(QuestionAnswer, Answer).join(Answer)}


    def increment_request_answer_count(self, profession_id, question_answer_id):
        request_answer = self.session.query(RequestAnswer).filter_by(profession_id=profession_id, question_answer_id=question_answer_id).first()
        if request_answer is None:
            request_answer = RequestAnswer(profession_id=profession_id, question_answer_id=question_answer_id, count = 1)
        else:
            request_answer.count = request_answer.count + 1
        self.session.add(request_answer)

    def increment_request_count(self, profession_id, question_answer):
        request = self.session.query(Request).filter_by(profession_id=profession_id, question_id=question_answer.question_id).first()
        if request is None:
            request = Request(profession_id=profession_id, question_id=question_answer.question_id, count=1)
        else:
            request.count = request.count + 1
        self.session.add(request)

    #
    # real_profession_id - настоящая профессия пользователя
    # proposed_profession_id - профессия, которую предположил наш алгоритм
    #
    def increment_counters(self, real_profession_id, proposed_profession_id, question_answer_id):
        question_answer = self.session.query(QuestionAnswer).get(question_answer_id)

        self.increment_request_count(proposed_profession_id, question_answer)

        # инкрементим только, если угадали
        if real_profession_id == proposed_profession_id:
            self.increment_request_answer_count(proposed_profession_id, question_answer_id)
        else:
            # если не угадали, сохраняем еще правильные ответы для профессии, которую указал пользователь, чтобы обучаться
            self.increment_request_count(real_profession_id, question_answer)
            self.increment_request_answer_count(real_profession_id, question_answer_id)

        self.session.commit()


