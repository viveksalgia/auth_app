from db_conn.db_conn_obj import get_conn_obj

def check_credentials(username, password):
    connection = get_conn_obj()
    cursor = connection.cursor()
    retmsg = cursor.callfunc("adm_users_pkg.validate_credentials", str, [username, password])
    return retmsg