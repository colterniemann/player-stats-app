import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

def connect():
    try:
        db_params = {
            "host": os.getenv("DB_HOST"),
            "dbname": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "port": os.getenv("DB_PORT"),
        }
        print("Connecting to the postgres database...")
        with psycopg.connect(**db_params) as conn:
            print("Connection successful!")
            return conn
    except Exception as e:
        print(f"Database error: {e}")
        return None
