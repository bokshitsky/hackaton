import frontik.handler

from app.handler import HackatonPage


class Page(HackatonPage):
    def get_page(self):
        self.set_template('finish.html')
        profession = self.storage.get_profession(int(self.get_argument('p')))

        self.json.put({
            'profession_name': profession.profession_name
        })
