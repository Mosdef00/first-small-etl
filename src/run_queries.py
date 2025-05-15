import os
import pandas as pd
from sqlalchemy import text
from load import get_engine

def load_query_from_file(file_path):
    """
    Load an SQL query from a file.
    """
    with open(file_path, 'r') as file:
        return file.read()

def execute_query_from_file(file_path):
    """
    Load and execute an SQL query from a file.
    """
    try:
        # Get the database engine
        engine = get_engine()

        # Load the query from the file
        query = load_query_from_file(file_path)

        # Execute the query
        with engine.connect() as connection:
            result = connection.execute(text(query))
            # Fetch all results and convert to list of rows
            data = result.fetchall()
            # Get column names
            columns = result.keys()
            return data, columns

    except Exception as e:
        print(f"Error executing query from {file_path}: {e}")
        return None, None

def save_results_to_csv(data, columns, output_file):
    """
    Save query results to a CSV file.
    """
    if data and columns:
        df = pd.DataFrame(data, columns=columns)
        df.to_csv(output_file, index=False)
        print(f"Results saved to {output_file}")
    else:
        print(f"No results to save for {output_file}")

if __name__ == "__main__":
    # Define the folder containing SQL files
    sql_folder = "C:/Users/mouss/first-small-etl/data/sql"

    # Create an output folder for CSV files if it doesn't exist
    output_folder = "query_results"
    os.makedirs(output_folder, exist_ok=True)

    # List all SQL files in the folder
    sql_files = [os.path.join(sql_folder, f) for f in os.listdir(sql_folder) if f.endswith('.sql')]

    # Execute each SQL file and save results
    for sql_file in sql_files:
        print(f"Running query from {sql_file}...")
        results, columns = execute_query_from_file(sql_file)

        # Generate output file name based on the SQL file name
        output_file = os.path.join(output_folder, os.path.basename(sql_file).replace('.sql', '.csv'))

        # Save the results to CSV
        save_results_to_csv(results, columns, output_file)