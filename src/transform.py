import pandas as pd
import numpy as np


def transform(cars):
    cars = cars.rename(columns={
    'Unnamed: 0': 'car_model',
    'am': 'transmission',
    'cyl': 'cylinders',
    "hp": "horsepower_hp",
    "mpg": "miles_per_gallon_mpg",
    'vs': 'engine_shape',
    'gear': 'gears'
})
    cars['car_model'] = cars['car_model'].replace({'Mazda RX4': 'Mazda RX-4',
                                                    'Mazda RX4 Wag': 'Mazda RX-4 Wag',
                                                    'Valiant': 'Plymouth Valiant',
                                                    'Camaro Z28': 'Chevrolet Camaro Z28'},regex=True)
    cars['car_model'] = cars['car_model'].str.replace(r'\bHornet\b', 'AMC Hornet', regex=True)
    cars['car_model'] = cars['car_model'].str.replace(r'\bMerc\b', 'Mercedes', regex=True) 
    cars['transmission'] = cars['transmission'].replace({0: 'Automatic', 1: 'Manual'})
    cars['engine_shape'] = cars['engine_shape'].replace({0: 'V-Shaped', 1: 'Straight'})

    return cars

if __name__ == "__main__":
    from extract import extract
    cars = extract()
    cars_transformed = transform(cars)
    print(cars_transformed.head())