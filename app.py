import duckdb
import pandas as pd
import streamlit as st

# Connexion DuckDB et chargement du CSV
con = duckdb.connect(database=':memory:')
df = pd.read_csv("data/Road_Accident_Data.csv")
con.register("accidents", df)

import folium
from streamlit_folium import folium_static
# --- Configuration de la page ---
st.set_page_config(page_title="Shopdern Dashboard", layout="centered")

# Carte centrée sur le Royaume-Uni
m = folium.Map(location=[54.5, -3], zoom_start=6)

# Ajout des points
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=3,
        color='red' if row['Road_Type'] == 'Motorway' else 'blue',
        fill=True,
        fill_opacity=0.6
    ).add_to(m)

folium_static(m)
