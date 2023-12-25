BEGIN TRANSACTION
INSERT INTO country (name) VALUES ('USA');

INSERT INTO country (name) VALUES ('Russia');

INSERT INTO country (name) VALUES ('Germany');

INSERT INTO country (name) VALUES ('Italy');

INSERT INTO country (name) VALUES ('Great Britain');

INSERT INTO genre (name) VALUES ('Drama');

INSERT INTO genre (name) VALUES ('Fantasy');

INSERT INTO genre (name) VALUES ('Horror');

INSERT INTO genre (name) VALUES ('Comedy');

INSERT INTO genre (name) VALUES ('Thriller');

INSERT INTO genre (name) VALUES ('Fantastic');

INSERT INTO movie (name, creation_year) VALUES ('The Shawshank Redemption', 1994);

INSERT INTO movie (name, creation_year) VALUES ('The Green Mile', 1999);

INSERT INTO movie (name, creation_year) VALUES ('Interstellar', 2014);

INSERT INTO movie (name, creation_year) VALUES ('Mai stati uniti', 2013);

INSERT INTO person (name, birth_date) VALUES ('Carlo Vanzina', '1951-03-13');

INSERT INTO person (name, birth_date) VALUES ('Ricky Memphis', '1968-08-29');

INSERT INTO person (name, birth_date) VALUES ('Tom Hanks', '1956-07-09');

INSERT INTO person (name, birth_date) VALUES ('Matthew McConaughey', '1969-11-04');

INSERT INTO person (name, birth_date) VALUES ('Jonathan Nolan', '1976-06-06');

INSERT INTO person (name, birth_date) VALUES ('Christopher Nolan', '1970-07-30');

INSERT INTO person (name, birth_date) VALUES ('Robbie Coltrane', '1950-03-30');

INSERT INTO person (name, birth_date) VALUES ('Donald Trump', '1946-06-14');

INSERT INTO death (date, person_id) VALUES ('2022-10-14', 7);

INSERT INTO death (date, person_id) VALUES ('2018-07-08', 1);

INSERT INTO role (name) VALUES ('Director');

INSERT INTO role (name) VALUES ('Producer');

INSERT INTO role (name) VALUES ('Actor');

INSERT INTO role (name) VALUES ('Screenwriter');

INSERT INTO person_role_movie (role_id, person_id, movie_id) VALUES (1, 1, 4);

INSERT INTO person_role_movie (role_id, person_id, movie_id) VALUES (3, 2, 4);

INSERT INTO person_role_movie (role_id, person_id, movie_id) VALUES (4, 2, 4);

INSERT INTO person_role_movie (role_id, person_id, movie_id) VALUES (3, 3, 2);

INSERT INTO person_role_movie (role_id, person_id, movie_id) VALUES (3, 4, 3);

INSERT INTO person_role_movie (role_id, person_id, movie_id) VALUES (4, 5, 3);

INSERT INTO person_role_movie (role_id, person_id, movie_id) VALUES (1, 6, 3);

INSERT INTO person_role_movie (role_id, person_id, movie_id) VALUES (3, 7, 1);

INSERT INTO genre_movie (genre_id, movie_id) VALUES (1, 1);

INSERT INTO genre_movie (genre_id, movie_id) VALUES (1, 2);

INSERT INTO genre_movie (genre_id, movie_id) VALUES (6, 3);

INSERT INTO genre_movie (genre_id, movie_id) VALUES (1, 3);

INSERT INTO genre_movie (genre_id, movie_id) VALUES (4, 4);

INSERT INTO genre_movie (genre_id, movie_id) VALUES (5, 4);

INSERT INTO country_movie (country_id, movie_id) VALUES (1, 1);

INSERT INTO country_movie (country_id, movie_id) VALUES (1, 2);

INSERT INTO country_movie (country_id, movie_id) VALUES (5, 3);

INSERT INTO country_movie (country_id, movie_id) VALUES (1, 3);

INSERT INTO country_movie (country_id, movie_id) VALUES (4, 4);

INSERT INTO country_movie (country_id, movie_id) VALUES (3, 4);

INSERT INTO person_country (person_id, country_id) VALUES (1, 4);

INSERT INTO person_country (person_id, country_id) VALUES (2, 4);

INSERT INTO person_country (person_id, country_id) VALUES (2, 3);

INSERT INTO person_country (person_id, country_id) VALUES (3, 1);

INSERT INTO person_country (person_id, country_id) VALUES (3, 5);

INSERT INTO person_country (person_id, country_id) VALUES (4, 1);

INSERT INTO person_country (person_id, country_id) VALUES (5, 1);

INSERT INTO person_country (person_id, country_id) VALUES (6, 1);

INSERT INTO person_country (person_id, country_id) VALUES (7, 5);
COMMIT;