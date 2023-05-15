CREATE DATABASE travel_app

CREATE TABLE destinations (
    id SERIAL PRIMARY KEY,
    type TEXT,
    image_url TEXT
);

CREATE TABLE travels(
    id SERIAL PRIMARY KEY,
    name TEXT,
    title TEXT,
    image_url TEXT,
    location TEXT,
    description TEXT
);


CREATE TABLE users(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  email TEXT,
  password_digest TEXT
);


CREATE TABLE likes(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  travel_id INTEGER
);

CREATE TABLE comments(
  id SERIAL PRIMARY KEY,
  user_id INTEGER,
  travel_id INTEGER,
  comments TEXT
);
