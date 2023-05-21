
import datetime
from Problem2.database import database
class Inventory:
    def __init__(self):
        self.db = database(username="Aggie", password="Aggie")
    
    def add(self,itemName): #uses insertPosts(self, post:dict):
        return self.db.insertPosts(itemName)
        
    def remove(self, itemName): #uses def deletePost(self, query:dict)
        return self.db.deletePost(itemName)
    
    def edit(self, itemName, newItemName):
        pass
    
class peopleCounting:
    def __init__(self):
        pass
    
    #count the ammount of people that were there each day and keep that for each day
    def countPerDay(self):
        pass
