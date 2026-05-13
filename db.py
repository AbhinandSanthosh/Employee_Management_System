import psycopg2

DB_NAME = "company_db"
DB_USER = "postgres"
DB_PASSWORD = "abhinand12"
DB_HOST = "localhost"
DB_PORT = "5432"


def get_connection():

    try:

        connection = psycopg2.connect(
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

        print("Database connected successfully")

        return connection

    except Exception as e:

        print("Database connection failed")
        print("Error:", e)

get_connection()