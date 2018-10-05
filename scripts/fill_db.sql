insert into question (text) values ('Вы работаете в офисе?');
insert into question (text) values ('У Вас опасная профессия?');
insert into question (text) values ('Вы часто бываете в командировках?');

insert into profession (name) values ('Повар');
insert into profession (name) values ('Программист');
insert into profession (name) values ('Клоун');
insert into profession (name) values ('Учитель');
insert into profession (name) values ('Сварщик');
insert into profession (name) values ('Альпинист');

insert into answer(text) values ('Да');
insert into answer(text) values ('Нет');

insert into question_answer(answer_id, question_id) values (1, 1);
insert into question_answer(answer_id, question_id) values (1, 2);
insert into question_answer(answer_id, question_id) values (2, 1);
insert into question_answer(answer_id, question_id) values (2, 2);
insert into question_answer(answer_id, question_id) values (3, 1);
insert into question_answer(answer_id, question_id) values (3, 2);