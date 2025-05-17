import psycopg2

try:
    connection = psycopg2.connect(
        dbname="cars_test_db",
        user="postgres",
        password="woodwar7",
        host="localhost",
        port="5432"
    )
    print("Connection successful!")
    connection.close()
except Exception as e:
    print(f"Connection failed: {e}")