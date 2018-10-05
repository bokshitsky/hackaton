# coding=utf-8

from frontik.app import FrontikApplication
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class HackApplication(FrontikApplication):
    def __init__(self, **settings):
        super(HackApplication, self).__init__(**settings)

        engine = create_engine('sqlite:///db.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()
