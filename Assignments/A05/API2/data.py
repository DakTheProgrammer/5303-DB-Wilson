import csv
import glob
import json
import mysql.connector
import json

jfile = open('Config.json')
data = json.load(jfile)

cnx = mysql.connector.connect(user='dakota', password = data['DBPASS'], host = 'DakotaServer', database = 'SQLZoo')
cursor = cnx.cursor()

files = glob.glob('datasets.imdbws.com/*.tsv')

for file in files:
    print(file)
    with open(file, newline = '\n') as tsvfile:
        movieData = csv.reader(tsvfile, delimiter ='\t')
        for row in movieData:
            print('^'.join(row))