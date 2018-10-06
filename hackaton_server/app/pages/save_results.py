import frontik.handler

from app.handler import HackatonPage


class Page(HackatonPage):
    def get_page(self):
        self.set_template('finish.html')
        profession = self.storage.get_profession(int(self.get_argument('p')))

        used_question_answers_ids = [int(qa) for qa in self.get_arguments('qa')]

        for qa in used_question_answers_ids:
            self.application.snapshot.increment_counters(qa, profession)
