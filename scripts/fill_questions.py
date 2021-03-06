from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import Question, Answer, QuestionAnswer

questions_common = [
    'Вы работаете в офисе?',
    'У вас опасная профессия?',
    'Вы часто бываете в командировках?',
    'Вы любите готовить?',
    'Вы пользуетесь компьютером по работе?',
    'Вы перфекционист?',
    'Вы участвуете в хакатоне?',
    'Вы знаете много людей?',
    'Вы общительный?',
    'Вы работаете в цирке',
    'Вы рисуете?',
    'Вы считаете деньги?',
    'Придумываете что-то новое?',
    'Вы работаете с документами?',
    'Вы работаете в школе?',
]

common_answers = [
    'Да',
    'Нет',
    'Не совсем',
]


def insert_question(text, session):
    question = session.query(Question).filter_by(text=text).first()
    if question is None:
        question = Question(text=text)
        session.add(question)
        session.commit()
    return question


def insert_answer(text, session):
    answer = session.query(Answer).filter_by(text=text).first()
    if answer is None:
        answer = Answer(text=text)
        session.add(answer)
        session.commit()
    return answer


def insert_question_answer(question_id, answer_id, session):
    qa = session.query(QuestionAnswer).filter_by(question_id=question_id, answer_id=answer_id).first()
    if qa is None:
        qa = QuestionAnswer(question_id=question_id, answer_id=answer_id)
        session.add(qa)
        session.commit()
    return qa


def insert_question_with_answers(text, answers, session):
    q = insert_question(text, session)
    for answer in answers:
        a = insert_answer(answer, session)
        insert_question_answer(q.id, a.id, session)


def main():
    engine = create_engine('sqlite:///../db.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    for question in questions_common:
        q = insert_question(question, session)
        for answer in common_answers:
            a = insert_answer(answer, session)
            insert_question_answer(q.id, a.id, session)

    insert_custom(session)


def insert_custom(session):
    insert_question_with_answers('Какой язык предпочитаете?', ['java', 'python', 'perl', 'я русский'], session)
    insert_question_with_answers('Что вы продаете?', ['Продукт', 'Себя', 'Не знаю', 'Ничего'], session)
    insert_question_with_answers('Вы пишете фронтенд?', ['Да', 'К сожалению, да', 'Нет', 'Что это?'], session)

    insert_question_with_answers('Вы преподаёте?', ['Да', 'Нет'], session)
    insert_question_with_answers('Вы работаете с техникой?', ['Да', 'Нет'], session)



if __name__ == '__main__':
    main()
