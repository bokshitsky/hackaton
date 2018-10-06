from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import Profession

from tables import Question, Request, Answer, QuestionAnswer, RequestAnswer

professions = [
    'Повар',
    'Клоун',
    'Учитель',
    'Сварщик',
    'Альпинист',
    'Сисадмин',
    'Продавец',
    'Формашлеп',
    'Юрист',
    'Уборщик',
    'Архитектор',
    'Строитель',
    'Менеджер по продажам',
    'HR',
    'Бэкенд разработчик',
    'Дизайнер',
    'Тестировщик',
    'Data scientist',
]


def insert_profession(name, session):
    if session.query(Profession).filter_by(name=name).first() is None:
        request = Profession(name=name)
        session.add(request)
        session.commit()


def get_profession(name, session):
    return session.query(Profession).filter_by(name=name).first()


def get_question(text, session):
    return session.query(Question).filter_by(text=text).first()


def get_answer(text, session):
    return session.query(Answer).filter_by(text=text).first()


def get_question_answer(question_id, answer_id, session):
    return session.query(QuestionAnswer).filter_by(question_id=question_id, answer_id=answer_id).first()


def set_profession_question_request(proff_id, question_id, session, total_requests):
    request = session.query(Request).filter_by(profession_id=proff_id, question_id=question_id).first()
    if request is None:
        request = Request(profession_id=proff_id, question_id=question_id, count=total_requests)
    else:
        request.count = total_requests
    session.add(request)
    session.commit()
    return request


def set_profession_question_request_answer_request(proff_id, question_answer_id, count, session):
    request_answer = session.query(RequestAnswer).filter_by(profession_id=proff_id,
                                                            question_answer_id=question_answer_id).first()
    if request_answer is None:
        request_answer = RequestAnswer(profession_id=proff_id, question_answer_id=question_answer_id, count=count)
    else:
        request_answer.count = count
    session.add(request_answer)
    session.commit()
    return request_answer


def insert_profession_answers(name, question_text, answers_map, session):
    proff_id = get_profession(name, session).id
    question_id = get_question(question_text, session).id
    total_requests = sum(count for answer, count in answers_map)

    set_profession_question_request(proff_id, question_id, session, total_requests)
    for answer_text, count in answers_map:
        answer = get_answer(answer_text, session)
        qa = get_question_answer(question_id, answer.id, session)
        set_profession_question_request_answer_request(proff_id, qa.id, count, session)


def main():
    engine = create_engine('sqlite:///../db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    for p in professions:
        insert_profession(p, session)

    insert_profession_answers('Повар', 'Вы работаете в офисе?', [('Да', 5), ('Нет', 95)], session)



if __name__ == '__main__':
    main()
