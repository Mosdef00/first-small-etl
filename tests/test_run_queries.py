import pytest
import pandas as pd
from unittest.mock import patch, mock_open, MagicMock
from src.run_queries import load_query_from_file, execute_query_from_file, save_results_to_csv

def test_load_query_from_file():
    """
    Test loading an SQL query from a file.
    """
    # Mock file content
    mock_query = "SELECT * FROM cars;"
    
    # Patch the built-in open function
    with patch("builtins.open", mock_open(read_data=mock_query)):
        # Call the function
        query = load_query_from_file("mock_file.sql")

    # Assert the query was loaded correctly
    assert query == mock_query

@patch("src.run_queries.get_engine")
@patch("src.run_queries.load_query_from_file")
def test_execute_query_from_file(mock_load_query, mock_get_engine):
    """
    Test executing an SQL query from a file.
    """
    # Mock the SQL query
    mock_query = "SELECT * FROM cars;"
    mock_load_query.return_value = mock_query

    # Mock the database engine and connection
    mock_engine = MagicMock()
    mock_connection = mock_engine.connect.return_value.__enter__.return_value
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [("Mazda RX-4", 21.0), ("Toyota Corolla", 33.9)]
    mock_result.keys.return_value = ["car_model", "miles_per_gallon_mpg"]
    mock_connection.execute.return_value = mock_result
    mock_get_engine.return_value = mock_engine

    # Call the function
    results, columns = execute_query_from_file("mock_file.sql")

    # Assert the query was executed and returned the expected results
    mock_load_query.assert_called_once_with("mock_file.sql")
    mock_connection.execute.assert_called_once()
    assert results == [("Mazda RX-4", 21.0), ("Toyota Corolla", 33.9)]
    assert columns == ["car_model", "miles_per_gallon_mpg"]

@patch("pandas.DataFrame.to_csv")
def test_save_results_to_csv(mock_to_csv):
    """
    Test saving query results to a CSV file.
    """
    # Mock data and columns
    data = [("Mazda RX-4", 21.0), ("Toyota Corolla", 33.9)]
    columns = ["car_model", "miles_per_gallon_mpg"]
    output_file = "output.csv"

    # Call the function
    save_results_to_csv(data, columns, output_file)

    # Assert the DataFrame was saved to a CSV file
    mock_to_csv.assert_called_once()
    args, kwargs = mock_to_csv.call_args
    assert args[0] == output_file
    assert kwargs["index"] is False