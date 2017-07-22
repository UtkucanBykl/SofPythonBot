from database import Database

db = Database()

qslist = db.List()
search = "How"
print(qslist[0]["title"])
print(qslist[0]["answer"])