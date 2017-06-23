from database import Database

db = Database()

qslist = db.List()
search = "How"
for title in qslist:
    if(search in title["title"]):
        print (title["title"])
