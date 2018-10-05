from functools import reduce

import frontik.handler


class Page(frontik.handler.PageHandler):
    def get_page(self):
        used_question_answers = self.get_arguments("aq")

        professions_snapshot = storage.get_professions_snapshot()
        for profession in professions_snapshot:
            for used_question_answer in used_question_answers:
                ratio = storage.get_profession_history(profession, used_question_answer)
                profession.current_probability = profession.current_probability * ratio

        professions_sorted = sorted(professions_snapshot,
                                    key=lambda profession: profession.current_probability, reversed=True)

        total_weight = sum(p.current_probability for p in professions_sorted)
        professions_sorted_weightned = [p.current_probability / total_weight for p in professions_sorted]

        if professions_sorted_weightned[0].current_probability > 0.9:
            return self.redirect_to_finish()
        self.redirect_to_next_stage()



    def post_page(self):
        self.get_argument