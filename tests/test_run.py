import pytest
from unittest.mock import patch, MagicMock
from src.run import run_etl


@patch("src.run.get_engine")
@patch("src.run.extract")
@patch("src.run.transform")
@patch("src.run.load_to_postgres")
def test_run_etl(mock_load_to_postgres, mock_transform, mock_extract, mock_get_engine):
    """
    Integration test for the run_etl function to ensure the ETL pipeline works end-to-end.
    """
    # Mock the extract function to simulate raw data
    mock_raw_data = MagicMock(name="raw_data")
    mock_extract.return_value = mock_raw_data

    # Mock the transform function to simulate transformed data
    mock_transformed_data = MagicMock(name="transformed_data")
    mock_transform.return_value = mock_transformed_data

    # Mock the get_engine function to simulate a database engine
    mock_engine = MagicMock(name="engine")
    mock_get_engine.return_value = mock_engine

    # Mock the load_to_postgres so it doesn't actually connect to a database
    mock_load_to_postgres.return_value = None

    # Run the ETL process
    run_etl()

    # Assert that extract was called exactly once
    mock_extract.assert_called_once()

    # Assert that transform was called with the raw data returned by extract
    mock_transform.assert_called_once_with(mock_raw_data)

    # Assert that load_to_postgres was called with the transformed data, the correct table name, and the mocked engine
    mock_load_to_postgres.assert_called_once_with(mock_transformed_data, "cars", mock_engine)