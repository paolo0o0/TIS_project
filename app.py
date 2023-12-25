from flask import Flask, render_template
from lib_db import Movie_data

app = Flask(__name__)
movie_system = Movie_data()

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/movies")
def list_of_movies():
    movies = movie_system.get_movies()
    return render_template("movies.html.j2", movies=movies)

@app.route("/movies/<movie_id>")
def movie(movie_id=None):
    movie_info = movie_system.get_movie(movie_id)
    genre = movie_system.get_genre(movie_id)
    countries = movie_system.get_country(movie_id)
    people = movie_system.get_people(movie_id)
    return render_template(
        "movie.html.j2",
        name=movie_info[0][0],
        creation_year=movie_info[0][1],
        genre=genre,
        countries=countries,
        people=people,
    )

@app.route("/persons")
def list_of_persons():
    persons = movie_system.get_persons()
    return render_template("people.html.j2", persons=persons)

@app.route("/persons/<person_id>")
def person(person_id=None):
    person_info = movie_system.get_person(person_id)
    death_date = movie_system.get_death_date(person_id)
    countries = movie_system.get_person_country(person_id)
    movies_roles = movie_system.get_person_movie(person_id)
    return render_template(
        "person.html.j2",
        name=person_info[0][0],
        birth_year=person_info[0][1],
        death_date=death_date[0],
        countries=countries,
        movies_roles=movies_roles,
    )

app.run(host="0.0.0.0", port=8000)