"""
get student with the highest gpa
"""
import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
mydb = client['School']
data = mydb.Students

for student in data.find().sort({"gpa": -1}).limit(1):
    print(student)