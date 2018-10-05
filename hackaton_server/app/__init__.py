# coding=utf-8
import tornado

from frontik.app import FrontikApplication

import sqlalchemy
from frontik.routing import FileMappingRouter

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from hackaton_server.app import pages


class HackApplication(FrontikApplication):
    def __init__(self, **settings):

        new_settings = settings
        new_settings.update({'tornado_settings': {'static_path': 'app/static'}})

        super(HackApplication, self).__init__(**new_settings)
        engine = create_engine('sqlite:///db.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def application_urls(self):
        return [
            ('/static/(.*)', tornado.web.StaticFileHandler),
            ('', FileMappingRouter(pages)),
        ]
