# coding=utf-8

from frontik.app import FrontikApplication

class HackApplication(FrontikApplication):
    def __init__(self, **settings):
        super(HackApplication, self).__init__(**settings)
