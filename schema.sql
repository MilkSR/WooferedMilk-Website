drop table if exists users;
create table users (
  id INTEGER primary key autoincrement,
  name TEXT not null,
  status TEXT,
  twitch-title TEXT,
  twitch-game TEXT,
  emote-method TEXT,
  dogfacts INTEGER not null,
  dogs INTEGER not null,
  multi INTEGER not null,
  novelty INTEGER not null,
  quote INTEGER not null,
  speedrun INTEGER not null,
  utility INTEGER not null,
  youtube INTEGER not null,
  faq INTEGER not null,
  highlights TEXT,
  ignore TEXT,
  mods TEXT,
  nick TEXT,
  trigger TEXT not null
);
create table commands (
  id INTEGER primary key autoincrement,
  command-name TEXT not null,
  command-response TEXT not null,
  channel-id Foreign Key INTEGER
);
create table personal-commands (
  id INTEGER primary key autoincrement,
  command-name TEXT not null,
  command-response TEXT not null,
  user-id Foreign Key INTEGER
);
create table emote-list (
  id INTEGER primary key autoincrement,
  emote-name TEXT not null,
  emote-use INTEGER not null,
  channel-id Foreign Key INTEGER
);
create table quotes (
  id INTEGER primary key autoincrement,
  quote TEXT not null,
  channel-id Foreign Key INTEGER
);
create table faqs (
  id INTEGER primary key autoincrement,
  game TEXT not null,
  link TEXT not null,
  channel-id Foreign Key INTEGER
);