import random

from app.handler import HackatonPage

from app.utils import update_url

from app.model.attrdict import AttrDict


class Page(HackatonPage):
    def get_page(self):
        self.set_template('stage.html')

        used_question_answers_ids = [int(qa) for qa in self.get_arguments('qa')]

        next_question = self.get_next_question(used_question_answers_ids)
        next_question_answers = self.get_storage().get_question_answers(next_question.question_id)

        self.json.put({
            'question': {'text': next_question.question_text},
            'answers': [{'qa_id': nqa.question_answer_id, 'text': nqa.answer_text} for nqa in next_question_answers]
        })

        # professions_snapshot = storage.get_professions_snapshot()
        # for profession in professions_snapshot:
        #     for used_question_answer in used_question_answers_ids:
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

    def get_next_question(self, used_question_answers_ids):
        remaining_questions = self.get_remaining_questions_ids(used_question_answers_ids)
        next_question_id = random.sample(remaining_questions, 1)[0]
        return self.get_storage().get_question(next_question_id)

    def post_page(self):
        last_selected_question_answer = self.get_argument('current')
        used_question_answers_ids = [int(qa) for qa in (self.get_arguments('qa') + [last_selected_question_answer])]

        storage = self.get_storage()

        professions = random.shuffle(storage.get_professions())
        # initial_probability = 1 / len(professions)
        for profession in professions:
            profession.probability = 1 # initial_probability
            for question_answer in used_question_answers_ids:
                total_requests = storage.get_question_answer_total_requests(profession.profession_id, question_answer) + 1 # +1 нужен для корректной обработки отсутствующих данных
                successfull_requests = storage.get_question_answer_successful_requests(profession.profession_id, question_answer) + 1
                profession.probability = profession.probability * successfull_requests / total_requests

        professions.sort(key=lambda p: p.probability, reverse=True)
        total_weight = sum(p.probability for p in professions)
        for profession in professions:
            profession.probability = profession.probability / total_weight

        remaining_questions = self.get_remaining_questions_ids(used_question_answers_ids)
        if not remaining_questions or professions[0].probability > 0.8:
            return self.redirect_to_finish(professions[0].profession_id, last_selected_question_answer, used_question_answers_ids)

        self.redirect_to_next_stage(used_question_answers_ids)

    def get_remaining_questions_ids(self, used_question_answers_ids):
        storage = self.get_storage()

        used_questions = set(
            storage.get_question_by_question_answer(qa_id).question_id for qa_id in used_question_answers_ids
        )
        all_questions_ids = set(storage.get_all_question_ids())
        remaining_questions = all_questions_ids.difference(used_questions)
        return remaining_questions

    def redirect_to_finish(self, profession_id, last_question_answer_id, used_question_answers):
        next_stage_url = update_url('/finish', {
            'qa': used_question_answers,
            'lqa': last_question_answer_id,
            'p': profession_id
        })
        self.redirect(next_stage_url)

    def redirect_to_next_stage(self, used_question_answers):
        next_stage_url = update_url('/stage', {'qa': used_question_answers})
        self.redirect(next_stage_url)
