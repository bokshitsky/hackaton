import frontik.handler

from app.handler import HackatonPage


class Page(HackatonPage):
    def get_page(self):
        self.set_template('save_results.html')

        professions = sorted(self.storage.get_professions(), key=lambda p: p.profession_name)
        self.json.put({
            'professions': professions
        })

        # # для тестирвоания
        # self.application.snapshot.increment_counters(1, 0, 1)
        # self.application.snapshot.increment_counters(1, 1, 1)

    def post_page(self):
        is_success = self.get_argument('result') == 'success'

        if is_success:
            self.storage

        else:
            pass
