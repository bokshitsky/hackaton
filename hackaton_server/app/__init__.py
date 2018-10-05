# coding=utf-8
import tornado

from frontik.app import FrontikApplication
import sqlalchemy
from frontik.routing import FileMappingRouter
from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

from hackaton_server.app import pages


class HackApplication(FrontikApplication):
    def __init__(self, **settings):
        super(HackApplication, self).__init__(**settings)


    engine = create_engine('sqlite:///db.db')

    def application_urls(self):
        return [
            ('/static/(.*)', tornado.web.StaticFileHandler, {'path': 'static'}),
            ('', FileMappingRouter(pages)),
        ]
