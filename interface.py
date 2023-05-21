from settingUp import Inventory
import cv2
import time
import os
from QRCODE import QRCODE
#from gridfs import GridFS
class Interface:
    def __init__(self):
        self.Inventory = Inventory()
        
        self.selections = ['Bag/Backpack',
            'belt',
            'Books',
            'Dress',
            'Hat', 
            'Household',
            'Jacket',
            'Long-sleeve/button up',
            'Pants/Jeans', 
            'Ring/Jewelry',
            'School supplies',
            'Shirts',
            'Shoes',
            'Skirt',
            'Sunglasses',
            'Sweater/Carnigan',
            'Tank Top',
            'Tie',
            'Misc'
        ]
    def selector(self):
        self.typeOfSelections()
        selection = int(input('What would you like to add: '))
        
        if selection == 0:
            item = self.selections[0]
        elif selection == 1:
            item = self.selections[1]
        elif selection == 2:
            item = self.selections[2]
        elif selection == 3:
            item = self.selections[3]
        elif selection == 4:
            item = self.selections[4]
        elif selection == 5:
            item = self.selections[5]
        elif selection == 6:
            item = self.selections[6]
        elif selection == 7:
            item = self.selections[7]
        elif selection == 8:
            item = self.selections[8]
        elif selection == 9:
            item = self.selections[9]
        elif selection == 10:
            item = self.selections[10]
        elif selection == 11:
            item = self.selections[11]
        elif selection == 12:
            item = self.selections[12]
        elif selection == 13:
            item = self.selections[13]
        elif selection == 14:
            item = self.selections[14]
        elif selection == 15:
            item = self.selections[15]
        elif selection == 16:
            item = self.selections[16]
        elif selection == 17:
            item = self.selections[17]
        elif selection == 18:
            item = self.selections[18]
        return item
    
    

    
    
    def typeOfSelections(self):
        x = 0
        for i in self.selections:
            print('[' +str(x)+ '] - '+i)
            x = x+1
    def choice(self):
        customerChoice = int(input("Enter [0] - add an item\nEnter [1] - remove an item\nEnter here: "))
        if customerChoice == 0:
            #take a picture call it takePicture
            print('We need a picture of the item')
            camera = cv2.VideoCapture(0)# first camera
            
            input('Press Enter to capture(In 3 seconds)')
            time.sleep(3)
            return_value, image = camera.read()
            cv2.imwrite('opencv'+'.png', image)
            #aws to make it a url
            item = self.selector()
            del(camera)
            qrcode = os.path.join('qrcode.png')
            picture = os.path.join('picture.png')
            itemDescription  = {
                "item" : item,
                "picture" : picture,
                "qrcode": qrcode,
                "addedItemDescription" : input('Write me a description of the item you are adding: ')
            }
            
            self.Inventory.add(itemDescription)
        elif customerChoice == 1:
            item = self.selector()
            self.Inventory.remove(item)