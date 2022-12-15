import json
import os
import cx_Oracle

def create_conn(credentials):
    try:
        # Establish the database connection
        connection = cx_Oracle.connect(user=credentials["oracledbuser"], password=credentials["oracledbpass"],
                               dsn=credentials["oracledbhost"] + ":" + credentials["oracledbport"] + "/" + credentials["oracledbservice"])
    except Exception as err:
        print("Error while creating Oracle DB connection" + str(err))
    finally:
        return connection

def get_conn_obj():
    try:
        connection = object()
        if os.getenv("AUTH_CREDENTIALS") is None:
            print("Please set environment variable AUTH_CREDENTIALS to the auth_config.json file absolute path")
            raise Exception("Please set environment variable AUTH_CREDENTIALS to the auth_config.json file absolute path")
        else:
            try:
                file = open(os.getenv("AUTH_CREDENTIALS"), "r")
                line = file.readline()
                credentials = json.loads(line)
                connection = create_conn(credentials)
            except Exception as err:
                print("Exception while reading the config file " + str(err))
            finally:
                file.close()
    except Exception as err:
        print("Exception occurred " + str(err))
    finally:
        return connection
