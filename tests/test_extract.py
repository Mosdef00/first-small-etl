import pytest
from src.extract import extract
import pandas as pd

def test_extract(tmp_path):
    """
    Test de la fonction extract pour vérifier que les données sont correctement extraites.
    """
    # Crée un fichier CSV temporaire
    test_file = tmp_path / "test_data.csv"
    test_file.write_text(
        "car_model,miles_per_gallon_mpg,cylinders,disp,horsepower_hp,drat,wt,qsec,engine_shape,transmission,gears,carb\n"
        "Mazda RX-4,21.0,6,160.0,110,3.9,2.62,16.46,V-Shaped,Manual,4,4\n"
        "Toyota Corolla,33.9,4,71.1,65,4.22,1.835,19.9,Straight,Manual,4,1"
    )

    # Appelle la fonction d'extraction
    cars = extract(str(test_file))

    # Vérifie que les données sont correctement extraites
    assert isinstance(cars, pd.DataFrame)  # Doit être un DataFrame
    assert len(cars) == 2  # Vérifie qu'il y a 2 lignes
    assert list(cars.columns) == [
        "car_model",
        "miles_per_gallon_mpg",
        "cylinders",
        "disp",
        "horsepower_hp",
        "drat",
        "wt",
        "qsec",
        "engine_shape",
        "transmission",
        "gears",
        "carb",
    ]  # Vérifie les colonnes