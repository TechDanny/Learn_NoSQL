"""
This file creates a Database called 'Employee' and also add a collection called 'employeeinformation'
"""
import pymongo

client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
mydb = client['Employee']
information = mydb.employeeinformation
records = {
    "firstName": "Danny",
    "lastName": "koki",
    "age": 24,
    "Department": "ICT"
}
information.insert_one(records)