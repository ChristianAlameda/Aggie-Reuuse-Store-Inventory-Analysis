import qrcode
import random
class QRCODE:
    def createQRCODE():
        # Data to be encoded
        data = random.randint(1,1000000)
        
        # Encoding data using make() function
        img = qrcode.make(data)
        
        # Saving as an image file
        img.save('qrcode.png')