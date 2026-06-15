import pymysql

def connect_client(db_name, db_user, db_password):

    return pymysql.connect(
        host="host.docker.internal",
        user=db_user,
        password=db_password,
        database=db_name
    )