from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

def get_engine():
    """
    Create and return a SQLAlchemy engine using environment variables.
    """
    # Get database connection details from environment variables
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    # Create a connection string
    connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    # Create and return a SQLAlchemy engine
    return create_engine(connection_string)

def load_to_postgres(df, table_name):
    """
    Load a DataFrame into a PostgreSQL table using SQLAlchemy.
    """
    # Get the engine
    engine = get_engine()

    # Load the DataFrame into the PostgreSQL database
    df.to_sql(table_name, engine, if_exists='replace', index=False)