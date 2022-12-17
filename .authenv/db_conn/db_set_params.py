from db_conn.db_conn_obj import get_conn_obj

def set_parameters(sid, name, dataType, value):
    connection = get_conn_obj()
    cursor = connection.cursor()
    retmsg = cursor.var(str)
    cursor.callproc('adm_global.manage_session_params', [sid, name, dataType, value, retmsg])
    return retmsg