from database import database
import datetime
import pprint

def main():
    db = database(username="Aggie", password="Aggie")
    for post in db.returnPosts():
        pprint.pprint(post)
    studentID = input("Input ID: ")
    db.insertDocument({
        "StudentID":studentID,
        "datetime":datetime.datetime.utcnow()  
    })

if __name__ == "__main__":
    main()

