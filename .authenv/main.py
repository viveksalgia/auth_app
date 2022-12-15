import json
from flask import Flask, request
from api_routes.validate_creds import val_cred_api, register_user

app = Flask(__name__)

@app.route('/authenticate', methods = ['POST'])
def val_create_session():
    reqJson = request.get_json(force=True)
    user = reqJson['username']
    passw = reqJson['password']
    return val_cred_api(user, passw)

@app.route('/register', methods = ['POST'])
def reg_user():
    reqJson = request.get_json(force=True)
    user = reqJson['username']
    passw = reqJson['password']
    desc = reqJson['description']
    email = reqJson['emailAddress']
    return register_user(user, passw, desc, email)