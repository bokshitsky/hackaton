insert into question (text) values ('Вы работаете в офисе?');
insert into question (text) values ('У Вас опасная профессия?');
insert into question (text) values ('Вы часто бываете в командировках?');

insert into question (text) values ('Вы любите готовить?');
insert into question (text) values ('Вы общительный человек?');
insert into question (text) values ('Как часто вы пользуетесь компьютером?');
insert into question (text) values ('Вы перфекционист?');
insert into question (text) values ('Что вы продаете?');
insert into question (text) values ('Вы все знаете?');
insert into question (text) values ('Вы любите копаться в ...');
insert into question (text) values ('Вы любите помогать людям?');
insert into question (text) values ('Как вы провели прошлые выходные?');
insert into question (text) values ('Что вы рисуете?');
insert into question (text) values ('Вы считаете деньги?');
insert into question (text) values ('Когда вы болеете ...');
insert into question (text) values ('Вы участвуете в хакатоне?');
insert into question (text) values ('Придумываете что-то новое?');
insert into question (text) values ('Что значит 99,9999 для вас?');
insert into question (text) values ('Поддерживаете все в идеальном состоянии?');
insert into question (text) values ('Вы всегда рады помочь?');
insert into question (text) values ('Вы знаете много людей?');
insert into question (text) values ('Без Вас никуда?');
insert into question (text) values ('Ваше любимое животное?');
insert into question (text) values ('Когда вы работаете?');
insert into question (text) values ('Какой язык вам ближе?');

insert into profession (name) values ('Повар');
insert into profession (name) values ('Программист');
insert into profession (name) values ('Клоун');
insert into profession (name) values ('Учитель');
insert into profession (name) values ('Сварщик');
insert into profession (name) values ('Альпинист');

insert into profession (name) values ('Сисадмин');
insert into profession (name) values ('Продавец');
insert into profession (name) values ('Формашлеп');
insert into profession (name) values ('Юрист');
insert into profession (name) values ('Уборщик');
insert into profession (name) values ('Архитектор');
insert into profession (name) values ('Менеджер');
insert into profession (name) values ('HR');
insert into profession (name) values ('Веб разработчик');
insert into profession (name) values ('Бэкенд разработчик');
insert into profession (name) values ('Дизайнер');
insert into profession (name) values ('Бэкенд разработчик');
insert into profession (name) values ('Гуру');
insert into profession (name) values ('Data scientist');

insert into answer(text) values ('Да');
insert into answer(text) values ('Нет');

insert into answer(text) values ('Раз в год');
insert into answer(text) values ('Каждый день');
insert into answer(text) values ('По выходным');
insert into answer(text) values ('Периодически');
insert into answer(text) values ('Что это?');
insert into answer(text) values ('Услуги');
insert into answer(text) values ('Старье всякое');
insert into answer(text) values ('Вкусненькое');
insert into answer(text) values ('Ничего');
insert into answer(text) values ('Безусловно!');
insert into answer(text) values ('Все знать не возможно!');
insert into answer(text) values ('Не все, но многое');
insert into answer(text) values ('коде');
insert into answer(text) values ('данных');
insert into answer(text) values ('песке');
insert into answer(text) values ('голове');
insert into answer(text) values ('нигде');
insert into answer(text) values ('гулял');
insert into answer(text) values ('кодил');
insert into answer(text) values ('отдыхал');
insert into answer(text) values ('отлично!');
insert into answer(text) values ('не скажу');
insert into answer(text) values ('картины');
insert into answer(text) values ('схемы');
insert into answer(text) values ('интерфейс');
insert into answer(text) values ('я не умею :(');
insert into answer(text) values ('я работаю');
insert into answer(text) values ('пью чай и ем мед');
insert into answer(text) values ('хожу на работу');
insert into answer(text) values ('плачууу');
insert into answer(text) values ('бонусы');
insert into answer(text) values ('очень большая скидка');
insert into answer(text) values ('цифры');
insert into answer(text) values ('несомненно!');
insert into answer(text) values ('агась');
insert into answer(text) values ('вы справитесь и без меня');
insert into answer(text) values ('питон');
insert into answer(text) values ('лиса');
insert into answer(text) values ('кошка');
insert into answer(text) values ('собака');
insert into answer(text) values ('енот');
insert into answer(text) values ('ночью');
insert into answer(text) values ('по выходным');
insert into answer(text) values ('всегда');
insert into answer(text) values ('как все');
insert into answer(text) values ('когда хочу');
insert into answer(text) values ('java');
insert into answer(text) values ('js');
insert into answer(text) values ('python');
insert into answer(text) values ('bash');
insert into answer(text) values ('русский');
insert into answer(text) values ('sql');
insert into answer(text) values ('язык жестов');


insert into question_answer(question_id, answer_id) values (1, 1);
insert into question_answer(question_id, answer_id) values (1, 2);
insert into question_answer(question_id, answer_id) values (2, 1);
insert into question_answer(question_id, answer_id) values (2, 2);
insert into question_answer(question_id, answer_id) values (3, 1);
insert into question_answer(question_id, answer_id) values (3, 2);

insert into question_answer(question_id, answer_id) values (4, 1);
insert into question_answer(question_id, answer_id) values (4, 2);
insert into question_answer(question_id, answer_id) values (5, 1);
insert into question_answer(question_id, answer_id) values (5, 2);
insert into question_answer(question_id, answer_id) values (6, 3);
insert into question_answer(question_id, answer_id) values (6, 4);
insert into question_answer(question_id, answer_id) values (6, 5);
insert into question_answer(question_id, answer_id) values (6, 6);
insert into question_answer(question_id, answer_id) values (7, 1);
insert into question_answer(question_id, answer_id) values (7, 2);
insert into question_answer(question_id, answer_id) values (7, 7);
insert into question_answer(question_id, answer_id) values (8, 9);
insert into question_answer(question_id, answer_id) values (8, 10);
insert into question_answer(question_id, answer_id) values (8, 8);
insert into question_answer(question_id, answer_id) values (8, 11);
insert into question_answer(question_id, answer_id) values (9, 12);
insert into question_answer(question_id, answer_id) values (9, 13);
insert into question_answer(question_id, answer_id) values (9, 14);
insert into question_answer(question_id, answer_id) values (10, 15);
insert into question_answer(question_id, answer_id) values (10, 16);
insert into question_answer(question_id, answer_id) values (10, 17);
insert into question_answer(question_id, answer_id) values (10, 18);
insert into question_answer(question_id, answer_id) values (10, 19);
insert into question_answer(question_id, answer_id) values (11, 1);
insert into question_answer(question_id, answer_id) values (11, 2);
insert into question_answer(question_id, answer_id) values (12, 20);
insert into question_answer(question_id, answer_id) values (12, 21);
insert into question_answer(question_id, answer_id) values (12, 22);
insert into question_answer(question_id, answer_id) values (12, 23);
insert into question_answer(question_id, answer_id) values (12, 24);
insert into question_answer(question_id, answer_id) values (13, 25);
insert into question_answer(question_id, answer_id) values (13, 26);
insert into question_answer(question_id, answer_id) values (13, 27);
insert into question_answer(question_id, answer_id) values (13, 28);
insert into question_answer(question_id, answer_id) values (14, 1);
insert into question_answer(question_id, answer_id) values (14, 2);
insert into question_answer(question_id, answer_id) values (15, 29);
insert into question_answer(question_id, answer_id) values (15, 30);
insert into question_answer(question_id, answer_id) values (15, 31);
insert into question_answer(question_id, answer_id) values (15, 32);
insert into question_answer(question_id, answer_id) values (16, 1);
insert into question_answer(question_id, answer_id) values (16, 2);
insert into question_answer(question_id, answer_id) values (17, 1);
insert into question_answer(question_id, answer_id) values (17, 2);
insert into question_answer(question_id, answer_id) values (18, 33);
insert into question_answer(question_id, answer_id) values (18, 34);
insert into question_answer(question_id, answer_id) values (18, 35);
insert into question_answer(question_id, answer_id) values (19, 1);
insert into question_answer(question_id, answer_id) values (19, 2);
insert into question_answer(question_id, answer_id) values (20, 1);
insert into question_answer(question_id, answer_id) values (20, 2);
insert into question_answer(question_id, answer_id) values (21, 1);
insert into question_answer(question_id, answer_id) values (21, 2);
insert into question_answer(question_id, answer_id) values (22, 36);
insert into question_answer(question_id, answer_id) values (22, 37);
insert into question_answer(question_id, answer_id) values (22, 38);
insert into question_answer(question_id, answer_id) values (23, 39);
insert into question_answer(question_id, answer_id) values (23, 40);
insert into question_answer(question_id, answer_id) values (23, 41);
insert into question_answer(question_id, answer_id) values (23, 42);
insert into question_answer(question_id, answer_id) values (23, 43);
insert into question_answer(question_id, answer_id) values (24, 44);
insert into question_answer(question_id, answer_id) values (24, 45);
insert into question_answer(question_id, answer_id) values (24, 46);
insert into question_answer(question_id, answer_id) values (24, 47);
insert into question_answer(question_id, answer_id) values (24, 48);
insert into question_answer(question_id, answer_id) values (25, 49);
insert into question_answer(question_id, answer_id) values (25, 50);
insert into question_answer(question_id, answer_id) values (25, 51);
insert into question_answer(question_id, answer_id) values (25, 52);
insert into question_answer(question_id, answer_id) values (25, 53);
insert into question_answer(question_id, answer_id) values (25, 54);
insert into question_answer(question_id, answer_id) values (25, 55);