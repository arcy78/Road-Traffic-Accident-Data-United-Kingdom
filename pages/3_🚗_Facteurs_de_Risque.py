import streamlit as st
import pandas as pd
import altair as alt
from utils.kpi_calculations import load_data

st.title("🚗 Facteurs de Risque")

df = load_data()

# Filtres dynamiques
st.sidebar.header("Filtres")
district = st.sidebar.multiselect("District", df["Local_Authority_(District)"].unique(), default=None)
weather = st.sidebar.multiselect("Conditions météo", df["Weather_Conditions"].dropna().unique())
road_surface = st.sidebar.multiselect("État de la route", df["Road_Surface_Conditions"].dropna().unique())

# Application des filtres
if district:
    df = df[df["Local_Authority_(District)"].isin(district)]
if weather:
    df = df[df["Weather_Conditions"].isin(weather)]
if road_surface:
    df = df[df["Road_Surface_Conditions"].isin(road_surface)]

# Visualisation : météo
st.subheader("Accidents selon les conditions météo")
weather_counts = df["Weather_Conditions"].value_counts().reset_index()
weather_counts.columns = ["Weather", "Count"]
st.altair_chart(alt.Chart(weather_counts).mark_bar().encode(
    x="Weather",
    y="Count",
    color="Weather"
), use_container_width=True)

# Visualisation : surface route
st.subheader("État de la chaussée")
surface_counts = df["Road_Surface_Conditions"].value_counts().reset_index()
surface_counts.columns = ["Surface", "Count"]
st.altair_chart(alt.Chart(surface_counts).mark_bar().encode(
    x="Surface",
    y="Count",
    color="Surface"
), use_container_width=True)

# Visualisation : jonctions
st.subheader("Type de contrôle aux intersections")
junction_counts = df["Junction_Control"].value_counts().reset_index()
junction_counts.columns = ["Type de contrôle", "Count"]
st.altair_chart(alt.Chart(junction_counts).mark_bar().encode(
    x="Type de contrôle",
    y="Count",
    color="Type de contrôle"
), use_container_width=True)
