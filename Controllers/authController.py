from middleware.schemas.authSchemas import user_auth_schema
from flask import request, jsonify
from marshmallow import ValidationError
from Services import authServices

def register():
    try:
        user_data = user_auth_schema.load(request.json)
        return authServices.register(user_data)
    except ValidationError as e:
        return jsonify(e.messages)

def login():
    try:
        login_data = user_auth_schema.load(request.json)
        return authServices.login(login_data)
    except ValidationError as e:
        return jsonify(e.messages)