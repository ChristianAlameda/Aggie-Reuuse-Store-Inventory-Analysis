from database import database

def main():
    db = database(username="Aggie", password="Aggie")


    allPosts = []
    for post in db.returnPosts():
        allPosts.append({
            "StudentID":post["StudentID"],
            "date":post["date"]
        })

if __name__ == "__main__":
    main()

