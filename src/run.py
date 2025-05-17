import logging
from extract import extract
from transform import transform
from load import load_to_postgres, get_engine

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("etl_pipeline.log"),  # Logs will be saved to this file
        logging.StreamHandler()  # Logs will also be printed to the console
    ]
)

logger = logging.getLogger(__name__)

def run_etl():
    """
    Orchestrates the ETL pipeline: extract, transform, and load.
    """
    logger.info("ETL pipeline started.")

    try:
        # 1. File path for extraction
        file_path = 'C:/Users/mouss/first-small-etl/data/input/cars.csv'

        # 2. Extraction
        logger.info("Starting the extraction process...")
        raw_data = extract(file_path)
        logger.info("Extraction completed successfully.")

        # 3. Transformation
        logger.info("Starting the transformation process...")
        transformed_data = transform(raw_data)
        logger.info("Transformation completed successfully.")

        # 4. Loading
        logger.info("Starting the loading process...")
        engine = get_engine()  # Get the database engine
        load_to_postgres(transformed_data, "cars", engine)  # Pass the engine
        logger.info("Loading completed successfully.")

        logger.info("ETL pipeline finished successfully.")

    except Exception as e:
        logger.error(f"ETL pipeline failed: {e}", exc_info=True)

if __name__ == "__main__":
    run_etl()