from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.school
students = db.students.find()
count = 0
ids = []
for student in students:
    student_scores = [scores['score'] for scores in student['scores'] if scores['type'] == 'homework']
    if len(student_scores) > 1:
        student_min_homework_score = min(student_scores)
        db.students.update({'_id': student['_id']},
                        {'$pull': {'scores': {'type': 'homework', 'score': student_min_homework_score}}})
