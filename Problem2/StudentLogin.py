from database import database
import datetime

db = database(username="Aggie", password="Aggie")

studentID = input("Input ID: ")
db.insertDocument({
    "StudentID":studentID,
    "datetime":datetime.datetime.utcnow()  
})