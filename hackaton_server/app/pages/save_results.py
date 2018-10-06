import frontik.handler

from app.handler import HackatonPage

from app.utils import update_url


class Page(HackatonPage):
    def get_page(self):
        self.set_template('save_results.html')

        professions = sorted(self.storage.get_professions(), key=lambda p: p.profession_name)
        self.json.put({
            'professions': professions
        })

    def post_page(self):
        is_success = self.get_argument('result') == 'success'
        used_question_answers_ids = [int(qa) for qa in self.get_arguments('qa')]
        if is_success:
            profession_id = int(self.get_argument('p'))
            for qa in used_question_answers_ids:
                self.application.snapshot.increment_counters(profession_id, qa)
            return self.redirect('/start')

        choose_coorect_profession_url = update_url('/save_results', {'qa': used_question_answers_ids})
        self.redirect(choose_coorect_profession_url)
