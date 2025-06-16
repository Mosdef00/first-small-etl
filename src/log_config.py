import logging
import os

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log"),  # Save logs to the 'logs' folder
        logging.StreamHandler()               # Print logs to the console
    ]
)

def get_logger(name):
    """
    Returns a logger instance with the specified name.
    """
    return logging.getLogger(name)