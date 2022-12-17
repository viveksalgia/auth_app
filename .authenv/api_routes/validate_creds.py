from db_conn.db_validate_credentials import check_credentials
from db_conn.db_register_user import register
from db_conn.db_create_session import init
from db_conn.db_set_params import set_parameters

def val_cred_api(username, password):
    retmsg = check_credentials(username, password)
    retstr = ''

    if retmsg == 'SUCCESS':
        retstr = {"retcode" : "SUCCESS", "retmsg" : "User validated successfully!!"}
    else:
        retstr = {"retcode" : "ERROR", "retmsg" : "Invalid credentials. Please check the username or password."}

    return retstr

def register_user(username, password, description, email_address):
    retmsg = register(username, password, description, email_address)
    return retmsg

def init_session(username, machine):
    sessionId = init(username, machine)
    retstr = {"sessionId" : str(sessionId)}
    return retstr

def set_params(sid, name, dataType, value):
    retval = set_parameters(sid, name, dataType, value)
    retstr = {"name" : name, "status" : retval.getvalue()}
    return retstr