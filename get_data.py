"""
Query data from a collection
"""
import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
mydb = client['School']
data = mydb.Students

"""
lets get all the data from collection
"""
for learners in data.find({}):
    print(learners)