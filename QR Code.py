import qrcode
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
import string

# Inventory data structure to store the items
inventory = []

# Function to generate a random serial number
def generate_serial_number():
    serial_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return serial_number

# Function to add an item to the inventory
def add_item(name):
    item = {
        'name': name,
        'serial_number': generate_serial_number(),
        'date_added': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    inventory.append(item)
    generate_qr_code(item)

# Function to generate a QR code for an inventory item
def generate_qr_code(item):
    unique_code = f"{item['name']}-{item['serial_number']}-{item['date_added']}"

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )
    qr.add_data(unique_code)
    qr.make(fit=True)
    qr_image = qr.make_image(fill_color='black', back_color='white')

    # Display the QR code
    qr_image.show()

# Gather data from the user to add an item to the inventory
name = input("Enter the item name: ")

# Add the item to the inventory
add_item(name)
