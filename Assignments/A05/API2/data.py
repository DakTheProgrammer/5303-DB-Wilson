import csv
import json
import mysql.connector

jfile = open('Config.json')
data = json.load(jfile)

cnx = mysql.connector.connect(user='dakota', password = data['DBPASS'], host = 'DakotaServer', database = 'IMDB')
cursor = cnx.cursor()

file = 'datasets.imdbws.com/name.basics.tsv'

sql = 'INSERT INTO FilmMakers VALUES(%s, %s, %s, %s, %s, %s)'

with open(file, newline = '\n') as tsvfile:
    movieData = csv.reader(tsvfile, delimiter ='\t')
    for row in movieData:
        temp = row[4].split(',')
        if ('actor' in temp) or ('writer' in temp) or ('director' in temp) and 1 == 0:
            if row[1] == '\\N':
                name = None
            else:
                name = row[1]
            
            if row[2] == '\\N':
                birthYear = None
            else:
                birthYear = row[2]
            
            if row[3] == '\\N':
                deathYear = None
            else:
                deathYear = row[3]
            
            if row[4] == '\\N':
                professions = None
            else:
                professions = row[4]
            
            if row[5] == '\\N':
                knownFor = None
            else:
                knownFor = row[5]
            
            actorID = row[0]
            
            data = (actorID, name, birthYear, deathYear, professions, knownFor)
            cursor.execute(sql, data)
            cnx.commit()
            print(row)

file = 'datasets.imdbws.com/title.crew.tsv'
sql1 = 'INSERT INTO Directors VALUES (%s, %s)'
sql2 = 'INSERT INTO Writers VALUES (%s, %s)'

with open(file, newline = '\n') as tsvfile:
    movieData = csv.reader(tsvfile, delimiter ='\t')
    for row in movieData:
        if 'tconst' not in row:
            if row[1] == '\\N':
                directors = None
            else:
                directors = row[1]
        
            if row[2] == '\\N':
                writers = None
            else:
                writers = row[2]
                
            data1 = (row[0], directors)
            data2 = (row[0], writers)
            cursor.execute(sql1, data1)
            cnx.commit()
            cursor.execute(sql2, data2)
            cnx.commit()
            print(row)

file = 'datasets.imdbws.com/title.principals.tsv'
sql = "INSERT INTO MovieCrew VALUES (%s, %s, %s, %s, %s)"

with open(file, newline = '\n') as tsvfile:
    movieData = csv.reader(tsvfile, delimiter ='\t')
    for row in movieData:
        if 'tconst' not in row:
            print(row)
            if row[1] == '\\N':
                order = None
            else:
                order = row[1]
            
            if row[2] == '\\N':
                name = None
            else:
                name = row[2]
            
            if row[3] == '\\N':
                cat = None
            else:
                cat = row[3]
            
            if row[5] == '\\N':
                char = None
            else:
                char = row[5]
            
            data = (row[0], name, order, cat, char)
            cursor.execute(sql, data)
            cnx.commit()

file = 'datasets.imdbws.com/title.ratings.tsv'
sql = "INSERT INTO Rating VALUES (%s, %s, %s)"

with open(file, newline = '\n') as tsvfile:
    movieData = csv.reader(tsvfile, delimiter ='\t')
    for row in movieData:
        if 'tconst' not in row:
            print(row)
            if row[1] == '\\N':
                rating = None
            else:
                rating = row[1]
            
            if row[2] == '\\N':
                vote = None
            else:
                vote = row[2]
            
            data = (row[0], rating, vote)
            cursor.execute(sql, data)
            cnx.commit()

file = 'datasets.imdbws.com/title.basics.tsv'
sql1 = "INSERT INTO Movies VALUES (%s, %s)"
sql2 = "INSERT INTO AboutMovies VALUES (%s, %s, %s, %s, %s)"

with open(file, newline = '\n') as tsvfile:
        movieData = csv.reader(tsvfile, delimiter ='\t')
        for row in movieData:
            if 'tconst' not in row and row[1] == 'movie':
                print(row)
                if row[2] == '\\N':
                    title = None
                else:
                    title = row[2]
                
                if row[4] == '\\N':
                    adult = None
                else:
                    adult = row[4]
                
                if row[5] == '\\N':
                    syear = None
                else:
                    syear = row[5]

                if row[7] == '\\N':
                    run = None
                else:
                    run = row[7]

                if row[8] == '\\N':
                    gen = None
                else:
                    gen = row[8]
                
                data1 = (row[0], title)
                data2 = (row[0], adult, run, gen, syear)
                cursor.execute(sql1, data1)
                cnx.commit()
                cursor.execute(sql2, data2)
                cnx.commit()
