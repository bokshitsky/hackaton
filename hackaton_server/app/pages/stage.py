import math
import random

from app.handler import HackatonPage
from app.utils import update_url


class Page(HackatonPage):
    def get_page(self):
        self.set_template('stage.html')
        next_question_id = int(self.get_argument('nq'))
        next_question = self.storage.get_question(next_question_id)
        next_question_answers = self.storage.get_question_answers(next_question_id)
        self.json.put({
            'question': {'text': next_question.question_text},
            'answers': [{'qa_id': nqa.question_answer_id, 'text': nqa.answer_text} for nqa in next_question_answers]
        })

    def post_page(self):
        last_selected_question_answer = self.get_argument('current', None)
        if last_selected_question_answer:
            used_question_answers_ids = [int(qa) for qa in (self.get_arguments('qa') + [last_selected_question_answer])]
        else:
            used_question_answers_ids = []

        professions = self.calculate_professions_probabilities(used_question_answers_ids)
        remaining_question_ids = self.get_remaining_questions_ids(used_question_answers_ids)
        top_profession = professions[0]
        if not remaining_question_ids or top_profession.probability > 0.8:
            return self.redirect_to_finish(top_profession.profession_id,
                                           last_selected_question_answer,
                                           used_question_answers_ids)

        next_question = self.get_next_question(professions, remaining_question_ids)
        self.redirect_to_next_stage(next_question, used_question_answers_ids)

    def get_next_question(self, professions, remaining_question_ids):
        remaining_questions = [self.storage.get_question(question_id) for question_id in remaining_question_ids]
        for question in remaining_questions:
            question.entropy = 0
            question_answers = self.storage.get_question_answers(question.question_id)

            for answer in question_answers:
                answer.probability = 0
                answer.probability_by_profession = {}
                for profession in professions:
                    question_answer_id = answer.question_answer_id

                    total_requests = self.get_total_requests(profession, question_answer_id)
                    successfull_requests = self.get_successful_requests(profession, question_answer_id)
                    answer_probability_for_profession = successfull_requests / total_requests
                    answer.probability += profession.probability * answer_probability_for_profession
                    answer.probability_by_profession[profession.profession_id] = answer_probability_for_profession

                professions_snapshot = [p.get_copy() for p in professions]
                for profession in professions_snapshot:
                    answer_probability_for_profession = answer.probability_by_profession[profession.profession_id]
                    profession.probability = profession.probability * answer_probability_for_profession
                self.rescale_professions_weight(professions_snapshot)

                professions_entropy = sum(profession.probability * (-math.log(profession.probability)) for profession in
                                          professions_snapshot)

                question.entropy += professions_entropy * answer.probability

        return min(remaining_questions, key=lambda question: question.entropy)

    def get_remaining_questions_ids(self, used_question_answers_ids):
        used_questions = set(
            self.storage.get_question_by_question_answer(qa_id).question_id for qa_id in used_question_answers_ids
        )
        all_questions_ids = set(self.storage.get_all_question_ids())
        remaining_questions = all_questions_ids.difference(used_questions)
        return remaining_questions

    def calculate_professions_probabilities(self, used_question_answers_ids):
        professions = self.storage.get_professions()
        random.shuffle(professions)

        for profession in professions:
            profession.probability = 1  # initial_probability
            for question_answer_id in used_question_answers_ids:
                # +2 и +1 нужны для корректной обработки отсутствующих данных
                total_requests = self.get_total_requests(profession, question_answer_id)
                successfull_requests = self.get_successful_requests(profession, question_answer_id)
                profession.probability = profession.probability * successfull_requests / total_requests

        self.rescale_professions_weight(professions)
        professions.sort(key=lambda p: p.probability, reverse=True)
        return professions

    def get_successful_requests(self, profession, question_answer):
        return self.storage.get_question_answer_successful_requests(profession.profession_id,
                                                                    question_answer) + 1

    def get_total_requests(self, profession, question_answer):
        return self.storage.get_question_answer_total_requests(profession.profession_id,
                                                               question_answer) + 2

    def rescale_professions_weight(self, professions):
        total_weight = sum(p.probability for p in professions)
        for profession in professions:
            profession.probability = profession.probability / total_weight

    def redirect_to_finish(self, profession_id, last_question_answer_id, used_question_answers):
        finish_url = update_url('/finish', {
            'qa': used_question_answers,
            'lqa': last_question_answer_id,
            'p': profession_id
        })
        self.redirect(finish_url)

    def redirect_to_next_stage(self, next_question, used_question_answers_ids):
        next_stage_url = update_url('/stage', {'qa': used_question_answers_ids, 'nq': next_question.question_id})
        self.redirect(next_stage_url)
