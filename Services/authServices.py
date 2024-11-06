import pymongo
from werkzeug.security import generate_password_hash

cluster = pymongo.MongoClient('mongodb://localhost:27017/')
db = cluster['finance_db']
accounts_collection = db['accounts']

def register(user_data):
    new_account = {
        "username":user_data['username'],
        "password":generate_password_hash(user_data['password'])
    }
    accounts_collection.insert_one(new_account)

def login(user_data):
    user = accounts_collection.find_one({"username":user_data['username'],"password":generate_password_hash(user_data['password'])})
    if user:
        print(user['_id'])