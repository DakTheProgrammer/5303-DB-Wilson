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
    GETroutes = ['PercGenre/<string>GENRE', 'AllGenre/<string>GENRE', 'DirecGenre/<string>NAME', 'HighRateGenre/<string>GENRE', 'TitleInfo/<string>NAME']
    example = [url + 'PercGenre/comedy', url + 'AllGenre/action', url + 'DirecGenre/Woody Allen', url + 'HighRateGenre/horror', url + 'TitleInfo/Up']

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