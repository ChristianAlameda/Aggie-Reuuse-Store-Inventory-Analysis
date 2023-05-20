from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# uri = "mongodb+srv://Aggie:Aggie@Aggie.2ddyt5b.mongodb.net/?retryWrites=true&w=majority"
# # Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))
# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

class database():

    def __init__(self,username,password) -> None:
        uri = "mongodb+srv://<username>:<password>@aggie.2ddyt5b.mongodb.net/?retryWrites=true&w=majority".replace("<password>", password)
        uri = uri.replace("<username>", username)
        # Create a new client and connect to the server
        self.client = MongoClient(uri, server_api=ServerApi('1'))
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)
        self.db = self.client.Aggie
        print(self.db)
    
    def add():
        pass

db = database(username="Aggie", password="Aggie")