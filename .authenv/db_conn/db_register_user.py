from db_conn.db_conn_obj import get_conn_obj

def register(username, password, description, email_address):
    connection = get_conn_obj()
    cursor = connection.cursor()
    retcode = cursor.var(int)
    retmsg = cursor.var(str)
    cursor.callproc('adm_users_pkg.create_user', [retcode, retmsg, username, password, 'Y', description, email_address])
    plsqlretcode = retcode.getvalue()
    plsqlretmsg = retmsg.getvalue()
    return {"ReturnCode":plsqlretcode, "ReturnMsg":plsqlretmsg}