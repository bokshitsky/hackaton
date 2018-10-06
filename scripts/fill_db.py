from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from tables import Profession, Answer, Question, QuestionAnswer,RequestAnswer, Request

def main():
    engine = create_engine('sqlite:///../db.db')
    Session = sessionmaker(bind=engine)
    session = Session()


if __name__ == '__main__':
    main()
