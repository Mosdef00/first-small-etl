import pandas as pd

def extract():
    cars = pd.read_csv('C:/Users/mouss/first-small-etl/data/input/cars.csv')
    return cars

if __name__ == "__main__":
    cars = extract()
    print(cars.head())
