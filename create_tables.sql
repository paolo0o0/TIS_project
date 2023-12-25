CREATE TABLE genre (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);

CREATE TABLE country (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);

CREATE TABLE movie (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, creation_year INTEGER);

CREATE TABLE genre_movie (genre_id INTEGER NOT NULL, movie_id INTEGER NOT NULL, FOREIGN KEY(genre_id) REFERENCES genre(id), FOREIGN KEY(movie_id) REFERENCES movie(id), PRIMARY KEY(genre_id, movie_id));

CREATE TABLE country_movie (country_id INTEGER NOT NULL, movie_id INTEGER NOT NULL, FOREIGN KEY(country_id) REFERENCES country(id), FOREIGN KEY(movie_id) REFERENCES movie(id), PRIMARY KEY(country_id, movie_id));

CREATE TABLE person (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, birth_date DATE);

CREATE TABLE person_country (person_id INTEGER NOT NULL, country_id INTEGER NOT NULL, FOREIGN KEY(country_id) REFERENCES country(id), FOREIGN KEY(person_id) REFERENCES person(id), PRIMARY KEY(person_id, country_id));

CREATE TABLE role (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL);

CREATE TABLE death (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, date DATE NOT NULL, person_id INTEGER, FOREIGN KEY(person_id) REFERENCES person(id));

CREATE TABLE person_role_movie (role_id INTEGER NOT NULL, person_id INTEGER NOT NULL, movie_id INTEGER NOT NULL, FOREIGN KEY(role_id) REFERENCES role(id), FOREIGN KEY(person_id) REFERENCES person(id), FOREIGN KEY(movie_id) REFERENCES movie(id), PRIMARY KEY(role_id, person_id, movie_id));

