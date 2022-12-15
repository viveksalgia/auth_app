from db_conn.db_validate_credentials import check_credentials
from db_conn.db_register_user import register

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