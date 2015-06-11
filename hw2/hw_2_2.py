from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import pymongo
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.students
grades = db.grades
count = 0
ids = []
for grade in grades.find({'type': 'homework'}).sort([
    ('student_id', pymongo.ASCENDING),
    ('score', pymongo.ASCENDING),
]):
    print(grade)
    count += 1
    if count == 2:
        count = 0
        continue
    else:
        ids.append(grade['_id'])

for _id in ids:
    db.grades.delete_one({'_id': _id})
