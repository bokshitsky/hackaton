import frontik.handler
from app.handler import HackatonPage


class Page(HackatonPage):
    def get_page(self):
        self.set_template('start.html')
        self.json.put({
            'text': 'Hello, world!'
        })

    def post_page(self):
        self.redirect('/stage')
