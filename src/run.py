from extract import extract
from transform import transform
from load import load_to_postgres

def run_etl():
    # 1. Extraction
    raw_data = extract()
    
    # 2. Transformation
    transformed_data = transform(raw_data)
    
    # 3. Chargement
    load_to_postgres(transformed_data, "cars")  # "cars" = nom de la table en DB
    print("ETL terminé avec succès !")

if __name__ == "__main__":
    run_etl()