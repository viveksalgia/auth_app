from flask import Flask, request, make_response
from api_routes.validate_creds import val_cred_api, register_user, init_session, set_params


app = Flask(__name__)

@app.route('/authenticate', methods = ['POST'])
def val_create_session():
    reqJson = request.get_json(force=True)
    user = reqJson['username']
    passw = reqJson['password']
    return val_cred_api(user, passw)

@app.route('/register', methods = ['POST'])
def reg_user():
    if request.authorization:
        user = request.authorization.username
        passw = request.authorization.password
        retstr = val_cred_api(user, passw)
        if retstr['retcode'] == 'SUCCESS':
            reqJson = request.get_json(force=True)
            user = reqJson['username']
            passw = reqJson['password']
            desc = reqJson['description']
            email = reqJson['emailAddress']
            return register_user(user, passw, desc, email)
        else:
            return make_response('Unable to authenticate', 401)
    else:
        return make_response('Unable to authenticate', 401)

@app.route('/initsession', methods = ['POST'])
def initialize_session():
    if request.authorization:
        user = request.authorization.username
        passw = request.authorization.password
        retstr = val_cred_api(user, passw)
        if retstr['retcode'] == 'SUCCESS':
            reqJson = request.get_json(force=True)
            user = reqJson['username']
            machine = reqJson['machine']
            return init_session(user, machine)
        else:
            return make_response('Unable to authenticate', 401)
    else:
        return make_response('Unable to authenticate', 401)

@app.route('/setssnparams', methods = ['POST'])
def session_params():
    if request.authorization:
        user = request.authorization.username
        passw = request.authorization.password
        retstr = val_cred_api(user, passw)
        if retstr['retcode'] == 'SUCCESS':
            reqJson = request.get_json(force=True)
            finalRetVal = {}
            finalRetList = []
            for j in reqJson['parameters']:
                sid = j['sessionId']
                name = j['name']
                dataType = j['dataType']
                value = j['value']
                retVal = set_params(sid, name, dataType, value)
                finalRetList.append(retVal)
            finalRetVal = {"parameters" : finalRetList}
            return finalRetVal
        else:
            return make_response('Unable to authenticate', 401)
    else:
        return make_response('Unable to authenticate', 401)

@app.route('/')
def root():
    return '<!DOCTYPE html> <html> <head> <title>Networx API Server</title> </head> <body> <div> <p>Welcome to the API Server</p> </div> </body> </html>'

if __name__ == '__main__':
    app.run(host='0.0.0.0')