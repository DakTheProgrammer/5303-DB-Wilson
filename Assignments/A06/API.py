from fastapi import FastAPI
from fastapi.params import Query
import pymongo
from typing import List
from pydantic import BaseModel

class Point(BaseModel):
    x: float
    y: float

cnx = pymongo.MongoClient('mongodb://167.99.6.44:27017')
db = cnx['PlacesToEat']
coll = db['dine']

app = FastAPI()

@app.get('/')
async def root():
    url = 'http://167.99.6.44:8003/'
    routes = ['allRestaurants', 'allRestaurants/<int> pages(0-25)', 'uniqueCategories', 'category/<STRING> category', 'zip/<LIST <STRING>> [zipcodes]', 'near/<POINT <FLOAT>> (x,y)', 'minRating/<INT> rating 0-90']
    examples = [url + 'allRestaurants', url + 'allRestaurants/12', url + 'uniqueCategories', url + 'category/Delicatessen', url + 'zip/?zips=10065&zips=10024&zips=10308', url + 'near/{x: -73.9814868, y: 40.6746454}', url + 'minRating/65']

    return{'Routes' : routes, 'Examples' : examples}


@app.get('/allRestaurants')
async def allRestaurants():
    query = list(coll.find({},{'_id':0}).limit(1000))

    res = {'result': query, 'count': len(query)}

    return{'response': res}

@app.get('/allRestaurants/{page}')
async def allRestaurantsPage(page: int):
    query = list(coll.find({},{'_id':0}).skip(page * 1000).limit(1000))

    res = {'result': query, 'count': len(query)}

    return{'response': res}

@app.get('/uniqueCategories')
async def uniqueCategories():
    query = list(coll.distinct('cuisine'))

    res = {'result': query, 'count': len(query)}

    return{'response': res}

@app.get('/category/{cat}')
async def category(cat: str):
    query = list(coll.find({'cuisine': cat},{'_id':0}))

    res = {'result': query, 'count': len(query)}

    return{'response': res}

@app.get('/zip/')
async def zip(zips: List[str] = Query(None)):
    query = list(coll.find({'address.zipcode': {'$in': zips}},{'_id': 0}).limit(1000))

    res = {'result': query, 'count': len(query)}

    return{'response': res}

@app.get('/near/')
async def near(grid: Point):
    query = list(coll.find({'location':{ '$near':{'$geometry': { 'type': "Point",  'coordinates': [ grid.x, grid.y ] },'$minDistance': 0,'$maxDistance': 1000}}},{'_id': 0}).limit(1000))

    res = {'result': query, 'count': len(query)}

    return{'result': res}

@app.get('/minRating/{rate}')
async def minRating(rate: int):
    query = list(coll.find({'grades.0.score': {'$gte': rate}},{'_id': 0, 'grades': {'$slice': 1}}))

    res = {'result': query, 'count': len(query)}

    return{'response': res}