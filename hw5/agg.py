__author__ = 'cifer'
import pymongo
connection = pymongo.MongoClient()
db = connection.states

result = db.zips.aggregate([{"$group": {"_id": "$state", "population": {"$sum": "$pop"}}}])
for doc in result:
    print doc
