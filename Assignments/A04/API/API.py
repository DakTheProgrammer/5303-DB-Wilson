from fastapi import FastAPI
from fastapi.params import Query
import mysql.connector
import json

from starlette.routing import Route

jfile = open('Config.json')
data = json.load(jfile)

app = FastAPI()

cnx = mysql.connector.connect(user='dakota', password = data['DBPASS'], host = 'DakotaServer', database = 'SQLZoo')
cursor = cnx.cursor()

@app.get('/')
async def root():
    url = 'http://167.99.6.44:8001/'
    GETroutes = ['basics', 'world', 'nobel', 'within', 'aggregate', 'joins', 'all']
    PUTroutes = ['world']
    POSTroutes = ['teacher']

    dicGETroute = {}
    dicPUTroute = {}
    dicPOSTroute = {}

    for i in range(0, len(GETroutes)):
        dicGETroute.update({GETroutes[i]: url + GETroutes[i]})

    for i in range(0, len(PUTroutes)):
        dicPUTroute.update({PUTroutes[i]: url + PUTroutes[i]})

    for i in range(0, len(POSTroutes)):
        dicPOSTroute.update({POSTroutes[i]: url + POSTroutes[i]})

    return{'GET routes' : dicGETroute, 'PUT routes'  : dicPUTroute, 'POST routes': dicPOSTroute}

@app.get('/basics')
async def basic():
    questions = {
    1: "show the population of Germany",
    2: "Show the name and the population for 'Sweden', 'Norway' and 'Denmark'.",
    3: "Which countries are not too small and not too big? BETWEEN allows range checking (range specified is inclusive of boundary values). The example below shows countries with an area of 250,000-300,000 sq. km. Modify it to show the country and the area for countries with an area between 200,000 and 250,000."
    }
    queries = {
    1: "SELECT population FROM world WHERE name = 'Germany';",
    2: "SELECT name, population FROM world WHERE name IN ('Sweden', 'Norway','Denmark');",
    3: "SELECT name, area FROM world WHERE area BETWEEN 200000 AND 250000;"
    }

    result = {}

    for query in queries:
        cursor.execute(queries[query])

        columns = cursor.description
        result.update({query: [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]})

    return{'questions': questions, 'sql': queries, 'results': result}

@app.get('/basics/{id}')
async def basic_read_item(id: int):
    questions = {
    1: "show the population of Germany",
    2: "Show the name and the population for 'Sweden', 'Norway' and 'Denmark'.",
    3: "Which countries are not too small and not too big? BETWEEN allows range checking (range specified is inclusive of boundary values). The example below shows countries with an area of 250,000-300,000 sq. km. Modify it to show the country and the area for countries with an area between 200,000 and 250,000."
    }
    queries = {
    1: "SELECT population FROM world WHERE name = 'Germany';",
    2: "SELECT name, population FROM world WHERE name IN ('Sweden', 'Norway','Denmark');",
    3: "SELECT name, area FROM world WHERE area BETWEEN 200000 AND 250000;"
    }
    
    cursor.execute(queries[id])

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    
    return{'question': questions[id],'sql': queries[id], 'result': result}

@app.get('/world')
async def world():
    questions = {
    1: "Observe the result of running this SQL command to show the name, continent and population of all countries.",
    2: "Show the name for the countries that have a population of at least 200 million. 200 million is 200000000, there are eight zeros.",
    3: "Give the name and the per capita GDP for those countries with a population of at least 200 million.",
    4: "Show the name and population in millions for the countries of the continent 'South America'. Divide the population by 1000000 to get population in millions.",
    5: "Show the name and population for France, Germany, Italy",
    6: "Show the countries which have a name that includes the word 'United'",
    7: "Show the countries that are big by area or big by population. Show name, population and area.",
    8: "Exclusive OR (XOR). Show the countries that are big by area (more than 3 million) or big by population (more than 250 million) but not both. Show name, population and area.",
    9: "For South America show population in millions and GDP in billions both to 2 decimal places.",
    10: "Show per-capita GDP for the trillion dollar countries to the nearest $1000.",
    11: "Show the name and capital where the name and the capital have the same number of characters.",
    12: "Show the name and the capital where the first letters of each match. Don't include countries where the name and the capital are the same word.",
    13: "Find the country that has all the vowels and no spaces in its name."
    }
    queries = {
    1:"SELECT name, continent, population FROM world;",
    2:"SELECT name FROM world WHERE population >= 200000000;",
    3:"SELECT name,gdp FROM world WHERE population >= 200000000;",
    4:"SELECT name, population/1000000 FROM world WHERE continent = 'South America';",
    5:"SELECT name, population FROM world WHERE name IN ('France','Germany','Italy');",
    6:"SELECT name FROM world WHERE name LIKE '%United%';",
    7:"SELECT name, population,area FROM world WHERE area >= 3000000 OR population >= 250000000;",
    8:"SELECT name, population,area FROM world WHERE area >= 3000000 XOR population >= 250000000;",
    9:"SELECT name,ROUND(population/1000000,2), ROUND(gdp/1000000000,2) FROM world WHERE continent = 'South America';",
    10:"SELECT name,ROUND(gdp/population,-3) FROM world WHERE gdp > 1000000000000;",
    11:"SELECT name,capital FROM world WHERE LENGTH(name) = LENGTH(capital);",
    12:"SELECT name, capital FROM world WHERE LEFT(name,1) = LEFT(capital,1) AND name <> capital;",
    13:"SELECT name FROM world WHERE name LIKE '%a%' AND name LIKE '%e%' AND name LIKE '%i%' AND name LIKE '%o%' AND name LIKE '%u%' AND name NOT LIKE '% %';"
    }

    result = {}

    for query in queries:
        cursor.execute(queries[query])

        columns = cursor.description
        result.update({query: [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]})

    return{'questions': questions,'sql': queries, 'results': result}

@app.get('/world/{id}')
async def world_read_item(id: int):
    questions = {
    1: "Observe the result of running this SQL command to show the name, continent and population of all countries.",
    2: "Show the name for the countries that have a population of at least 200 million. 200 million is 200000000, there are eight zeros.",
    3: "Give the name and the per capita GDP for those countries with a population of at least 200 million.",
    4: "Show the name and population in millions for the countries of the continent 'South America'. Divide the population by 1000000 to get population in millions.",
    5: "Show the name and population for France, Germany, Italy",
    6: "Show the countries which have a name that includes the word 'United'",
    7: "Show the countries that are big by area or big by population. Show name, population and area.",
    8: "Exclusive OR (XOR). Show the countries that are big by area (more than 3 million) or big by population (more than 250 million) but not both. Show name, population and area.",
    9: "For South America show population in millions and GDP in billions both to 2 decimal places.",
    10: "Show per-capita GDP for the trillion dollar countries to the nearest $1000.",
    11: "Show the name and capital where the name and the capital have the same number of characters.",
    12: "Show the name and the capital where the first letters of each match. Don't include countries where the name and the capital are the same word.",
    13: "Find the country that has all the vowels and no spaces in its name."
    }
    queries = {
    1:"SELECT name, continent, population FROM world;",
    2:"SELECT name FROM world WHERE population >= 200000000;",
    3:"SELECT name,gdp FROM world WHERE population >= 200000000;",
    4:"SELECT name, population/1000000 FROM world WHERE continent = 'South America';",
    5:"SELECT name, population FROM world WHERE name IN ('France','Germany','Italy');",
    6:"SELECT name FROM world WHERE name LIKE '%United%';",
    7:"SELECT name, population,area FROM world WHERE area >= 3000000 OR population >= 250000000;",
    8:"SELECT name, population,area FROM world WHERE area >= 3000000 XOR population >= 250000000;",
    9:"SELECT name,ROUND(population/1000000,2), ROUND(gdp/1000000000,2) FROM world WHERE continent = 'South America';",
    10:"SELECT name,ROUND(gdp/population,-3) FROM world WHERE gdp > 1000000000000;",
    11:"SELECT name,capital FROM world WHERE LENGTH(name) = LENGTH(capital);",
    12:"SELECT name, capital FROM world WHERE LEFT(name,1) = LEFT(capital,1) AND name <> capital;",
    13:"SELECT name FROM world WHERE name LIKE '%a%' AND name LIKE '%e%' AND name LIKE '%i%' AND name LIKE '%o%' AND name LIKE '%u%' AND name NOT LIKE '% %';"
    }
    
    cursor.execute(queries[id])

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    
    return{'question': questions[id],'sql': queries[id], 'result': result}

@app.get('/nobel')
async def nobel():
    questions = {
    1: "Change the query shown so that it displays Nobel prizes for 1950.",
    2: "Show who won the 1962 prize for Literature.",
    3: "Show the year and subject that won 'Albert Einstein' his prize.",
    4: "Give the name of the 'Peace' winners since the year 2000, including 2000.",
    5: "Show all details (yr, subject, winner) of the Literature prize winners for 1980 to 1989 inclusive.",
    6: "Show all details of the presidential winners:",
    7: "Show the winners with first name John",
    8: "Show the year, subject, and name of Physics winners for 1980 together with the Chemistry winners for 1984.",
    9: "Show the year, subject, and name of winners for 1980 excluding Chemistry and Medicine",
    10: "Show year, subject, and name of people who won a 'Medicine' prize in an early year (before 1910, not including 1910) together with winners of a 'Literature' prize in a later year (after 2004, including 2004)",
    11: "Find all details of the prize won by PETER GRÜNBERG",
    13: "Find all details of the prize won by EUGENE O'NEILL",
    14: "List the winners, year and subject where the winner starts with Sir. Show the the most recent first, then by name order."
    }
    queries = {
    1: "SELECT yr, subject, winner FROM nobel WHERE yr = 1950;",
    2: "SELECT winner FROM nobel WHERE yr = 1962 AND subject = 'Literature';",
    3: "SELECT yr,subject FROM nobel WHERE winner = 'Albert Einstein';",
    4: "SELECT winner FROM nobel WHERE subject = 'Peace' AND yr >= 2000;",
    5: "SELECT yr,subject,winner FROM nobel WHERE subject = 'Literature' AND yr <= 1989 AND yr >= 1980;",
    6: "SELECT * FROM nobel WHERE winner IN ('Theodore Roosevelt', 'Woodrow Wilson', 'Jimmy Carter', 'Barack Obama');",
    7: "SELECT winner FROM nobel WHERE winner LIKE 'John %';",
    8: "SELECT * FROM nobel WHERE (subject = 'Physics' AND yr = 1980) OR (subject = 'Chemistry ' AND yr = 1984);",
    9: "SELECT * FROM nobel WHERE yr = 1980 AND NOT (subject = 'Chemistry' or subject = 'Medicine');",
    10: "SELECT * FROM nobel WHERE (yr < 1910 AND subject = 'Medicine') OR (yr >= 2004 AND subject = 'Literature');",
    11: "SELECT * FROM nobel WHERE winner = 'PETER GRÜNBERG';",
    12: "SELECT * FROM nobel WHERE winner = 'EUGENE O''NEILL';",
    13: "SELECT winner, yr, subject FROM nobel WHERE winner LIKE 'Sir%' ORDER BY yr DESC,winner;",
    14: "SELECT winner, subject FROM nobel WHERE yr=1984 ORDER BY subject IN ('Chemistry','Physics') ,subject, winner;"
    }

    result = {}

    for query in queries:
        cursor.execute(queries[query])

        columns = cursor.description
        result.update({query: [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]})

    return{'questions': questions,'sql': queries, 'results': result}

@app.get('/nobel/{id}')
async def nobel_read_item(id: int):
    questions = {
    1: "Change the query shown so that it displays Nobel prizes for 1950.",
    2: "Show who won the 1962 prize for Literature.",
    3: "Show the year and subject that won 'Albert Einstein' his prize.",
    4: "Give the name of the 'Peace' winners since the year 2000, including 2000.",
    5: "Show all details (yr, subject, winner) of the Literature prize winners for 1980 to 1989 inclusive.",
    6: "Show all details of the presidential winners:",
    7: "Show the winners with first name John",
    8: "Show the year, subject, and name of Physics winners for 1980 together with the Chemistry winners for 1984.",
    9: "Show the year, subject, and name of winners for 1980 excluding Chemistry and Medicine",
    10: "Show year, subject, and name of people who won a 'Medicine' prize in an early year (before 1910, not including 1910) together with winners of a 'Literature' prize in a later year (after 2004, including 2004)",
    11: "Find all details of the prize won by PETER GRÜNBERG",
    13: "Find all details of the prize won by EUGENE O'NEILL",
    14: "List the winners, year and subject where the winner starts with Sir. Show the the most recent first, then by name order."
    }
    queries = {
    1: "SELECT yr, subject, winner FROM nobel WHERE yr = 1950;",
    2: "SELECT winner FROM nobel WHERE yr = 1962 AND subject = 'Literature';",
    3: "SELECT yr,subject FROM nobel WHERE winner = 'Albert Einstein';",
    4: "SELECT winner FROM nobel WHERE subject = 'Peace' AND yr >= 2000;",
    5: "SELECT yr,subject,winner FROM nobel WHERE subject = 'Literature' AND yr <= 1989 AND yr >= 1980;",
    6: "SELECT * FROM nobel WHERE winner IN ('Theodore Roosevelt', 'Woodrow Wilson', 'Jimmy Carter', 'Barack Obama');",
    7: "SELECT winner FROM nobel WHERE winner LIKE 'John %';",
    8: "SELECT * FROM nobel WHERE (subject = 'Physics' AND yr = 1980) OR (subject = 'Chemistry ' AND yr = 1984);",
    9: "SELECT * FROM nobel WHERE yr = 1980 AND NOT (subject = 'Chemistry' or subject = 'Medicine');",
    10: "SELECT * FROM nobel WHERE (yr < 1910 AND subject = 'Medicine') OR (yr >= 2004 AND subject = 'Literature');",
    11: "SELECT * FROM nobel WHERE winner = 'PETER GRÜNBERG';",
    12: "SELECT * FROM nobel WHERE winner = 'EUGENE O''NEILL';",
    13: "SELECT winner, yr, subject FROM nobel WHERE winner LIKE 'Sir%' ORDER BY yr DESC,winner;",
    14: "SELECT winner, subject FROM nobel WHERE yr=1984 ORDER BY subject IN ('Chemistry','Physics') ,subject, winner;"
    }
    
    cursor.execute(queries[id])

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    
    return{'question': questions[id],'sql': queries[id], 'result': result}

@app.get('/within')
async def within():
    questions = {
    1: "List each country name where the population is larger than that of 'Russia'.",
    2: "Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.",
    3: "List the name and continent of countries in the continents containing either Argentina or Australia. Order by name of the country.",
    4: "Which country has a population that is more than Canada but less than Poland? Show the name and the population.",
    5: "Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.",
    6: "Which countries have a GDP greater than every country in Europe? [Give the name only.] (Some countries may have NULL gdp values)",
    7: "Find the largest country (by area) in each continent, show the continent, the name and the area:",
    8: "List each continent and the name of the country that comes first alphabetically.",
    9: "Find the continents where all countries have a population <= 25000000. Then find the names of the countries associated with these continents. Show name, continent and population.",
    10: "Some countries have populations more than three times that of any of their neighbours (in the same continent). Give the countries and continents."
    }
    queries = {
    1: "SELECT name FROM world WHERE population > (SELECT population FROM world WHERE name='Russia');",
    2: "SELECT name FROM world WHERE gdp/population > (SELECT gdp/population FROM world WHERE name = 'United Kingdom') AND continent = 'Europe';",
    3: "SELECT name,continent FROM world WHERE continent = (SELECT continent FROM world WHERE name = 'Argentina ') OR continent = (SELECT continent FROM world WHERE name = 'Australia') ORDER BY name;",
    4: "SELECT name,population FROM world WHERE population > (SELECT population FROM world WHERE name = 'Canada') AND population < (SELECT population FROM world WHERE name = 'Poland');",
    5: "SELECT name, CONCAT(ROUND(population/(SELECT population FROM world WHERE name = 'Germany')* 100),'%')  AS percentage FROM world WHERE continent = 'Europe';",
    6: "SELECT name FROM world WHERE gdp > ALL(SELECT gdp FROM world WHERE continent = 'Europe' AND gdp IS NOT null);",
    7: "SELECT continent, name, area FROM world x WHERE area >= ALL (SELECT area FROM world y WHERE y.continent=x.continent AND area>0);",
    8: "SELECT continent, name FROM world x WHERE name <= ALL(SELECT name FROM world y WHERE x.continent = y.continent);",
    9: "SELECT name, continent, population FROM world x WHERE 25000000 >= ALL(SELECT population FROM world y WHERE x.continent = y.continent);",
    10: "SELECT name, continent FROM world x WHERE population > ALL(SELECT population * 3 FROM world y WHERE x.continent = y.continent AND x.name != y.name);"
    }

    result = {}

    for query in queries:
        cursor.execute(queries[query])

        columns = cursor.description
        result.update({query: [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]})

    return{'questions': questions,'sql': queries, 'results': result}

@app.get('/within/{id}')
async def within_read_item(id: int):
    questions = {
    1: "List each country name where the population is larger than that of 'Russia'.",
    2: "Show the countries in Europe with a per capita GDP greater than 'United Kingdom'.",
    3: "List the name and continent of countries in the continents containing either Argentina or Australia. Order by name of the country.",
    4: "Which country has a population that is more than Canada but less than Poland? Show the name and the population.",
    5: "Show the name and the population of each country in Europe. Show the population as a percentage of the population of Germany.",
    6: "Which countries have a GDP greater than every country in Europe? [Give the name only.] (Some countries may have NULL gdp values)",
    7: "Find the largest country (by area) in each continent, show the continent, the name and the area:",
    8: "List each continent and the name of the country that comes first alphabetically.",
    9: "Find the continents where all countries have a population <= 25000000. Then find the names of the countries associated with these continents. Show name, continent and population.",
    10: "Some countries have populations more than three times that of any of their neighbours (in the same continent). Give the countries and continents."
    }
    queries = {
    1: "SELECT name FROM world WHERE population > (SELECT population FROM world WHERE name='Russia');",
    2: "SELECT name FROM world WHERE gdp/population > (SELECT gdp/population FROM world WHERE name = 'United Kingdom') AND continent = 'Europe';",
    3: "SELECT name,continent FROM world WHERE continent = (SELECT continent FROM world WHERE name = 'Argentina ') OR continent = (SELECT continent FROM world WHERE name = 'Australia') ORDER BY name;",
    4: "SELECT name,population FROM world WHERE population > (SELECT population FROM world WHERE name = 'Canada') AND population < (SELECT population FROM world WHERE name = 'Poland');",
    5: "SELECT name, CONCAT(ROUND(population/(SELECT population FROM world WHERE name = 'Germany')* 100),'%')  AS percentage FROM world WHERE continent = 'Europe';",
    6: "SELECT name FROM world WHERE gdp > ALL(SELECT gdp FROM world WHERE continent = 'Europe' AND gdp IS NOT null);",
    7: "SELECT continent, name, area FROM world x WHERE area >= ALL (SELECT area FROM world y WHERE y.continent=x.continent AND area>0);",
    8: "SELECT continent, name FROM world x WHERE name <= ALL(SELECT name FROM world y WHERE x.continent = y.continent);",
    9: "SELECT name, continent, population FROM world x WHERE 25000000 >= ALL(SELECT population FROM world y WHERE x.continent = y.continent);",
    10: "SELECT name, continent FROM world x WHERE population > ALL(SELECT population * 3 FROM world y WHERE x.continent = y.continent AND x.name != y.name);"
    }
    
    cursor.execute(queries[id])

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    
    return{'question': questions[id],'sql': queries[id], 'result': result}

@app.get('/aggregate')
async def aggregate():
    questions = {
    1: "Show the total population of the world.",
    2: "List all the continents - just once each.",
    3: "Give the total GDP of Africa",
    4: "How many countries have an area of at least 1000000",
    5: "What is the total population of ('Estonia', 'Latvia', 'Lithuania')",
    6: "For each continent show the continent and number of countries.",
    7: "For each continent show the continent and number of countries with populations of at least 10 million.",
    8: "List the continents that have a total population of at least 100 million."
    }
    queries = {
    1: "SELECT SUM(population) FROM world;",
    2: "SELECT DISTINCT(continent) FROM world;",
    3: "SELECT SUM(gdp) FROM world WHERE continent = 'Africa';",
    4: "SELECT COUNT(area) FROM world WHERE area >= 1000000;",
    5: "SELECT SUM(population) FROM world WHERE name IN ('Estonia','Latvia','Lithuania');",
    6: "SELECT continent, COUNT(name) FROM world GROUP BY(continent);",
    7: "SELECT continent, COUNT(name) FROM world WHERE population >= 10000000 GROUP BY continent;",
    8: "SELECT continent FROM world GROUP BY continent HAVING SUM(population) >= 100000000;"
    }

    result = {}

    for query in queries:
        cursor.execute(queries[query])

        columns = cursor.description
        result.update({query: [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]})

    return{'questions': questions,'sql': queries, 'results': result}

@app.get('/aggregate/{id}')
async def aggregate_read_item(id: int):
    questions = {
    1: "Show the total population of the world.",
    2: "List all the continents - just once each.",
    3: "Give the total GDP of Africa",
    4: "How many countries have an area of at least 1000000",
    5: "What is the total population of ('Estonia', 'Latvia', 'Lithuania')",
    6: "For each continent show the continent and number of countries.",
    7: "For each continent show the continent and number of countries with populations of at least 10 million.",
    8: "List the continents that have a total population of at least 100 million."
    }
    queries = {
    1: "SELECT SUM(population) FROM world;",
    2: "SELECT DISTINCT(continent) FROM world;",
    3: "SELECT SUM(gdp) FROM world WHERE continent = 'Africa';",
    4: "SELECT COUNT(area) FROM world WHERE area >= 1000000;",
    5: "SELECT SUM(population) FROM world WHERE name IN ('Estonia','Latvia','Lithuania');",
    6: "SELECT continent, COUNT(name) FROM world GROUP BY(continent);",
    7: "SELECT continent, COUNT(name) FROM world WHERE population >= 10000000 GROUP BY continent;",
    8: "SELECT continent FROM world GROUP BY continent HAVING SUM(population) >= 100000000;"
    }
    
    cursor.execute(queries[id])

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    
    return{'question': questions[id],'sql': queries[id], 'result': result}

@app.get('/joins')
async def joins():
    questions = {
    1: "show the matchid and player name for all goals scored by Germany. To identify German players, check for: teamid = 'GER'",
    2: "Show id, stadium, team1, team2 for just game 1012",
    3: "show the player, teamid, stadium and mdate for every German goal.",
    4: "Show the team1, team2 and player for every goal scored by a player called Mario player LIKE 'Mario%'",
    5: "Show player, teamid, coach, gtime for all goals scored in the first 10 minutes gtime<=10",
    6: "List the dates of the matches and the name of the team in which 'Fernando Santos' was the team1 coach.",
    7: "List the player for every goal scored in a game where the stadium was 'National Stadium, Warsaw'",
    8: "Instead show the name of all players who scored a goal against Germany.",
    9: "Show teamname and the total number of goals scored.",
    10: "Show the stadium and the number of goals scored in each stadium.",
    11: "For every match involving 'POL', show the matchid, date and the number of goals scored.",
    12: "For every match where 'GER' scored, show matchid, match date and the number of goals scored by 'GER'",
    13: "List every match with the goals scored by each team as shown. This will use CASE WHEN which has not been explained in any previous exercises."
    }
    queries = {
    1: "SELECT matchid, player FROM goal WHERE teamid = 'GER';",
    2: "SELECT id,stadium,team1,team2 FROM game WHERE id = 1012;",
    3: "SELECT player, teamid,stadium, mdate FROM game JOIN goal ON (id=matchid) WHERE teamid = 'GER';",
    4: "SELECT team1, team2, player FROM game JOIN goal ON (id=matchid) WHERE player LIKE('Mario%');",
    5: "SELECT player, teamid, coach, gtime FROM goal JOIN eteam ON teamid=id WHERE gtime<=10;",
    6: "SELECT mdate, teamname FROM game JOIN eteam ON team1=eteam.id WHERE coach = 'Fernando Santos';",
    7: "SELECT player FROM goal JOIN game ON matchid=game.id WHERE stadium = 'National Stadium, Warsaw';",
    8: "SELECT DISTINCT player FROM game JOIN goal ON matchid = id  WHERE ((team1='GER' OR team2='GER') AND teamid != 'GER');", 
    9: "SELECT teamname, COUNT(teamid) FROM eteam JOIN goal ON id=teamid GROUP BY teamname;",
    10: "SELECT stadium, count(matchid) FROM game JOIN goal ON id=goal.matchid GROUP BY stadium;",
    11: "SELECT matchid,mdate, COUNT(matchid) FROM game JOIN goal ON matchid = id WHERE (team1 = 'POL' OR team2 = 'POL') GROUP BY matchid, mdate;",
    12: "SELECT DISTINCT id, mdate, COUNT(teamid) FROM game JOIN goal ON id=goal.matchid WHERE teamid = 'GER' GROUP BY id, mdate;",
    13: "SELECT mdate, team1, SUM(CASE WHEN teamid=team1 THEN 1 ELSE 0 END) AS score1, team2, SUM(CASE WHEN teamid=team2 THEN 1 ELSE 0 END) AS score2 FROM game LEFT JOIN goal ON matchid = id GROUP BY mdate, team1, team2 ORDER BY mdate, matchid, team1 AND team2;"
    }

    result = {}

    for query in queries:
        cursor.execute(queries[query])

        columns = cursor.description
        result.update({query: [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]})

    return{'questions': questions,'sql': queries, 'results': result}

@app.get('/joins/{id}')
async def joins_read_item(id: int):
    questions = {
    1: "show the matchid and player name for all goals scored by Germany. To identify German players, check for: teamid = 'GER'",
    2: "Show id, stadium, team1, team2 for just game 1012",
    3: "show the player, teamid, stadium and mdate for every German goal.",
    4: "Show the team1, team2 and player for every goal scored by a player called Mario player LIKE 'Mario%'",
    5: "Show player, teamid, coach, gtime for all goals scored in the first 10 minutes gtime<=10",
    6: "List the dates of the matches and the name of the team in which 'Fernando Santos' was the team1 coach.",
    7: "List the player for every goal scored in a game where the stadium was 'National Stadium, Warsaw'",
    8: "Instead show the name of all players who scored a goal against Germany.",
    9: "Show teamname and the total number of goals scored.",
    10: "Show the stadium and the number of goals scored in each stadium.",
    11: "For every match involving 'POL', show the matchid, date and the number of goals scored.",
    12: "For every match where 'GER' scored, show matchid, match date and the number of goals scored by 'GER'",
    13: "List every match with the goals scored by each team as shown. This will use CASE WHEN which has not been explained in any previous exercises."
    }
    queries = {
    1: "SELECT matchid, player FROM goal WHERE teamid = 'GER';",
    2: "SELECT id,stadium,team1,team2 FROM game WHERE id = 1012;",
    3: "SELECT player, teamid,stadium, mdate FROM game JOIN goal ON (id=matchid) WHERE teamid = 'GER';",
    4: "SELECT team1, team2, player FROM game JOIN goal ON (id=matchid) WHERE player LIKE('Mario%');",
    5: "SELECT player, teamid, coach, gtime FROM goal JOIN eteam ON teamid=id WHERE gtime<=10;",
    6: "SELECT mdate, teamname FROM game JOIN eteam ON team1=eteam.id WHERE coach = 'Fernando Santos';",
    7: "SELECT player FROM goal JOIN game ON matchid=game.id WHERE stadium = 'National Stadium, Warsaw';",
    8: "SELECT DISTINCT player FROM game JOIN goal ON matchid = id  WHERE ((team1='GER' OR team2='GER') AND teamid != 'GER');", 
    9: "SELECT teamname, COUNT(teamid) FROM eteam JOIN goal ON id=teamid GROUP BY teamname;",
    10: "SELECT stadium, count(matchid) FROM game JOIN goal ON id=goal.matchid GROUP BY stadium;",
    11: "SELECT matchid,mdate, COUNT(matchid) FROM game JOIN goal ON matchid = id WHERE (team1 = 'POL' OR team2 = 'POL') GROUP BY matchid, mdate;",
    12: "SELECT DISTINCT id, mdate, COUNT(teamid) FROM game JOIN goal ON id=goal.matchid WHERE teamid = 'GER' GROUP BY id, mdate;",
    13: "SELECT mdate, team1, SUM(CASE WHEN teamid=team1 THEN 1 ELSE 0 END) AS score1, team2, SUM(CASE WHEN teamid=team2 THEN 1 ELSE 0 END) AS score2 FROM game LEFT JOIN goal ON matchid = id GROUP BY mdate, team1, team2 ORDER BY mdate, matchid, team1 AND team2;"
    }
    
    cursor.execute(queries[id])

    columns = cursor.description
    result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cursor.fetchall()]
    
    return{'question': questions[id],'sql': queries[id], 'result': result}

@app.get('/all')
async def all():
    url = 'http://167.99.6.44:8001/'
    routes = ['basics', 'world', 'nobel', 'within', 'aggregate', 'joins']
    qcount = [3, 13, 14, 10, 8, 13]

    lofroutes = {}

    ids = []

    temp = {}

    for i in range(0,len(qcount)):
        for j in range(1,qcount[i] + 1):
            temp.update({j: url + routes[i] + '/' + str(j)})
        ids.append(temp)
        temp = {}

    for i in range(0, len(routes)):
        lofroutes.update({routes[i]: {
            'all': url + routes[i],
            'problem #': ids[i]
        }})
        

    return{'problem sets' : lofroutes}

@app.post('/teachers')
async def teachers(body: dict):
    data = {
    "id" : "int(11)",
    "dept" : "int(11)",
    "name" : "varchar(50)",
    "phone" : "varchar(50)",
    "mobile" : "varchar(50)"
    }

    query = "INSERT INTO teacher(id, dept, name, phone, mobile) VALUES (%s, %s, %s, %s, %s)"
    params = [body['id'], body['dept'], body['name'], body['phone'], body['mobile']]

    cursor.execute(query, params)
    cnx.commit()

    return{'params': data, 'sql': query, 'inserted': params}

@app.put('/world')
async def put_world(body: dict):
    data = {
        "required":{
            "name" : "varchar(50)",
        },
        "optional":{
            "continent": "varchar(60)",
            "area": "decimal(10,0)",
            "population": "decimal(11,0)",
            "gdp": "decimal(14,0)",
            "capital": "varchar(60)",
            "tld": "varchar(5)",
            "flag": "varchar(255)",
        }
    }

    query = "UPDATE world SET "

    params = []
    name = ''

    for stuff in body:
        if stuff != "name":
            query += (str(stuff) + " = %s, ")
            params.append(body[stuff])
        else:
            name = body[stuff]


    params.append(name)

    query = query[0:-2]

    query += " WHERE name = %s"

    cursor.execute(query, params)
    cnx.commit()

    return{'params': data, 'sql': query, 'updated': params}