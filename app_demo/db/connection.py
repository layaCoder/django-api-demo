import pymongo
from .dbsetting import connectUrl


class Connection:
    def __init__(self):
        client = pymongo.MongoClient(connectUrl)
        self.client = client['LAYA_BLOG']

    def getConnection(self):
        return self.client

    def closeConnection(self):
        self.client.close()
