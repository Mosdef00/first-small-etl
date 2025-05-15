# First-Small-ETL

Un projet de pipeline ETL (Extract, Transform, Load) minimaliste conçu à des fins d'apprentissage. Ce pipeline extrait des données d'un fichier CSV contenant des informations sur des voitures, les transforme, puis les charge dans une base de données PostgreSQL.

---

## 🚀 Fonctionnalités principales
- **Extraction** : Lecture des données à partir d'un fichier CSV (`cars.csv`) dans un DataFrame pandas.
- **Transformation** : Nettoyage et renommage des colonnes, remplacement de valeurs et préparation des données pour le chargement.
- **Chargement** : Insertion des données transformées dans une table PostgreSQL.
- **Exécution de requêtes SQL** : Gestion des requêtes SQL dynamiques via des fichiers `.sql` et sauvegarde des résultats dans des fichiers CSV.
- **Modularité** : Scripts séparés pour chaque étape (Extraction, Transformation, Chargement, Requêtes SQL) et un script principal pour orchestrer l'ensemble du pipeline.

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

### **Exécuter le pipeline ETL complet**
Lancez le script principal pour exécuter toutes les étapes (Extraction, Transformation, Chargement) :
```bash
python src/run.py
```

### **Exécuter les étapes individuellement**
- **Extraction** :
  ```bash
  python src/extract.py
  ```
- **Transformation** :
  ```bash
  python src/transform.py
  ```
- **Chargement** :
  ```bash
  python src/load.py
  ```

### **Exécuter les requêtes SQL et sauvegarder les résultats**
Utilisez le script `run_queries.py` pour exécuter les requêtes SQL enregistrées dans des fichiers `.sql` et sauvegarder les résultats dans des fichiers CSV :
```bash
python src/run_queries.py
```

- Placez vos fichiers `.sql` dans le dossier `sql/` (par exemple, `sql/max_horsepower.sql`).
- Les résultats de chaque requête seront sauvegardés dans le dossier `query_results/` avec des noms correspondants (par exemple, `query_results/max_horsepower.csv`).

#### **Description des requêtes SQL**
Voici une description des requêtes SQL présentes dans le dossier `sql/` :

1. **`max_horsepower.sql`** :
   - Cette requête sélectionne la voiture avec la puissance maximale (`horsepower_hp`) dans la base de données.
   - **Exemple de sortie** : La voiture et sa puissance maximale.

2. **`cars_by_transmission.sql`** :
   - Cette requête regroupe les voitures par type de transmission (`Transmission`) et compte le nombre de voitures pour chaque type.
   - **Exemple de sortie** : Nombre de voitures avec transmission manuelle ou automatique.

3. **`avg_horsepower.sql`** :
   - Cette requête calcule la puissance moyenne (`horsepower_hp`) des voitures en fonction du nombre de cylindres (`Cylinders`).
   - **Exemple de sortie** : Cylindres et puissance moyenne correspondante.

---

## 📂 Structure du projet

```
first-small-etl/
├── data/
│   └── input/
│       └── cars.csv          # Fichier de données d'entrée
├── notebooks/
│   └── exploration.ipynb     # Notebook Jupyter pour l'exploration des données
├── query_results/            # Résultats des requêtes SQL (CSV générés)
├── sql/
│   ├── max_horsepower.sql    # Exemple de requête SQL
│   ├── cars_by_transmission.sql
│   └── avg_horsepower.sql
├── src/
│   ├── extract.py            # Gestion de l'extraction des données
│   ├── transform.py          # Gestion de la transformation des données
│   ├── load.py               # Gestion du chargement des données
│   ├── run.py                # Orchestration du processus ETL
│   ├── run_queries.py        # Exécution des requêtes SQL et sauvegarde des résultats
├── requirements.txt          # Dépendances des paquets Python
├── .env                      # Fichier pour les variables d'environnement
└── README.md                 # Documentation du projet
```

---

## 🐾 Améliorations futures
- **Tests** : Implémenter des tests unitaires et d'intégration pour chaque étape ETL afin de garantir la cohérence des données et la fiabilité du pipeline.
- **Versionnement** : Introduire un système de versionnement pour le pipeline, permettant un meilleur suivi des modifications et des améliorations au fil du temps.
- **Gestion des erreurs** : Ajouter une gestion exhaustive des erreurs et un système de journalisation pour traiter les cas particuliers et les échecs imprévus.
- **Évolutivité** : Optimiser la performance et l'évolutivité pour les ensembles de données plus volumineux.
- **Documentation** : Étendre le README avec des exemples de transformations de données et de requêtes SQL pour plus de clarté.

---

## 📝 Licence
Ce projet est à des fins éducatives et est sous licence MIT.