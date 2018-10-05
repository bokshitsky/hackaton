create table profession (
  id integer primary key AUTOINCREMENT,
  name STRING
);

create table question (
  id integer primary key AUTOINCREMENT,
  text STRING
);

create table answer (
  id integer primary key AUTOINCREMENT,
  text STIRNG
);

CREATE TABLE question_answer (
  id integer primary key AUTOINCREMENT,
  answer_id integer,
  question_id integer,
  foreign key (answer_id) references answer(id),
  foreign key (question_id) references question(id)
);

create table request (
  profession_id integer,
  question_id integer,
  count integer,
  primary key (profession_id, question_id),
  foreign key (profession_id) references profession(id),
  foreign key (question_id) references question(id)
);

create table request_answer (
  profession_id integer,
  question_answer_id integer,
  count integer,
  primary key (profession_id, question_answer_id),
  foreign key (profession_id) references profession(id),
  foreign key (question_answer_id) references question_answer(id)
);