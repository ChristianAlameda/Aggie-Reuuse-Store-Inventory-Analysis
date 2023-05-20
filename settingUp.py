
import datetime
import Problem2.database
class Inventory:
    def __init__(self):
        pass
    
    def add(self,itemName):
        return Problem2.database.insertDocument(self,itemName)
        
    def remove(self, itemName):
        return Problem2.database.deletePost(itemName)
    
    def edit(self, itemName, newItemName):
        pass
    
class peopleCounting:
    def __init__(self):
        pass
    
    #count the ammount of people that were there each day and keep that for each day
    def countPerDay(self):
        pass
