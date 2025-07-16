import streamlit as st
import pydeck as pdk
from utils.kpi_calculations import load_data

st.title("📊 Analyse Spatiale des Accidents")

df = load_data()

st.subheader("Carte interactive des accidents")

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/light-v9',
    initial_view_state=pdk.ViewState(
        latitude=df['Latitude'].mean(),
        longitude=df['Longitude'].mean(),
        zoom=6,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'ScatterplotLayer',
            data=df,
            get_position='[Longitude, Latitude]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
