import pandas as pd
import numpy as np
from log_config import get_logger

# Configurer le logger
logger = get_logger(__name__)

def transform(cars):
    """
    Transformer les données extraites en appliquant des nettoyages et des modifications.
    """
    logger.info("Début de la transformation des données.")
    try:
        # Renommer les colonnes
        cars = cars.rename(columns={
            'Unnamed: 0': 'car_model',
            'am': 'transmission',
            'cyl': 'cylinders',
            "hp": "horsepower_hp",
            "mpg": "miles_per_gallon_mpg",
            'vs': 'engine_shape',
            'gear': 'gears'
        })
        logger.info("Renommage des colonnes effectué avec succès.")

        # Nettoyage des valeurs
        cars['car_model'] = cars['car_model'].replace({
            'Mazda RX4': 'Mazda RX-4',
            'Mazda RX4 Wag': 'Mazda RX-4 Wag',
            'Valiant': 'Plymouth Valiant',
            'Camaro Z28': 'Chevrolet Camaro Z28'
        }, regex=True)
        cars['car_model'] = cars['car_model'].str.replace(r'\bHornet\b', 'AMC Hornet', regex=True)
        cars['car_model'] = cars['car_model'].str.replace(r'\bMerc\b', 'Mercedes', regex=True)
        cars['transmission'] = cars['transmission'].replace({0: 'Automatic', 1: 'Manual'})
        cars['engine_shape'] = cars['engine_shape'].replace({0: 'V-Shaped', 1: 'Straight'})
        logger.info("Nettoyage des valeurs effectué avec succès.")

        return cars
    except Exception as e:
        logger.error(f"Erreur lors de la transformation des données : {e}")
        raise

if __name__ == "__main__":
    from extract import extract
    file_path = 'C:/Users/mouss/first-small-etl/data/input/cars.csv'
    cars = extract(file_path)
    cars_transformed = transform(cars)
    print(cars_transformed.head())