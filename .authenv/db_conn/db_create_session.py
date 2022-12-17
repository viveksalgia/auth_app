from db_conn.db_conn_obj import get_conn_obj

def init(username, machine):
    try:
        connection = get_conn_obj()
        cursor = connection.cursor()
        cur = connection.cursor()
        try:
            cursor.execute('select user_id from adm_users where user_name = :1', [username.upper()])
            row = cursor.fetchone()
            userId = row[0]
        except Exception as e:
            print('Exception while getting userid - ' + str(e))
        finally:
            cursor.close()

        sessionId = cur.var(int)
        cur.callproc('adm_global.create_web_session', [userId, machine, sessionId])
    except Exception as err:
        print('Exception encountered - ' + str(err))
    finally:
        cur.close()
        return sessionId.getvalue()