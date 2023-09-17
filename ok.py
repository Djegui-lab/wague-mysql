import streamlit as st
import mysql.connector
import pandas as pd 
from decouple import config


# Charger les variables d'environnement depuis le fichier .env
MYSQL_USER = config('MYSQL_USER')
MYSQL_PASSWORD = config('MYSQL_PASSWORD')
MYSQL_HOST = config('MYSQL_HOST')
MYSQL_DATABASE = config('MYSQL_DATABASE')


# Créez une connexion à la base de données en utilisant les variables d'environnement
conn = mysql.connector.connect(
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    host=MYSQL_HOST,
    database=MYSQL_DATABASE
)



# Créez un curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Écrivez votre application Streamlit
st.title("Application de visualisation de données MySQL (Locale)")

# Écrivez une requête SQL pour récupérer des données de votre base de données locale
query = "SELECT * FROM mytable"
pour= "SELECT AVG(age) AS moyenne_age FROM mytable;"

# Utilisez pandas pour lire les données de la base de données et créer un DataFrame
df = pd.read_sql(query, conn)
dfa = pd.read_sql(pour, conn)

# Affichez les données dans Streamlit
st.write("Données de la base de données MySQL (Locale) :")
st.write(df)
st.write(dfa)
# Fermez le curseur et la connexion à la base de données
cursor.close()
conn.close()
