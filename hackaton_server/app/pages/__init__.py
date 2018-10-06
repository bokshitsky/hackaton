from hackaton_server.app.handler import HackatonPage


class Page(HackatonPage):
    def get_page(self):
        self.redirect('/start')
