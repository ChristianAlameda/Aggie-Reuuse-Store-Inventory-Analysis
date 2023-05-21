from os.path import dirname,realpath
import datetime
import pprint

from database import database

from flask import Flask
from flask import request

app = Flask(__name__)

def addStudentID(id):
    db.insertPosts({
        "StudentID": id,
        "date": datetime.datetime.utcnow()
    })

@app.route("/student", methods=['GET', 'POST'])
def student():
    print(request.method)
    #print(request.form['id'])
    if request.method == 'POST':
        addStudentID(request.form['id'])
        
    return ui

@app.route("/product", methods=['GET', 'POST'])
def product():
    print(request.method)
    #print(request.form['id'])
    if request.method == 'POST':
        db.insertPost({
            "item": request.form["item"],
            "picture": request.form["picture"],
            "qrcode": request.form["qrcode"],
            "addedItemDescription": request.form["addedItemDescirption"]
        })
        
    return ui
        
@app.route("/")
def index():
    return ui

if __name__ == "__main__":
    db = database(username="Aggie", password="Aggie")

    file = open("dashboard.html", "r")
    ui = file.read()
    file.close()

    app.run()