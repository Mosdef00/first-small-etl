
# 🚗 ETL Pipeline pour données de voitures

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13%2B-blue)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

Un pipeline ETL minimaliste pour nettoyer et charger des données automobiles dans PostgreSQL.

## 📋 Table des matières
- [Installation](#-installation)
- [Usage](#-usage)
- [Structure du Projet](#-structure-du-projet)
- [Exemple de Données](#-exemple-de-données)
- [Dépannage](#-dépannage)
- [Contributions](#-contributions)
- [License](#-license)

## 📦 Installation

### Prérequis
- Python 3.9+
- PostgreSQL 13+
- pip
- git
- bash

### Étapes
1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/Mosdef00/first-small-etl.git
   cd first-small-etl

2. **Configurer l'environnement** : 
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate    # Windows
    pip install -r requirements.txt 

3. **Configurer la base de données** :