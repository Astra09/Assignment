from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
import pymongo
import json
from bson import json_util
myclient = pymongo.MongoClient("mongodb://localhost:27017/")


db = myclient["database_assignment"]
collection = db["assignment_collection"]
app = FastAPI()

@app.get("/courselist")
async def get_course_list():
    res=[]
    for x in collection.find({}):
        res.append(x)
    temp = res
    temp.sort(key=lambda x: (x["name"]))
    temp.sort(key=lambda x: (x["date"]),reverse=True)
    temp.sort(key=lambda x: (x["courseRating"]),reverse=True)
    courseList=[]
    for item in temp:
        courseList.append(item["name"])
    return courseList

@app.get("/overview")
async def get_overview():
    res=[]
    for x in collection.find({}):
        res.append(x)
    overviewList=[]
    for item in res:
        dc = {"Name":item["name"],"Date":item["date"],"Description":item["description"],"Domain":item["domain"],"Chapters":item["chapters"],"Course Rating" : item["courseRating"]}
        overviewList.append(dc)
    return overviewList

@app.get("/chapter/{cname}")
async def get_chapter(cname: str):
    res=[]
    for x in collection.find({}):
        res.append(x)
    chapterInfo=[]
    temp=[]
    for item in res:
        for each in item["chapters"]:
            if(each["name"].lower()==cname.lower()):
                chapterInfo.append(each)
    return chapterInfo

@app.post("/rating/{cname}/{rate}")
async def rate_chapter(cname:str, rate:int):
    res=[]
    for x in collection.find({}):
        res.append(x)
    for item in res:
        for each in item["chapters"]:
            if(each["name"].lower()==cname.lower()):
                item["chapters"][0]["rating"]+=rate
                item["courseRating"]+=rate
                collection.update_one({"_id":item["_id"]},{"$set": item})
            
    return "Rate Successful"
                 
    
