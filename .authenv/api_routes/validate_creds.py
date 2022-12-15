from db_conn.db_validate_credentials import check_credentials
import json

def val_cred_api(username, password):
    retmsg = check_credentials(username, password)
    retstr = ''

    if retmsg == 'SUCCESS':
        retstr = {"retcode" : "SUCCESS", "retmsg" : "User validated successfully!!"}
    else:
        retstr = {"retcode" : "ERROR", "retmsg" : "Invalid credentials. Please check the username or password."}

    return retstr
