import pymongo


client = pymongo.MongoClient("url")
db = client.URLshorten
URLcollection = db.URLs

def addURL(dict):
    _id = URLcollection.insert_one(dict).inserted_id
    return _id

def redirectURL(ID):
    return URLcollection.find_one({"URLid":str(ID)})

