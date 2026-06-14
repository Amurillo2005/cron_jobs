import schedule
import time
from datetime import datetime

from tenant_service import get_clients
from client_connection import connect_client
from test_ranking import ranking_general
from test_ranking import ranking_week

get_clients_db = get_clients()
client_index = 0

def process_all_clients():

    global client_index


    client = get_clients_db[client_index]
    connection = None

    try:
        name = client[0]
        db_name = client[1]
        db_user = client[2]
        db_password = client[3]

        print(f"Procesando {name} Hora inicio: {datetime.now()}")

        connection = (connect_client(db_name,db_user,db_password))

        ranking_general(connection)

        ranking_week(connection)

        print(f"Conexión con {name} terminada Hora fin: {datetime.now()}")

    except Exception as e:

        print(f"Error en {name}: {e}")

    finally:

        if connection:
            connection.close()

    client_index = (client_index + 1) % len(get_clients_db)
    print(f"------------------------------")

process_all_clients()

schedule.every(1).minutes.do(process_all_clients)


while True:

    schedule.run_pending()

    time.sleep(1)