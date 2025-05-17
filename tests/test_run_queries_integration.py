import pytest
import os
from unittest.mock import patch, MagicMock
from src.run_queries import execute_query_from_file, save_results_to_csv

@patch("src.run_queries.get_engine")
def test_run_queries_integration(mock_get_engine, tmp_path):
    """
    Test the full SQL query execution and result saving workflow.
    """
    # Mock the SQL query result
    mock_engine = MagicMock()
    mock_connection = mock_engine.connect.return_value.__enter__.return_value
    mock_result = MagicMock()
    mock_result.fetchall.return_value = [("Mazda RX-4", 21.0), ("Toyota Corolla", 33.9)]
    mock_result.keys.return_value = ["car_model", "miles_per_gallon_mpg"]
    mock_connection.execute.return_value = mock_result
    mock_get_engine.return_value = mock_engine

    # Mock SQL file content
    sql_file = tmp_path / "test_query.sql"
    sql_file.write_text("SELECT * FROM cars;")

    # Run the query
    results, columns = execute_query_from_file(str(sql_file))

    # Save to CSV
    output_file = tmp_path / "test_query.csv"
    save_results_to_csv(results, columns, str(output_file))

    # Assert the CSV file was created
    assert output_file.exists()

    # Check CSV content
    with open(output_file, "r") as f:
        content = f.read()
        assert "car_model,miles_per_gallon_mpg" in content
        assert "Mazda RX-4,21.0" in content
        assert "Toyota Corolla,33.9" in content