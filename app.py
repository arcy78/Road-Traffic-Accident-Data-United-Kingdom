import streamlit as st

st.set_page_config(page_title="Tableau de bord - Sécurité Routière", layout="wide")

st.title("🚦 Tableau de Bord - Sécurité Routière (UK)")
st.markdown("""
Bienvenue sur le tableau de bord interactif des données de sécurité routière au Royaume-Uni.  
Utilisez la barre de navigation à gauche pour explorer les différentes analyses :
- **Analyse Spatiale** : localisation des accidents
- **Gravité & Temporel** : évolution mensuelle, jours critiques
- **Facteurs de Risque** : météo, état de route, jonctions
- **Victimes & Véhicules** : nombre moyen de blessés, types de véhicules
""")
