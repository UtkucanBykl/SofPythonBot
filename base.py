from database import Database

db = Database()

qslist = db.List()
search = "How"
for title in qslist:
    print (title["content"])
    print((title["answer"]))
    break