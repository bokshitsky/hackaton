create table profession (
  id SERIAL,
  name STRING,
  primary key (id)
);

create table question (
  id SERIAL,
  text STRING,
  primary key (id)
);

create table answer (
  id SERIAL,
  text STIRNG,
  primary key (id)
);

CREATE TABLE question_answer (
  id SERIAL,
  answer_id integer,
  question_id integer,
  primary key (id),
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