from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json
import datetime
import pprint
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
        self.posts = self.db.posts
        #print(self.db)
    
    def insertPosts(self, post:dict):
        #posts = self.db.posts
        post_id = self.posts.insert_one(post).inserted_id

    def getPost(self, query:dict):
        return self.posts.find_one(query)
    
    def getPosts(self, query:dict):
        return self.posts.find(query)
    
    def printPosts(self):
        for post in self.posts.find():
            pprint.pprint(post)

    def returnPosts(self):
        for post in self.posts.find():
            yield post

    def deletePost(self, query:dict):
        self.posts.delete_one(quary)
    
def main():
    db = database(username="Aggie", password="Aggie")
    db.deletePost({
        "StudentID":"005626665"
    })

    for post in db.returnPosts():
        pprint.pprint(post)

if __name__ == "__main__":
    main()