from pymongo import MongoClient

class Database():

    def __init__(self):
        self.__client = MongoClient("localhost", 27017)
        self.__db = self.__client["crawlerrrrrr"]
        self.__collection = self.__db["crawlerrrrrrrrcollection"]

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

    def ReturnAnswer(self, question):

        myresult = list(self.__collection.find())
        for i in range(len(myresult)):
            a = myresult[i]["title"]
            try:
                question = question.replace("\n","")
                if(a == question):
                    try:
                        return str(myresult[i]["answer"])
                    except:
                        return "Err"
            except:
                pass
        return "Böyle bir konu yok cınım"