import os
import logging
import pandas as pd
from sqlalchemy import text
from load import get_engine

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("run_queries.log"),  # Save logs to a file
        logging.StreamHandler()  # Print logs to the console
    ]
)

logger = logging.getLogger(__name__)

def load_query_from_file(file_path):
    """
    Load an SQL query from a file.
    """
    try:
        with open(file_path, 'r') as file:
            query = file.read()
            logger.info(f"Successfully loaded query from {file_path}")
            return query
    except Exception as e:
        logger.error(f"Error loading query from {file_path}: {e}", exc_info=True)
        raise

def execute_query_from_file(file_path):
    """
    Load and execute an SQL query from a file.
    """
    try:
        # Get the database engine
        engine = get_engine()
        logger.info("Database engine created successfully.")

        # Load the query from the file
        query = load_query_from_file(file_path)

        # Execute the query
        with engine.connect() as connection:
            logger.info(f"Executing query from {file_path}...")
            result = connection.execute(text(query))
            # Fetch all results and convert to list of rows
            data = result.fetchall()
            # Get column names
            columns = result.keys()
            logger.info(f"Query executed successfully from {file_path}. Number of rows fetched: {len(data)}")
            return data, columns

    except Exception as e:
        logger.error(f"Error executing query from {file_path}: {e}", exc_info=True)
        return None, None

def save_results_to_csv(data, columns, output_file):
    """
    Save query results to a CSV file.
    """
    try:
        if data and columns:
            df = pd.DataFrame(data, columns=columns)
            df.to_csv(output_file, index=False)
            logger.info(f"Results saved to {output_file}")
        else:
            logger.warning(f"No results to save for {output_file}")
    except Exception as e:
        logger.error(f"Error saving results to {output_file}: {e}", exc_info=True)
        raise

if __name__ == "__main__":
    # Define the folder containing SQL files
    sql_folder = "C:/Users/mouss/first-small-etl/data/sql"

    # Create an output folder for CSV files if it doesn't exist
    output_folder = "query_results"
    os.makedirs(output_folder, exist_ok=True)
    logger.info(f"Output folder '{output_folder}' created or already exists.")

    # List all SQL files in the folder
    sql_files = [os.path.join(sql_folder, f) for f in os.listdir(sql_folder) if f.endswith('.sql')]
    logger.info(f"Found {len(sql_files)} SQL files in '{sql_folder}'.")

    # Execute each SQL file and save results
    for sql_file in sql_files:
        logger.info(f"Running query from {sql_file}...")
        results, columns = execute_query_from_file(sql_file)

        # Generate output file name based on the SQL file name
        output_file = os.path.join(output_folder, os.path.basename(sql_file).replace('.sql', '.csv'))

        # Save the results to CSV
        save_results_to_csv(results, columns, output_file)