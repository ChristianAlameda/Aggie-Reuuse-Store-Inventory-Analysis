from database import database
import csv

def main():
    db = database(username="Aggie", password="Aggie")


    allPosts = []
    for post in db.returnPosts():

        try:
            allPosts.append({
                "StudentID":post["StudentID"],
                "date":post["date"]
            })
        except KeyError:
            pass

    data_file = open("stats.csv", "w")
    writer = csv.writer(data_file)

    count = 0

    for value in allPosts:
        if count == 0:
            header = value.keys()
            writer.writerow(header)
            count += 1
        
        writer.writerow(value.values())

    data_file.close()
if __name__ == "__main__":
    main()

