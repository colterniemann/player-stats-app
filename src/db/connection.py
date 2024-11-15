import psycopg
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseConnection:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            db_params = {
                "host": os.getenv("DB_HOST"),
                "dbname": os.getenv("DB_NAME"),
                "user": os.getenv("DB_USER"),
                "password": os.getenv("DB_PASSWORD"),
                "port": os.getenv("DB_PORT"),
            }
            print("Connecting to the postgres database...")
            self.conn = psycopg.connect(**db_params)
            self.conn.autocommit = False
            print("Connection successful!")
        except Exception as e:
            print(f"Database error: {e}")
            self.conn = None

    def close(self):
        if self.conn:
            self.conn.close()
            print("Connection closed.")

    def get_connection(self):
        return self.conn
