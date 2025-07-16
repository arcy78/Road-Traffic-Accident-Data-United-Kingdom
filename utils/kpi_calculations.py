import pandas as pd
import streamlit as st  # ← 🔴 Import manquant corrigé
import os

@st.cache_data
def load_data(path='data/Road_Accident_Data.csv'):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Le fichier {path} est introuvable.")

    df = pd.read_csv(path)

    # Nettoyage des colonnes date/heure
    df["Accident Date"] = pd.to_datetime(df["Accident Date"], errors='coerce')
    df["Time"] = pd.to_datetime(df["Time"], format="%H:%M", errors='coerce')

    # Colonnes dérivées
    df['Hour'] = df["Time"].dt.hour
    df['Month'] = df["Accident Date"].dt.to_period('M').astype(str)

    # Normalisation des chaînes
    df["Accident_Severity"] = df["Accident_Severity"].astype(str)
    df["Weather_Conditions"] = df["Weather_Conditions"].astype(str)
    df["Vehicle_Type"] = df["Vehicle_Type"].astype(str)
    df["Road_Surface_Conditions"] = df["Road_Surface_Conditions"].astype(str)

    return df

# KPI principaux

def total_accidents(df):
    return len(df)

def total_casualties(df):
    return int(df["Number_of_Casualties"].sum())

def total_vehicles(df):
    return int(df["Number_of_Vehicles"].sum())

def average_casualties(df):
    if len(df) == 0:
        return 0
    return df["Number_of_Casualties"].mean()

def average_vehicles(df):
    if len(df) == 0:
        return 0
    return df["Number_of_Vehicles"].mean()

def count_by_severity(df):
    return df["Accident_Severity"].value_counts().to_dict()

def count_by_weather(df):
    return df["Weather_Conditions"].value_counts().to_dict()

def count_by_road_surface(df):
    return df["Road_Surface_Conditions"].value_counts().to_dict()

def count_by_vehicle_type(df):
    return df["Vehicle_Type"].value_counts().to_dict()

