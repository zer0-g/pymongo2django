import settings
from pymongo import MongoClient
from pymongo.database import DBRef


def get_DBInstance():

    connStr = userStr = db = None
    
    if settings.user and settings.password:
        userStr = settings.user + ":" + settings.password + "@"
        
    if userStr:
        connStr = 'mongodb://' + userStr + settings.host
    else:
        connStr = 'mongodb://' + settings.host

    if settings.port:
        connStr += ':' + str(settings.port)

    if settings.name:
        connStr += '/' + settings.name
        conn = MongoClient(connStr)
        db = conn[settings.name]

    return db
    
