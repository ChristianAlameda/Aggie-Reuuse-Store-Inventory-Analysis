import settingUp
class Interface:
    def __init__(self):
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
        print(item)
        return item

    
    def add(self, item):
        pass
    def typeOfSelections(self):
        x = 0
        for i in self.selections:
            print('[' +str(x)+ '] - '+i)
            x = x+1