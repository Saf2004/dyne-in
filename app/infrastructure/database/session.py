import os
from dotenv import load_dotenv
import psycopg2

load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        user=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('POSTGRES_HOST'),
        port=os.getenv('POSTGRES_PORT'),
        database=os.getenv('POSTGRES_DB')
    )
