import random

import tornado
from functools import reduce

import frontik.handler

from app.handler import HackatonPage

from app.utils import update_url


class Page(HackatonPage):
    def get_page(self):
        self.set_template('stage.html')

        used_question_answers = [int(qa) for qa in self.get_arguments('qa')]

        remaining_questions = self.get_remaining_questions_ids(used_question_answers)
        next_question_id = random.sample(remaining_questions, 1)[0]
        next_question_text = self.get_questions()[next_question_id]

        next_question_answers = self.get_question_to_answers_map()[next_question_id]

        self.json.put({
            'question': {'text': next_question_text},
            'answers': [{'qa_id': qa_id, 'id': id, 'text': text} for qa_id, id, text in next_question_answers]
        })

        # professions_snapshot = storage.get_professions_snapshot()
        # for profession in professions_snapshot:
        #     for used_question_answer in used_question_answers:
        #         ratio = storage.get_profession_history(profession, used_question_answer)
        #         profession.current_probability = profession.current_probability * ratio
        #
        # professions_sorted = sorted(professions_snapshot,
        #                             key=lambda profession: profession.current_probability, reversed=True)
        #
        # total_weight = sum(p.current_probability for p in professions_sorted)
        # professions_sorted_weightned = [p.current_probability / total_weight for p in professions_sorted]
        #
        # if professions_sorted_weightned[0].current_probability > 0.9:
        #     return self.redirect_to_finish()
        # self.redirect_to_next_stage()

    def get_remaining_questions_ids(self, used_question_answers):
        question_answer_to_question_map = self.get_question_answer_to_question_map()
        used_questions = set(
            question_answer_to_question_map[question_answer_id] for question_answer_id in used_question_answers)
        all_questions_ids = set(self.get_questions().keys())
        remaining_questions = all_questions_ids.difference(used_questions)
        return remaining_questions

    def post_page(self):
        self.redirect_to_next_stage()

    def redirect_to_next_stage(self):
        next_stage_url = update_url('/stage', {'qa': self.get_arguments('qa') + self.get_arguments('current')})
        self.redirect(next_stage_url)
