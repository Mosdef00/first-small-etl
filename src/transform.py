import pandas as pd
import numpy as np


def transform(cars):
    cars = cars.rename(columns={
    'Unnamed: 0': 'Car Model',
    'am': 'Transmission',
    'cyl': 'Cylinders',
    "hp": "horsepower_hp",
    "mpg": "miles_per_gallon_mpg",
    'vs': 'Engine shape',
    'gear': 'Gears'
})
    cars['Transmission'] = cars['Transmission'].replace({0: 'Automatic', 1: 'Manual'})
    cars['Engine shape'] = cars['Engine shape'].replace({0: 'V-Shaped', 1: 'Straight'})

    return cars

if __name__ == "__main__":
    from extract import extract
    cars = extract()
    cars_transformed = transform(cars)
    print(cars_transformed.head())