# coding=utf-8

from frontik.app import FrontikApplication
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData


class HackApplication(FrontikApplication):
    def __init__(self, **settings):
        super(HackApplication, self).__init__(**settings)


    engine = create_engine('sqlite:///db.db')
