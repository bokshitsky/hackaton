import frontik


class HackatonPage(frontik.handler.PageHandler):

    def get_questions(self):
        return self.application.snapshot.question

    def get_answers(self):
        return self.application.snapshot.answer

    def get_professions(self):
        return self.application.snapshot.profession

    def get_question_answer_to_question_map(self):
        return self.application.snapshot.question_answer_to_question_map

    def get_question_to_question_answer_map(self):
        return self.application.snapshot.question_to_question_answer_map

    def get_question_to_answers_map(self):
        return self.application.snapshot.question_to_answers