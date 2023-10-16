from pymongo import MongoClient
import os

connection_string = os.environ.get("CONNECTION_STRING")

client = MongoClient(connection_string) 

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client.emaildb

users = db.users


print(list(users.find()))
