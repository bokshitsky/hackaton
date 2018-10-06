from typing import DefaultDict

from app.model.tables import Profession, Answer, Question, QuestionAnswer, RequestAnswer, Request

from app.model.attrdict import AttrDict


class storage(object):

    def __init__(self):
        sessions = {}


class DbSnapshot(object):

    def __init__(self, session):
        self.session = session

        self.professions = dict()
        for p in session.query(Profession):
            self.professions[p.id] = AttrDict(dict(profession_id=p.id,
                                                   profession_name=p.name))

        self.questions = dict()
        for q in session.query(Question):
            self.questions[q.id] = AttrDict(dict(question_id=q.id,
                                                 question_text=q.text))

        self.question_to_question_answer_map = DefaultDict(list)
        self.question_answer_to_question_map = dict()
        for qa, a, q in session.query(QuestionAnswer, Answer, Question).join(Answer, Question):
            self.question_to_question_answer_map[q.id].append(AttrDict(dict(question_id=q.id,
                                                                            answer_id=a.id,
                                                                            question_answer_id=qa.id,
                                                                            answer_text=a.text,
                                                                            question_text=q.text)))

            self.question_answer_to_question_map[qa.id] = AttrDict(dict(question_id=q.id,
                                                                        answer_id=a.id,
                                                                        question_answer_id=qa.id,
                                                                        answer_text=a.text,
                                                                        question_text=q.text))

        self.professions_questions = DefaultDict(lambda: DefaultDict(int))
        for r in self.session.query(Request):
            self.professions_questions[r.profession_id][r.question_id] = r.count

        self.professions_questions_answers = DefaultDict(lambda: DefaultDict(int))
        for ra in self.session.query(RequestAnswer):
            self.professions_questions_answers[ra.profession_id][ra.question_answer_id] = ra.count

    def get_question_by_question_answer(self, question_answer_id):
        return self.question_answer_to_question_map[question_answer_id]

    def get_question_answers(self, question_id):
        return [qa.get_copy() for qa in self.question_to_question_answer_map[question_id]]

    def get_question_answer_total_requests(self, profession_id, question_answer_id):
        question_id = self.question_answer_to_question_map[question_answer_id]
        return self.professions_questions[profession_id].get(question_id, 0)

    def get_question_answer_successful_requests(self, profession_id, question_answer_id):
        return self.professions_questions_answers[profession_id].get(question_answer_id, 0)

    def get_all_question_ids(self):
        return list(self.question_to_question_answer_map.keys())

    def get_question(self, question_id):
        return self.questions[question_id].get_copy()

    def get_profession(self, profession_id):
        return self.professions[profession_id].get_copy()

    def get_professions(self):
        return [p.get_copy() for p in self.professions.values()]

    def increment_request_answer_count(self, profession_id, question_answer_id):
        request_answer = self.session.query(RequestAnswer).filter_by(profession_id=profession_id,
                                                                     question_answer_id=question_answer_id).first()
        if request_answer is None:
            request_answer = RequestAnswer(profession_id=profession_id, question_answer_id=question_answer_id, count=1)
        else:
            request_answer.count = request_answer.count + 1
        self.session.add(request_answer)

    def increment_request_count(self, profession_id, question_answer):
        request = self.session.query(Request).filter_by(profession_id=profession_id,
                                                        question_id=question_answer.question_id).first()
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
            # если не угадали, сохраняем еще правильные ответы для профессии, которую указал пользователь,
            # чтобы обучаться
            self.increment_request_count(real_profession_id, question_answer)
            self.increment_request_answer_count(real_profession_id, question_answer_id)

        self.session.commit()
