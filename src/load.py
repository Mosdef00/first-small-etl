from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

def load_to_postgres(df, table_name):
    # Load environment variables from .env file
    load_dotenv()

    # Get database connection details from environment variables
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    # Create a connection string
    connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    # Create a SQLAlchemy engine
    engine = create_engine(connection_string)

    # Load the DataFrame into the PostgreSQL database
    df.to_sql(table_name, engine, if_exists='replace', index=False)