import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def get_tenant_connection():

    return pymysql.connect(
        host="host.docker.internal",
        user=os.getenv("TENANT_DB_USER"),
        password=os.getenv("TENANT_DB_PASSWORD"),
        database="zeus"
    )