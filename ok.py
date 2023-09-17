import streamlit as st
import mysql.connector
import pandas as pd 
# Créez une connexion à la base de données MySQL locale
conn = mysql.connector.connect(
    host="localhost",  # Ou l'adresse IP de votre serveur MySQL local
    user="fred",
    password="12345",
    database="ma_base_donneesmysql"
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
