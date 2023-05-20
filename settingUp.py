import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
print(myclient.list_database_names())

class inventory:
    def __init__(self):
        pass
    def add(self,itemName):
        pass
    def remove(self, itemName):
        pass
    def edit(self, itemName, newItemName):
        pass
class peopleCounting:
    def __init__(self):
        pass
    #count the ammount of people that were there each day and keep that for each day
    def countPerDay(self):
        pass
