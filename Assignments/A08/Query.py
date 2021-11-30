import json
import mysql.connector
import time
import pymongo
import redis
import random

file = open('MOCK_DATA.json', 'r' , encoding="utf-8")
info = json.load(file)

red = redis.Redis(host='localhost', port=6379, db=0)

passfile = open('Config.json', 'r')
passwords = json.load(passfile)

cnx = mysql.connector.connect(user='dakota', password = passwords['DBPASS'], host = 'DakotaServer', database = 'Test')
cursor = cnx.cursor(buffered=True)

mongo = pymongo.MongoClient('mongodb://167.99.6.44:27017')
db = mongo['Test']
coll = db['tester']

single = 'SELECT * FROM tester WHERE id = %s'

sql = 'INSERT INTO tester VALUES (%s, %s, %s, %s, %s, %s)'

update = 'UPDATE tester SET gender = %s WHERE id = %s'

multi = 'SELECT * FROM tester'

delete = 'DELETE FROM tester WHERE id = %s;'
deleteall = 'DELETE FROM tester'

print('==========================INSERTS======================')

for N in (250, 500, 750, 1000):
    cursor.execute(deleteall)
    cnx.commit()

    start = time.time()

    for i, rows in enumerate(info):
        cursor.execute(sql, [rows['id'], rows['first_name'], rows['last_name'], rows['email'], rows['gender'], rows['city']])
        cnx.commit()
        if i == N - 1:
            break

    end = time.time()

    print('Sql took ', end-start, ' seconds to insert ', N)

print('---------------------------------------------------')

for N in (250, 500, 750, 1000):
    coll.drop()

    start = time.time()

    coll.insert_many(info[0:N])

    end = time.time()

    print('Mongo took ', end-start, ' seconds to insert ', N)

print('---------------------------------------------------')

for N in (250, 500, 750, 1000):
    red.flushall()

    start = time.time()

    for i, rows in enumerate(info):
        red.hset(rows['id'],  mapping={'first_name': rows['first_name'], 'last_name': rows['last_name'], 'email': rows['email'], 'gender': rows['gender'], 'city': rows['city']})
        if i == N - 1:
            break

    end = time.time()

    print('Redis took ', end-start, ' seconds to insert ', N)

print('==========================SINGLE SELECTS======================')

for N in (250, 500, 750, 1000):
    
    start = time.time()
    for i in range(1,N + 1):
        cursor.execute(single, [random.randint(1, 1000)])
    end = time.time()

    print('Sql took ', end-start, ' seconds to search ', N, ' single random items')

    start = time.time()
    for i in range(1,N + 1):
        coll.find({'id': random.randint(1, 1000)},{'_id': 0})
    end = time.time()

    print('MongoDB took ', end-start, ' seconds to search ', N, ' single random items')

    start = time.time()
    for i in range(1,N + 1):
        red.hgetall(random.randint(1, 1000))
    end = time.time()

    print('Redis took ', end-start, ' seconds to search ', N, ' single random items')

    print('----------------------------------------------\n')

print('==========================MULTI SELECTS======================')

for N in (250, 500, 750, 1000):
    
    start = time.time()
    for i in range(1,N + 1):
        cursor.execute(multi)
    end = time.time()

    print('Sql took ', end-start, ' seconds to search ', N, ' multiple random items')

    start = time.time()
    for i in range(1,N + 1):
        coll.find({},{'_id': 0})
    end = time.time()

    print('MongoDB took ', end-start, ' seconds to search ', N, ' multiple random items')

    start = time.time()
    keys = red.keys('*')
    for i in range(1,N + 1):
        for key in keys:
            red.hgetall(int(str(key)[2:-1]))
    end = time.time()

    print('Redis took ', end-start, ' seconds to search ', N, ' multiple items')

    print('----------------------------------------------\n')

print('==========================UPDATES======================')

for N in (250, 500, 750, 1000):
    
    start = time.time()
    for i in range(1,N + 1):
        cursor.execute(update, [random.randint(1, 1000), random.randint(1, 1000)])
        cnx.commit()
    end = time.time()

    print('Sql took ', end-start, ' seconds to update ', N, ' random items')

    start = time.time()
    for i in range(1,N + 1):
        coll.update_one({'id': random.randint(1, 1000)}, {'$set':{'gender':random.randint(1, 1000)}})
    end = time.time()

    print('MongoDB took ', end-start, ' seconds to update ', N, ' random items')

    start = time.time()
    for i in range(1,N + 1):
        key = random.randint(1, 1000)
        row = red.hgetall(key)
        row[str.encode('gender')] = str.encode(str(random.randint(1, 1000)))
        red.hset(key,  mapping= row)      
    end = time.time()

    print('Redis took ', end-start, ' seconds to update ', N, ' random items')

    print('----------------------------------------------\n')

print('==========================DELETES======================')

for N in (250, 500, 750):
    
    start = time.time()
    for i in range(1,N + 1):
        cursor.execute(delete, [i])
        cnx.commit()
    end = time.time()

    print('Sql took ', end-start, ' seconds to delete ', N, ' items')

    start = time.time()
    for i in range(1,N + 1):
        coll.delete_one({'id': i})
    end = time.time()

    print('MongoDB took ', end-start, ' seconds to delete ', N, ' items')

    start = time.time()
    for i in range(1,N + 1):
        red.delete(i)
    end = time.time()

    print('Redis took ', end-start, ' seconds to delete ', N, ' items')

    print('----------------------------------------------\n')

    A = 1000

    cursor.execute(deleteall)
    cnx.commit()

    for i, rows in enumerate(info):
        cursor.execute(sql, [rows['id'], rows['first_name'], rows['last_name'], rows['email'], rows['gender'], rows['city']])
        cnx.commit()
        if i == A - 1:
            break

    coll.drop()

    coll.insert_many(info[0:A])

    red.flushall()

    for i, rows in enumerate(info):
        red.hset(rows['id'],  mapping={'first_name': rows['first_name'], 'last_name': rows['last_name'], 'email': rows['email'], 'gender': rows['gender'], 'city': rows['city']})
        if i == A - 1:
            break

N = 1000

start = time.time()
cursor.execute(deleteall)
cnx.commit()
end = time.time()

print('Sql took ', end-start, ' seconds to delete ', N, ' items')

start = time.time()
coll.drop()
end = time.time()

print('MongoDB took ', end-start, ' seconds to delete ', N, ' items')

start = time.time()
red.flushall()
end = time.time()

print('Redis took ', end-start, ' seconds to delete ', N, ' items')

print('----------------------------------------------\n')