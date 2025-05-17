import pytest
from src.transform import transform
import pandas as pd

def test_transform():
    """
    Test de la fonction transform pour vérifier que les données sont correctement transformées.
    """
    # Données d'entrée simulées
    data = pd.DataFrame({
        'Unnamed: 0': ['Mazda RX4', 'Toyota Corolla'],
        'am': [1, 0],
        'cyl': [6, 4],
        'hp': [110, 65],
        'mpg': [21.0, 33.9],
        'vs': [0, 1],
        'gear': [4, 4]
    })

    # Appelle la fonction de transformation
    transformed_data = transform(data)

    # Vérifie que les colonnes ont été renommées
    assert "car_model" in transformed_data.columns
    assert "transmission" in transformed_data.columns
    assert "horsepower_hp" in transformed_data.columns

    # Vérifie que les valeurs ont été transformées
    assert transformed_data.loc[0, "car_model"] == "Mazda RX-4"  # Le nom du modèle est modifié
    assert transformed_data.loc[0, "transmission"] == "Manual"  # Valeur transformée
    assert transformed_data.loc[1, "engine_shape"] == "Straight"  # Valeur transformée