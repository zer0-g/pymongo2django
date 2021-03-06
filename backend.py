import settings
from pymongo import MongoClient,MongoReplicaSetClient
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


def get_ReplicaDB():

    db = None
    
    if settings.hosts !=[] and settings.replicaName:
        hostStr = ','.join(settings.hosts)
        conn = MongoReplicaSetClient(hostStr,replicaSet=settings.replicaName)
        db = conn[settings.name]

    return db


class Document(object):
    db = None
    objects =None
    name = 'test' #default value for collection name

    def __init__(self):
        self.db = get_DBInstance()
        self.objects = self.db[self.db.name]

    def setName(self,name):
        self.name=name
        self.objects = self.db[name]


class DocumentSet(object):
    db = None
    objects =None
    name = 'test' #default value for collection name

    def __init__(self):
        self.db = get_ReplicaDB()
        self.objects = self.db[self.db.name]

    def setName(self,name):
        self.name=name
        self.objects = self.db[name]
        
