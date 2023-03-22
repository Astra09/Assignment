import pymongo
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")


db = myclient["database_assignment"]
collection = db["assignment_collection"]
collection.create_index("name",unique= True)
with open('courses.json') as file:
    file_data = json.load(file)
collection.insert_many(file_data)


