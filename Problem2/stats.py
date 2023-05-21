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

    data_file = open("IDs.csv", "w")
    writer = csv.writer(data_file)

    allPosts2 = []
    for post in db.returnPosts():
        try:
            allPosts2.append({
                "item": post["item"],
                "picture": post["picture"],
                "qrcode": post["qrcode"],
                "addedItemDescription": post["addedItemDescription"]
            })
        except KeyError:
            pass

    data_file2 = open("Products.csv", "w")
    writer2 = csv.writer(data_file2)

    count = 0

    for value in allPosts:
        if count == 0:
            header = value.keys()
            writer.writerow(header)
            count += 1
        
        writer.writerow(value.values())

    data_file.close()

    count2 = 0

    for value in allPosts2:
        if count2 == 0:
            header = value.keys()
            writer2.writerow(header)
            count2 += 1
        
        writer2.writerow(value.values())

    data_file2.close()
if __name__ == "__main__":
    main()

