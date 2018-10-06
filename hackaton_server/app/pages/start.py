import random

import frontik.handler
from app.handler import HackatonPage


class Page(HackatonPage):
    def get_page(self):
        voice_message = random.sample(['Начнем?', 'Давайте начнем', 'Начинай уже'], 1)[0]
        self.set_template('start.html')
        self.json.put({
            'voice_message': voice_message
        })

    def post_page(self):
        self.redirect('/stage')
