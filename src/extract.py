import pandas as pd
from log_config import get_logger

# Configurer le logger
logger = get_logger(__name__)

def extract(file_path):
    """
    Extraire les données d'un fichier CSV.
    """
    logger.info(f"Début de l'extraction des données depuis {file_path}")
    try:
        cars = pd.read_csv(file_path)
        logger.info(f"Extraction réussie : {len(cars)} lignes extraites.")
        return cars
    except Exception as e:
        logger.error(f"Erreur lors de l'extraction des données depuis {file_path} : {e}")
        raise

if __name__ == "__main__":
    file_path = 'C:/Users/mouss/first-small-etl/data/input/cars.csv'
    cars = extract(file_path)
    print(cars.head())