from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from log_config import get_logger

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Configurer le logger
logger = get_logger(__name__)

def get_engine():
    """
    Crée et retourne un moteur SQLAlchemy en utilisant les variables d'environnement.
    """
    try:
        # Obtenir les détails de connexion depuis les variables d'environnement
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST')
        db_port = os.getenv('DB_PORT')
        db_name = os.getenv('DB_NAME')

        # Vérifier que toutes les variables nécessaires sont définies
        missing_vars = [var for var in ['DB_USER', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT', 'DB_NAME'] if not os.getenv(var)]
        if missing_vars:
            raise ValueError(f"Les variables d'environnement suivantes sont manquantes : {', '.join(missing_vars)}")

        # Créer une chaîne de connexion
        connection_string = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'
        logger.info("Connexion à la base de données PostgreSQL établie avec succès.")
        
        # Créer et retourner un moteur SQLAlchemy
        return create_engine(connection_string, pool_size=10, max_overflow=20)

    except Exception as e:
        logger.error(f"Erreur lors de la création du moteur SQLAlchemy : {e}")
        raise

def load_to_postgres(df, table_name, engine):
    """
    Charger un DataFrame dans une table PostgreSQL en utilisant un moteur SQLAlchemy existant.
    """
    try:
        # Charger le DataFrame dans la base de données PostgreSQL
        logger.info(f"Début du chargement des données dans la table '{table_name}'.")
        df.to_sql(table_name, engine, if_exists='replace', index=False, chunksize=1000)
        logger.info(f"Chargement des données dans la table '{table_name}' terminé avec succès.")

    except Exception as e:
        logger.error(f"Erreur lors du chargement des données dans la table '{table_name}' : {e}")
        raise