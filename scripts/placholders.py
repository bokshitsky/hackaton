from fill_professions import professions
from fill_questions import questions_common


for p in professions:
    for q in questions_common:
        print ("insert_profession_answers('{}', '{}', [('Да', 5), ('Нет', 95)], session)".format(p, q))
