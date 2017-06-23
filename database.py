from pymongo import MongoClient

class Database():

    def __init__(self):
        self.__client = MongoClient("localhost", 27017)
        self.__db = self.__client["webcrawlerr"]
        self.__collection = self.__db["webcrawlerrcollection"]

    def Insert(self, question):
        if (self.__collection.find_one({"title":question["title"]})):
            return False
        try:
            self.__collection.insert(question)
            return True
        except:
            return False

    def List(self):

        myresult = list(self.__collection.find())
        return myresult