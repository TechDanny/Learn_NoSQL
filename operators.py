"""
Using operators to access data
"""
import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
mydb = client['School']
data = mydb.Students

"""
using less than or equal to retrieve data
"""
print("=====Printing data that age is less than or Equal to 25=====")
for learners in data.find({"Age": {"$lte": 25}}):
    print(learners)

"""
using great than to retriev data
"""

print("=====Printing data that age greater that 25=====")
for learners in data.find({"Age": {"$gt": 25}}):
    print(learners)

"""
using the and operator to access data
"""

print("using 'and' operator to access data that is in both")

for learners in data.find({"$and": [{"name": "Spongebob"}, {"Age": 23}]}):
    print(learners)

"""
Using the 'or' Operator
"""

print("using 'or' operator to access either of the data")

for learners in data.find({"$or": [{"name": "Spongebob"}, {"Age": 25}]}):
    print(learners)
