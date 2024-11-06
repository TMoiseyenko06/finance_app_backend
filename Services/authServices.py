import pymongo
from werkzeug.security import generate_password_hash, check_password_hash
from flask import jsonify
from utils.util import encode_token
from database import db

accounts_collection = db['accounts']



def register(user_data):
    if accounts_collection.count_documents({'username':user_data['username']}, limit = 1) == 0:
        new_account = {
            "username":user_data['username'],
            "password":generate_password_hash(user_data['password'])
        }
        accounts_collection.insert_one(new_account)
        return jsonify({"status":"OK",
                        "message":"User Register"    
                        }),201
    else:
        return jsonify({"error":"username already exists"}), 400

def login(user_data):
    if accounts_collection.count_documents({"username":user_data['username']}, limit = 1 ) != 0:
        user = accounts_collection.find_one({"username": user_data['username']})
        if user is None:
           return jsonify({"status": "Error", "message": "Invalid username or password"}), 400
        if not check_password_hash(user['password'], user_data['password']):
            return jsonify({"status": "Error", "message": "Invalid username or password"}), 400
        user_id = user['_id']
        return jsonify({
            "status":"OK",
            "auth_token":encode_token(user_id)
                        }),200
