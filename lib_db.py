from sqlalchemy import create_engine, text

class Movie_data(object):
    def __init__(self):
        self._engine = create_engine(f"sqlite:///movie_system.db", echo = True)

    ''' Создаёт таблицы в соответствии с описанной архитектурой '''
    def create_tables(self, file):
        with open(file, 'r') as f:
            queries = f.read().split('\n\n')

        with self._engine.connect() as connection:
            for query in queries:
                replaced_query = query.replace('\n', '')
                sql = text(replaced_query)
                connection.execute(sql)
        print("queries was executed successfully")

    ''' Заполнить таблицы данными '''
    def insert_into_tables(self, file):
        with open(file, 'r') as f:
            queries = f.read().split('\n')

        with self._engine.connect() as connection:
            for query in queries:
                replaced_query = query.replace('\n\n', '')
                sql = text(replaced_query)
                connection.execute(sql)
        print("queries was executed successfully")

    ''' Возвращает список названий фильмов, содержащихся в базе данных '''
    def get_movies(self):
        sql = text("SELECT DISTINCT id, name FROM movie ORDER BY name;")
        with self._engine.connect() as connection:
            sql_result = connection.execute(sql)
        res = []
        for elem in sql_result:
            res.append(elem)
        return res

    ''' Получить жанр фильма по его movie_id'''
    def get_genre(self, movie_id):
        sql = text('SELECT DISTINCT genre.name FROM (SELECT name, genre_id, movie.id AS movie_id FROM movie '
                   'LEFT JOIN genre_movie ON movie.id = genre_movie.movie_id) AS genre_movie '
                   'LEFT JOIN genre ON genre.id = genre_movie.genre_id WHERE movie_id = ' + str(movie_id) + ';')
        with self._engine.connect() as connection:
            sql_result = connection.execute(sql)
        res = []
        for elem in sql_result:
            res.append(elem[0])
        return res

    ''' Возвращает информацию о фильме из таблицы movie по его movie_id '''
    def get_movie(self, movie_id):
        sql = text('SELECT name, creation_year FROM movie WHERE id = ' + str(movie_id) + ';')
        with self._engine.connect() as connection:
            sql_result = connection.execute(sql)
        res = []
        for elem in sql_result:
            res.append(elem)
        return res

    ''' Возвращает список стран, принадлежащих фильму по его movie_id '''
    def get_country(self, movie_id):
        sql = text('SELECT country.name FROM '
                   '(SELECT movie.id AS movie_id, country_id FROM movie LEFT JOIN country_movie '
                   'ON movie.id = country_movie.movie_id) AS movie_country LEFT JOIN country '
                   'ON country.id = movie_country.country_id WHERE movie_id = ' + str(movie_id) + ';')
        with self._engine.connect() as connection:
            sql_result = connection.execute(sql)
        res = []
        for elem in sql_result:
            res.append(elem[0])
        return res

    ''' Возвращает список персон, связанных с фильмом по его movie_id '''
    def get_people(self, movie_id):
        sql = text('SELECT DISTINCT person.name FROM (SELECT movie.id AS movie_id, person_id '
                   'FROM movie LEFT JOIN person_role_movie ON movie.id = person_role_movie.movie_id) AS movie_person '
                   'LEFT JOIN person ON movie_person.person_id = person.id WHERE movie_id = ' + str(movie_id) + ';')
        with self._engine.connect() as connection:
            sql_result = connection.execute(sql)
        res = []
        for elem in sql_result:
            res.append(elem[0])
        return res

    ''' Возвращает список персон, связанных с кинематографом '''
    def get_persons(self):
        sql = text('SELECT DISTINCT id, name FROM person INNER JOIN person_role_movie ON '
                   'person.id = person_role_movie.person_id ORDER BY name;')
        with self._engine.connect() as connection:
            sql_result = connection.execute(sql)
        res = []
        for elem in sql_result:
            res.append(elem)
        return res

    ''' Возвращает информацию о персоне, содержащуюся в таблице person '''
    def get_person(self, person_id):
        sql = text('SELECT name, birth_date FROM person WHERE id = ' + str(person_id) + ';')
        with self._engine.connect() as connection:
            sql_result = connection.execute(sql)
        res = []
        for elem in sql_result:
            res.append(elem)
        return res

    ''' Возвращает дату смерти человека по его person_id, если человек жив, то None '''
    def get_death_date(self, person_id):
        sql = text('SELECT date FROM person LEFT JOIN death ON person.id = death.person_id '
                   'WHERE person.id = ' + str(person_id) + ';')
        with self._engine.connect() as connection:
            sql_result = connection.execute(sql)
        res = []
        for elem in sql_result:
            res.append(elem[0])
        return res

    ''' Возвращает список стран, связанных с фильмом по его movie_id'''
    def get_person_country(self, person_id):
        sql = text('SELECT DISTINCT name FROM (SELECT person.id AS person_id, country_id FROM person LEFT JOIN '
                   'person_country ON person.id = person_country.person_id) AS person_country LEFT JOIN country ON '
                   'person_country.country_id = country.id WHERE '
                   'person_country.person_id = ' + str(person_id) + ' ORDER BY name;')
        with self._engine.connect() as connection:
            sql_result = connection.execute(sql)
        res = []
        for elem in sql_result:
            res.append(elem[0])
        return res

    ''' Возвращает список фильмов, связанных с персоной и список ролей в каждом из них по movie_id'''
    def get_person_movie(self, person_id):
        sql = text('SELECT DISTINCT movie.name, movie.id FROM person_role_movie INNER JOIN movie ON '
                   'person_role_movie.movie_id = movie.id WHERE person_role_movie.person_id = ' + str(person_id) + ';')
        with self._engine.connect() as connection:
            sql_result = connection.execute(sql)
        movies = []
        movie_roles = dict()
        for elem in sql_result:
            movies.append(elem[0])
            movie_id = elem[1]
            sql = text('SELECT DISTINCT name FROM person_role_movie INNER JOIN role ON '
                       'person_role_movie.role_id = role.id WHERE movie_id = ' + str(movie_id) +
                       ' AND person_id = ' + str(person_id) + ';')

            with self._engine.connect() as connection:
                sql_role_result = connection.execute(sql)
            res = []
            for role in sql_role_result:
                res.append(role[0])
            movie_roles[elem[0]] = res
        return movie_roles


bd = Movie_data()
bd.create_tables('create_tables.sql')
bd.insert_into_tables('inserts.sql')
print(bd.get_movies())
print(bd.get_movie(3))
print(bd.get_movie(4), bd.get_genre(4), bd.get_country(4), bd.get_people(4))
print(bd.get_persons())
print(bd.get_person(7))
print(bd.get_death_date(7))
print(bd.get_person_country(2))
print(bd.get_person_movie(5))


