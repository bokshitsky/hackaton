import frontik.handler

from app.handler import HackatonPage


class Page(HackatonPage):
    def get_page(self):
        self.set_template('finish.html')
        profession = self.storage.get_profession(int(self.get_argument('p')))

        last_answer_text = self.storage.get_question_by_question_answer(int(self.get_argument('lqa'))).answer_text
        if last_answer_text.lower() == 'нет':
            final_text = profession.profession_name.lower() + 'a ответ'
        else:
            final_text = 'Я думаю, что вы ' + profession.profession_name.lower()

        self.json.put({
            'profession_name': profession.profession_name,
            'profession_id': profession.profession_id,
            'question_answer_ids': self.get_arguments('qa'),
            'final_text': final_text
        })
