import code
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
import string
# Gather data from the user to add an item to the inventory
name = input("Enter the item name: ")

# Add the item to the inventory

class QR_CODE:
    def __init__(self):
        
    # Inventory data structure to store the items
        self.inventory = []

    # Function to generate a random serial number
    def generate_serial_number(self):
        serial_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        return serial_number

    # Function to add an item to the inventory
    def add_item(self):
        item = {
            'name': name,
            'serial_number': self.generate_serial_number(),
            'date_added': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.inventory.append(item)
        

    # Function to generate a QR code for an inventory item
    
        unique_code = f"{item['name']}-{item['serial_number']}-{item['date_added']}"

        qr = code.QRCode(
            version=1,
            box_size=10,
            border=5
        )
        qr.add_data(unique_code)
        qr.make(fit=True)
        qr_image = qr.make_image(fill_color='black', back_color='white')

        # Display the QR code
        qr_image.show()