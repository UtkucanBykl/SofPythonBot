from database import Database

db = Database()

qslist = db.List()
search = "What does the “yield” keyword do in Python?"
for question in qslist:
    if question["title"] == search:
        print(question["answer"])
