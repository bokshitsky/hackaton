from fill_professions import professions
from fill_questions import questions_common

#
# for p in professions:
#     for q in questions_common:
#         print ("insert_profession_answers('{}', '{}', [('Да', 5), ('Нет', 90), ('Не совсем', 5)], session)".format(p, q))


for p in professions:
    print ("insert_profession_answers('{}', 'Какой язык предпочитаете?', [('java', 1), ('python', 1), ('perl', 1), ('я русский', 97)], session)".format(p))
    print ("insert_profession_answers('{}', 'Что вы продаете?', [('Продукт', 1), ('Себя', 20), ('Не знаю', 30), ('Ничего', 70)], session)".format(p))
    print ("insert_profession_answers('{}', 'Вы пишете фронтенд?', [('Да', 1), ('К сожалению, да', 1), ('Что это?', 100)], session)".format(p))
