import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017/m")
db = client["courses"]
collection = db["courses"]

with open("courses.json", "r") as f:
    courses = json.load(f)

collection.create_index("name")

for course in courses:
    course['rating'] = {'total': 0, 'count': 0}

for course in courses:
    for chapter in course['chapters']:
        chapter['rating'] = {'total': 0, 'count': 0}

for course in courses:
    collection.insert_one(course)

client.close()
