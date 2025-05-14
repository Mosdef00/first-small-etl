# First-Small-ETL

Un projet de pipeline ETL (Extract, Transform, Load) minimaliste conçu à des fins d'apprentissage. Ce pipeline extrait des données d'un fichier CSV contenant des informations sur des voitures, les transforme, puis les charge dans une base de données PostgreSQL.

---

## 🚀 Fonctionnalités principales
- **Extraction** : Lecture des données à partir d'un fichier CSV (`cars.csv`) dans un DataFrame pandas.
- **Transformation** : Nettoyage et renommage des colonnes, remplacement de valeurs et préparation des données pour le chargement.
- **Chargement** : Insertion des données transformées dans une table PostgreSQL.
- **Modularité** : Scripts séparés pour chaque étape (Extraction, Transformation, Chargement) et un script principal pour orchestrer l'ensemble du pipeline.

---

## 🛠️ Prérequis
Pour exécuter ce pipeline, vous aurez besoin de :
- **PostgreSQL** installé et en cours d'exécution.
- **Python** (version 3.x recommandée).
- **Pip** pour gérer les paquets Python.
- Un fichier `.env` contenant les variables de connexion suivantes pour PostgreSQL :
  ```
  DB_USER=<votre-utilisateur>
  DB_PASSWORD=<votre-mot-de-passe>
  DB_HOST=<votre-hôte>
  DB_PORT=<votre-port>
  DB_NAME=<votre-nom-de-base-de-données>
  ```
- Les bibliothèques Python listées dans `requirements.txt` (par exemple, `pandas`, `sqlalchemy`, `python-dotenv`).

---

## 📦 Installation

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/Mosdef00/first-small-etl.git
   cd first-small-etl
   ```

2. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurer PostgreSQL** :
   - Créez une base de données avec le nom spécifié dans votre fichier `.env`.
   - Assurez-vous que les détails de connexion dans le fichier `.env` correspondent.

4. **Ajouter les données d'entrée** :
   - Vérifiez que le fichier `data/input/cars.csv` existe et respecte la structure prévue.

---

## 🚀 Utilisation

1. **Exécuter le pipeline ETL** :
   Lancez le script principal pour exécuter toutes les étapes (Extraction, Transformation, Chargement) :
   ```bash
   python src/run.py
   ```

2. **Exécuter les étapes individuellement** :
   - Extraction :
     ```bash
     python src/extract.py
     ```
   - Transformation :
     ```bash
     python src/transform.py
     ```
   - Chargement :
     ```bash
     python src/load.py
     ```

---

## 📂 Structure du projet

```
first-small-etl/
├── data/
│   └── input/
│       └── cars.csv          # Fichier de données d'entrée
├── notebooks/
│   └── exploration.ipynb     # Notebook Jupyter pour l'exploration des données
├── src/
│   ├── extract.py            # Gestion de l'extraction des données
│   ├── transform.py          # Gestion de la transformation des données
│   ├── load.py               # Gestion du chargement des données
│   └── run.py                # Orchestration du processus ETL
├── requirements.txt          # Dépendances des paquets Python
└── README.md                 # Documentation du projet
```

---

## 🐾 Améliorations futures
- **Intégration à la base de données** : Ajouter des requêtes SQL directement dans les scripts du pipeline ETL pour simplifier le workflow, remplaçant l'exécution manuelle dans `pgcli`.
- **Tests** : Implémenter des tests unitaires et d'intégration pour chaque étape ETL afin de garantir la cohérence des données et la fiabilité du pipeline.
- **Versionnement** : Introduire un système de versionnement pour le pipeline, permettant un meilleur suivi des modifications et des améliorations au fil du temps.
- **Gestion des erreurs** : Ajouter une gestion exhaustive des erreurs et un système de journalisation pour traiter les cas particuliers et les échecs imprévus.
- **Évolutivité** : Optimiser la performance et l'évolutivité pour les ensembles de données plus volumineux.
- **Documentation** : Étendre le README avec des exemples de transformations de données et de requêtes SQL pour plus de clarté.

---

## 📝 Licence
Ce projet est à des fins éducatives et est sous licence MIT.

