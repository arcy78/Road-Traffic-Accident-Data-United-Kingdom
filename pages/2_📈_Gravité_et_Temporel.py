import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils.kpi_calculations import load_data

st.title("📈 Analyse de la Gravité et Dimension Temporelle")

# Chargement des données
df = load_data()

# --- FILTRES DYNAMIQUES ---
st.sidebar.header("Filtres")

# Filtre sur la région administrative
local_authorities = df['Local_Authority_(District)'].unique()
selected_local_auth = st.sidebar.multiselect(
    "Sélectionnez les autorités locales",
    options=local_authorities,
    default=local_authorities
)

# Filtre sur le type de route
road_types = df['Road_Type'].unique()
selected_road_type = st.sidebar.multiselect(
    "Sélectionnez le type de route",
    options=road_types,
    default=road_types
)

# Filtre sur la gravité de l'accident (colonne Accident_Severity)
severity_levels = df['Accident_Severity'].unique()
selected_severity = st.sidebar.multiselect(
    "Sélectionnez la gravité de l'accident",
    options=severity_levels,
    default=severity_levels
)

# Application des filtres
df_filtered = df[
    (df['Local_Authority_(District)'].isin(selected_local_auth)) &
    (df['Road_Type'].isin(selected_road_type)) &
    (df['Accident_Severity'].isin(selected_severity))
]

# --- ANALYSE GRAVITÉ ---

st.subheader("Répartition des accidents par gravité")

# Regroupement et comptage par gravité
df_severity = df_filtered.groupby("Accident_Severity").size().reset_index(name="Nombre")

# Affichage des KPI sous forme de st.metric
cols = st.columns(len(df_severity))
for idx, row in df_severity.iterrows():
    cols[idx].metric(label=f"Gravité {row['Accident_Severity']}", value=int(row['Nombre']))

# --- ANALYSE TEMPORALITÉ ---

st.subheader("Analyse temporelle des accidents")

# On utilise la colonne 'Accident Date' convertie en datetime (déjà faite dans load_data)
# Regroupement par mois et gravité
df_time = df_filtered.groupby([ "Month", "Accident_Severity"]).size().reset_index(name="Nombre")

# Pivot pour faciliter le tracé
df_pivot = df_time.pivot(index='Month', columns='Accident_Severity', values='Nombre').fillna(0)

# Tracé avec matplotlib / seaborn
fig, ax = plt.subplots(figsize=(12,6))
df_pivot.plot(kind='line', marker='o', ax=ax)
ax.set_title("Évolution mensuelle des accidents par gravité")
ax.set_xlabel("Mois")
ax.set_ylabel("Nombre d'accidents")
ax.grid(True)
st.pyplot(fig)

# --- ANALYSE JOUR DE LA SEMAINE ---

st.subheader("Répartition des accidents par jour de la semaine")

# Comptage par jour de la semaine et gravité
df_day = df_filtered.groupby(['Day_of_Week', 'Accident_Severity']).size().reset_index(name="Nombre")

# Pivot pour stacked bar chart
df_day_pivot = df_day.pivot(index='Day_of_Week', columns='Accident_Severity', values='Nombre').fillna(0)

# Ordre des jours de la semaine (optionnel)
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df_day_pivot = df_day_pivot.reindex(days_order)

# Tracé en barres empilées
fig2, ax2 = plt.subplots(figsize=(10,6))
df_day_pivot.plot(kind='bar', stacked=True, ax=ax2)
ax2.set_title("Accidents par jour de la semaine et gravité")
ax2.set_xlabel("Jour de la semaine")
ax2.set_ylabel("Nombre d'accidents")
ax2.legend(title='Gravité')
st.pyplot(fig2)
