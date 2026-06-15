from config.tenant_connection import get_tenant_connection


def get_clients():

    connection = get_tenant_connection()

    try:

        cursor = connection.cursor()

        sql = """

        SELECT name, db_name, db_user,db_password
        FROM clients

        """

        cursor.execute(sql)

        return cursor.fetchall()

    finally:

        connection.close()