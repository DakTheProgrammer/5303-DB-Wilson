from typing import List
from fastapi import FastAPI
import mysql.connector
import json

jfile = open('Config.json')
data = json.load(jfile)

app = FastAPI()

cnx = mysql.connector.connect(user='dakota', password = data['DBPASS'], host = 'DakotaServer', database = 'IMDB')
cursor = cnx.cursor()

@app.get('/')
async def root():
    url = 'http://167.99.6.44:8002/'
    GETroutes = GETroutes = ['PercGenre/<string>GENRE', 'AllGenre/<string>GENRE', 'DirecGenre/<string>NAME', 'HighRateGenre/<string>GENRE', 'TitleInfo/<string>NAME', 'AllMovies(PLEASE DO NOT RUN THIS WILL CRASH MY SMALL SERVER)', 'AllMovies/<int>YEAR', 'AllMoviesRun/<int>RUNTIME', '/AllMoviesRun/<int>RUNTIME1/<int>RUNTIME2', 'AllMoviesActor/<string>ACTORID', 'Actor/<string>NAME', 'ActorMovies/<string>MOVIEID', 'ActorGenre/<string>GENRE', 'ActorWorkedWith/<string>ACTORID', 'ActorsWithProfession/<string>PROFESSION', 'DiffrentGenres', 'DiffrentProfessions']
    example = [url + 'PercGenre/comedy', url + 'AllGenre/action', url + 'DirecGenre/Woody Allen', url + 'HighRateGenre/horror', url + 'TitleInfo/Up', url + 'AllMovies(PLEASE DO NOT RUN THIS WILL CRASH MY SMALL SERVER)', url + 'AllMovies/2003', url + 'AllMoviesRun/95', url + 'AllMoviesRun/82/93', url +'AllMoviesActor/nm0000020', url + 'Actor/Tom', url + 'ActorMovies/tt0003107', url + 'ActorGenre/Horror', url + 'ActorWorkedWith/nm0000329', url + 'ActorsWithProfession/writer', url + 'DiffrentGenres', url + 'DiffrentProfessions']

    dicGETroute = {}

    for i in range(0, len(GETroutes)):
        dicGETroute.update({GETroutes[i]: url + GETroutes[i]})

    return{'GET routes' : dicGETroute, 'Examples' : example}

@app.get('/PercGenre/{gen}')
async def PercGenre(gen: str):
    question = 'The "%" of movies that are of a specific genre'

    sql = 'SELECT CONCAT(ROUND(COUNT(genre) / (SELECT COUNT(genre) FROM AboutMovies) * 100), "%") AS percentage FROM AboutMovies WHERE genre LIKE %s' #%s = '%GENRE%'

    data = ['%' + gen + '%']

    cursor.execute(sql, data)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

@app.get('/AllGenre/{gen}')
async def AllGenre(gen: str):
    question = 'Movies of specific genre'

    sql = 'SELECT title FROM Movies AS x JOIN AboutMovies AS y ON (x.t_id = y.t_id) WHERE genre LIKE %s'

    data = ['%' + gen + '%']

    cursor.execute(sql, data)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

@app.get('/DirecGenre/{name}')
async def DirecGenre(name: str):
    question = 'Director total films in each genre(query then parse strings)'

    dicOfGen = {
        'Action': 0,
        'Adult': 0,
        'Adventure': 0,
        'Animation': 0,
        'Biography': 0,
        'Comedy': 0,
        'Crime': 0,
        'Documentary': 0,
        'Family': 0,
        'Fantasy': 0,
        'Film-Noir': 0,
        'History': 0,
        'Horror': 0,
        'Musical': 0,
        'Music': 0,
        'Mystery': 0,
        'Romance': 0,
        'Sci-Fi': 0,
        'Short': 0,
        'Sport': 0,
        'Thriller': 0,
        'War': 0,
        'Western': 0
    }

    sql = 'SELECT genre FROM AboutMovies WHERE t_id IN (SELECT t_id FROM Directors WHERE directors LIKE (SELECT name_id FROM FilmMakers WHERE professions LIKE "%director%" AND name_real = %s))'

    data = [name]

    cursor.execute(sql, data)

    res = cursor.fetchall()

    for gen in res:
        if 'Action' in str(gen):
	        dicOfGen['Action'] += 1

        if 'Adult' in str(gen):
            dicOfGen['Adult'] += 1

        if 'Adventure' in str(gen):
            dicOfGen['Adventure'] += 1

        if 'Animation' in str(gen):
            dicOfGen['Animation'] += 1

        if 'Biography' in str(gen):
            dicOfGen['Biography'] += 1

        if 'Comedy' in str(gen):
            dicOfGen['Comedy'] += 1

        if 'Crime' in str(gen):
            dicOfGen['Crime'] += 1

        if 'Documentary' in str(gen):
            dicOfGen['Documentary'] += 1

        if 'Family' in str(gen):
            dicOfGen['Family'] += 1

        if 'Fantasy' in str(gen):
            dicOfGen['Fantasy'] += 1

        if 'Film-Noir' in str(gen):
            dicOfGen['Film-Noir'] += 1

        if 'History' in str(gen):
            dicOfGen['History'] += 1

        if 'Horror' in str(gen):
            dicOfGen['Horror'] += 1

        if 'Musical' in str(gen):
            dicOfGen['Musical'] += 1

        if 'Music' in str(gen):
            dicOfGen['Music'] += 1

        if 'Mystery' in str(gen):
            dicOfGen['Mystery'] += 1

        if 'Romance' in str(gen):
            dicOfGen['Romance'] += 1

        if 'Sci-Fi' in str(gen):
            dicOfGen['Sci-Fi'] += 1

        if 'Short' in str(gen):
            dicOfGen['Short'] += 1

        if 'Sport' in str(gen):
            dicOfGen['Sport'] += 1

        if 'Thriller' in str(gen):
            dicOfGen['Thriller'] += 1

        if 'War' in str(gen):
            dicOfGen['War'] += 1

        if 'Western' in str(gen):
            dicOfGen['Western'] += 1


    return{'question:': question, 'query': sql, 'result': dicOfGen}

@app.get('/HighRateGenre/{gen}')
async def HighRateGenre(gen: str):
    question = 'Highest rated movie of given genre'

    sql = 'SELECT genre, title, avg_rating FROM Movies AS x JOIN AboutMovies AS y ON (x.t_id = y.t_id) JOIN Rating AS z ON (x.t_id = z.t_id) WHERE avg_rating = (SELECT MAX(avg_rating) FROM Rating AS x JOIN AboutMovies AS y ON (x.t_id = y.t_id) WHERE genre LIKE %s) AND genre LIKE %s'

    data = ['%' + gen + '%', '%' + gen + '%']

    cursor.execute(sql, data)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

@app.get('/TitleInfo/{title}')
async def TitleInfo(title: str):
    question = 'Movie info by title'

    sql = 'SELECT title, x.t_id, is_adult, runtime, genre, year, avg_rating, num_votes from Movies AS x JOIN AboutMovies AS y ON (x.t_id = y.t_id) JOIN Rating AS z ON (x.t_id = z.t_id) WHERE title = %s'

    data = [title]

    cursor.execute(sql, data)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

@app.get('/AllMovies/')
async def AllMovies():
    question = 'Find all titles'

    sql = 'SELECT title, y.* FROM Movies AS x JOIN AboutMovies AS y ON (x.t_id = y.t_id)'

    cursor.execute(sql)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

@app.get('/AllMovies/{year}')
async def AllMoviesYear(year: int):
    question = 'Find all tiles in given year'

    sql = 'SELECT title, y.* FROM Movies AS x JOIN AboutMovies AS y ON (x.t_id = y.t_id) WHERE year = %s'

    data = [year]

    cursor.execute(sql, data)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

@app.get('/AllMoviesRun/{runtime}')
async def AllMoviesRuntime(runtime: int):
    question = 'Find all tiles that run higher then a given time(min)'

    sql = 'SELECT title, y.* FROM Movies AS x JOIN AboutMovies AS y ON (x.t_id = y.t_id) WHERE runtime > %s'

    data = [runtime]

    cursor.execute(sql, data)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

@app.get('/AllMoviesRun/{runtime1}/{runtime2}')
async def AllMoviesRuntimes(runtime1: int, runtime2: int):
    question = 'Find all tiles that run between two given time(min) > left < right'

    sql = 'SELECT title, y.* FROM Movies AS x JOIN AboutMovies AS y ON (x.t_id = y.t_id) WHERE runtime > %s AND runtime < %s'

    data = [runtime1, runtime2]

    cursor.execute(sql, data)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

@app.get('/AllMoviesActor/{actorid}')
async def AllMoviesActor(actorid: str):
    question = 'Find all tiles that an actor has acted in'

    sql = 'SELECT title, name_real FROM Movies AS x JOIN MovieCrew AS y ON (x.t_id = y.t_id) JOIN FilmMakers AS z ON (z.name_id = y.name_id) WHERE z.name_id = %s'

    data = [actorid]

    cursor.execute(sql, data)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

# @app.get('/AllMovies/{actorids}')
# async def AllMoviesActors(actorids: List):
#     ...

@app.get('/Actor/{name}')
async def Actor(name: str):
    question = 'Find all info about a given actor'

    sql = 'SELECT * FROM FilmMakers WHERE name_real LIKE %s'

    data = ['%' + name + '%']

    cursor.execute(sql, data)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

@app.get('/ActorMovies/{movieid}')
async def ActorMovies(movieid: str):
    question = 'Find all actor information from a given movie'

    sql = 'SELECT x.*, ordering, catigory, characters FROM FilmMakers AS x JOIN MovieCrew AS y ON (x.name_id = y.name_id) WHERE y.t_id = %s'

    data = [movieid]

    cursor.execute(sql, data)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

@app.get('/ActorGenre/{genre}')
async def ActorGenre(genre: str):
    question = 'Find all actors that have acted in a given genre'

    sql = 'SELECT DISTINCT x.*, genre FROM FilmMakers AS x JOIN MovieCrew AS y ON (x.name_id = y.name_id) JOIN AboutMovies AS z ON (y.t_id = z.t_id) WHERE z.genre = %s'

    data = [genre]

    cursor.execute(sql, data)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

@app.get('/ActorWorkedWith/{actorid}')
async def ActorWorkedWith(actorid: str):
    question = 'Find all actors who have worked with a given actor'

    sql = 'SELECT DISTINCT x.* FROM FilmMakers AS x JOIN MovieCrew AS y ON (x.name_id = y.name_id) WHERE x.name_id != %s AND (y.t_id IN (SELECT t_id FROM MovieCrew WHERE name_id = %s))'

    data = [actorid, actorid]

    cursor.execute(sql, data)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}


# @app.get('/ActorWorkedWithList/{actorids}')
# async def ActorWorkedWithList(actorids: list):
#     ...

@app.get('/ActorsWithProfession/{profession}')
async def ActorsWithProfession(profession: str):
    question = 'Find all actors who have a given profession'

    sql = 'SELECT * FROM FilmMakers WHERE professions LIKE %s'

    data = ['%' + profession + '%']

    cursor.execute(sql, data)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

@app.get('/DiffrentGenres/')
async def DiffrentGenres():
    question = 'Find all the diffrent combonations of genres'

    sql = 'SELECT DISTINCT genre FROM AboutMovies'

    cursor.execute(sql)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}

@app.get('/DiffrentProfessions/')
async def DiffrentProfessions():
    question = 'Find all the diffrent combonations of professions'

    sql = 'SELECT DISTINCT professions FROM FilmMakers'

    cursor.execute(sql)

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]

    return{'question:': question, 'query': sql, 'result': result}