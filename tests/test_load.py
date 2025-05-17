import pytest
import pandas as pd
from sqlalchemy import create_engine, text
from load import load_to_postgres

# Test database connection string
TEST_DATABASE_URL = "postgresql://postgres:woodwar7@localhost:5432/cars_test_db"

@pytest.fixture(scope="module")
def test_db_engine():
    """
    Fixture to provide a test database engine.
    Creates and tears down the test database.
    """
    # Create engine for the test database
    engine = create_engine(TEST_DATABASE_URL)

    # Create a test table
    with engine.connect() as connection:
        connection.execute(text("""
            CREATE TABLE IF NOT EXISTS cars (
                car_model VARCHAR(100),
                transmission VARCHAR(20),
                cyl INT,
                horsepower_hp INT,
                mpg FLOAT,
                engine_shape VARCHAR(20),
                gear INT
            )
        """))
    
    yield engine  # Provide the engine to the test

    # Teardown: Drop the test table
    with engine.connect() as connection:
        connection.execute(text("DROP TABLE IF EXISTS cars"))

def test_load_to_postgres(test_db_engine):
    """
    Test the load_to_postgres function using the test database.
    """
    # Mock data as a pandas DataFrame
    test_data = pd.DataFrame([
        {"car_model": "Mazda RX-4", "transmission": "Manual", "cyl": 6, "horsepower_hp": 110, "mpg": 21.0, "engine_shape": "V-Shaped", "gear": 4},
        {"car_model": "Toyota Corolla", "transmission": "Automatic", "cyl": 4, "horsepower_hp": 65, "mpg": 33.9, "engine_shape": "Straight", "gear": 4},
        {"car_model": "Peugeot 208", "transmission": "Manual", "cyl": 4, "horsepower_hp": 75, "mpg": 45.6, "engine_shape": "Straight", "gear": 5},
    ])

    # Call load_to_postgres with the test database engine
    load_to_postgres(test_data, "cars", test_db_engine)

    # Verify data was inserted
    with test_db_engine.connect() as connection:
        result = connection.execute(text("SELECT * FROM cars"))
        rows = result.fetchall()

        # Convert rows to dictionaries for easier comparison
        columns = ["car_model", "transmission", "cyl", "horsepower_hp", "mpg", "engine_shape", "gear"]
        rows_as_dicts = [dict(zip(columns, row)) for row in rows]

        # Assert the number of rows matches the mock data
        assert len(rows_as_dicts) == len(test_data)

        # Assert the content matches
        for row, expected in zip(rows_as_dicts, test_data.to_dict(orient="records")):
            assert row["car_model"] == expected["car_model"]
            assert row["transmission"] == expected["transmission"]
            assert row["cyl"] == expected["cyl"]
            assert row["horsepower_hp"] == expected["horsepower_hp"]
            assert row["mpg"] == expected["mpg"]
            assert row["engine_shape"] == expected["engine_shape"]
            assert row["gear"] == expected["gear"]