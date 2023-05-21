# inventory tracking
1. take the type of item
1.1 ask for why a description of the item
2. take a picture of the item
3. the date the item came in will be there
4. QR code will be assigned to that item


# database.py

### Connecting to the database
- Initialize the database object and set the username and password for the database
```
db = database(username="Aggie", password="Aggie)
```

### insertPost(post:dict)
- Insets a new post into the dictinary
    - Post must be a dictionary

```
db.insertDocument({
        "StudentID":studentID,
        "datetime":datetime.datetime.utcnow()  
    })
```

### deletePost(query:dict)
- Deletes a post from the database
    - Quary must be a ditionary, corresponding to a post in the database

```
 db.deletePost({
        "StudentID":"005626665"
    })

```

### getPost(query:dict)
- Returns a post corresponding to the inputed quary
```
db.getPost({
    "StudentID":"006"
})
```

### returnPosts()
- A generator so you can iterate over all posts in the dictionary
```
for post in db.returnPosts():
    pprint.pprint(post)

```
