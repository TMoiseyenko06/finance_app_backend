import pymongo
from werkzeug.security import generate_password_hash
from flask import jsonify
from utils.util import encode_token

cluster = pymongo.MongoClient('mongodb://localhost:27017/')
db = cluster['finance_db']
accounts_collection = db['accounts']

def register(user_data):
    if accounts_collection.count_documents({'username':user_data['username']}, limit = 1):
        new_account = {
            "username":user_data['username'],
            "password":generate_password_hash(user_data['password'])
        }
        accounts_collection.insert_one(new_account)
        return jsonify({"status":"OK",
                        "message":"User Register"    
                        }),201
    else:
        return jsonify({"error":"username already exists"})

def login(user_data):
    if accounts_collection.count_documents({"username":user_data['username']}, limit = 1 ):
        user = accounts_collection.find({"username":user_data['username'],"password":generate_password_hash(user_data['password'])})
        user_id = user['_id']
        return jsonify({
            "status":"OK",
            "auth_token":encode_token(user_id)
                        }),200
