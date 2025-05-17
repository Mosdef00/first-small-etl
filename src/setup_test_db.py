import psycopg2
from psycopg2 import sql

# Database connection parameters
DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = "postgres"  
DB_PASSWORD = "woodwar7"  
TEST_DB_NAME = "cars_test_db"

def create_test_database():
    """
    Creates the test database if it does not already exist.
    """
    try:
        # Connect to the PostgreSQL server
        connection = psycopg2.connect(
            dbname="postgres",  # Connect to the default `postgres` database
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        connection.autocommit = True  # Enable autocommit for CREATE DATABASE

        with connection.cursor() as cursor:
            # Check if the test database already exists
            cursor.execute(
                sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"),
                [TEST_DB_NAME]
            )
            exists = cursor.fetchone()

            if not exists:
                # Create the test database
                cursor.execute(
                    sql.SQL("CREATE DATABASE {}").format(
                        sql.Identifier(TEST_DB_NAME)
                    )
                )
                print(f"Test database '{TEST_DB_NAME}' created successfully.")
            else:
                print(f"Test database '{TEST_DB_NAME}' already exists.")
    except psycopg2.Error as e:
        print(f"Error while creating test database: {e}")
        raise
    finally:
        # Close the connection
        if connection:
            connection.close()

if __name__ == "__main__":
    create_test_database()