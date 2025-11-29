import streamlit as st
import os

# --- FONCTION SECURISEE POUR CHARGER L'IMAGE ---
# Cela évite que l'app plante si vous oubliez de mettre l'image
def charger_logo():
    if os.path.exists("logo.png"):
        return "logo.png"
    else:
        return "🚑" # Icône par défaut si pas d'image

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Rachid VSAV", 
    page_icon=charger_logo(),
    layout="centered"
)

# --- RECUPERATION AUTOMATIQUE (GPS VIA URL) ---
# On regarde si l'URL contient ?km=50
parametres = st.query_params
distance_auto = parametres.get("km", None)

# --- BARRE LATERALE (VOTRE MARQUE) ---
st.sidebar.title("Configuration")
if os.path.exists("logo.png"):
    st.sidebar.image("logo.png", width=150)
st.sidebar.caption("Développé par **Rachid AMIHA**")

# --- CORPS DE L'APPLICATION ---
st.title("🚑 VSAV : Rachid AMIHA")
st.write("Calculateur d'empreinte carbone connecté.")

# Gestion de la distance par défaut
valeur_defaut = 30
if distance_auto:
    try:
        valeur_defaut = int(float(distance_auto))
        st.success(f"📍 Distance reçue du GPS : **{valeur_defaut} km**")
    except:
        st.warning("Erreur de lecture GPS")

st.write("---")

# --- SAISIE ---
st.subheader("Données de la mission")
distance = st.slider("Distance (km)", 0, 300, valeur_defaut)
conso = st.select_slider("Consommation", options=[10, 15, 18, 20, 25], value=18)

# --- CALCUL ---
# Facteur Diesel (Scope 1 + 3 Amont)
facteur_diesel = 3.17 
co2 = (distance * conso / 100) * facteur_diesel

# --- RESULTATS ---
st.write("---")
st.header("Résultat")
st.metric("Empreinte Carbone", f"{co2:.2f} kg CO2e")

# Equivalence
smartphones = int(co2 / 0.005)
st.info(f"📱 Équivalent à la recharge de **{smartphones}** smartphones.")
