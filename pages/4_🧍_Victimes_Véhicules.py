import streamlit as st
import pandas as pd
import altair as alt
from utils.kpi_calculations import load_data, average_casualties, average_vehicles

st.title("🧍 Victimes et Véhicules Impliqués")

df = load_data()

# Filtres dynamiques
st.sidebar.header("Filtres")
severity = st.sidebar.multiselect("Gravité", df["Accident_Severity"].unique(), default=None)
vehicle_type = st.sidebar.multiselect("Type de véhicule", df["Vehicle_Type"].dropna().unique())

if severity:
    df = df[df["Accident_Severity"].isin(severity)]
if vehicle_type:
    df = df[df["Vehicle_Type"].isin(vehicle_type)]

# KPI - Moyenne
col1, col2 = st.columns(2)
with col1:
    st.metric("🚑 Victimes moyennes par accident", f"{average_casualties(df):.2f}")
with col2:
    st.metric("🚘 Véhicules moyens par accident", f"{average_vehicles(df):.2f}")

# Visualisation : victimes par gravité
st.subheader("Nombre total de victimes selon la gravité")
victim_severity = df.groupby("Accident_Severity")["Number_of_Casualties"].sum().reset_index()
st.altair_chart(alt.Chart(victim_severity).mark_bar().encode(
    x="Accident_Severity",
    y="Number_of_Casualties",
    color="Accident_Severity"
), use_container_width=True)

# Visualisation : type de véhicule
st.subheader("Répartition des accidents selon le type de véhicule")
veh_count = df["Vehicle_Type"].value_counts().reset_index()
veh_count.columns = ["Type", "Nombre"]
st.altair_chart(alt.Chart(veh_count).mark_bar().encode(
    x="Type",
    y="Nombre",
    color="Type"
).properties(width=700), use_container_width=True)
