drop table if exists users;
create table users (
  id INTEGER primary key autoincrement,
  name TEXT not null,
  status TEXT,
  commands TEXT,
  emotes TEXT,
  pcommands TEXT,
  dogfacts INTEGER not null,
  dogs INTEGER not null,
  multi INTEGER not null,
  quote INTEGER not null,
  speedrun INTEGER not null,
  utility INTEGER not null,
  youtube INTEGER not null,
  faq TEXT,
  highlights TEXT,
  ignore TEXT,
  mods TEXT,
  nick TEXT,
  quotes TEXT,
  trigger TEXT not null
);
