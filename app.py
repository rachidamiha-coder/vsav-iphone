import streamlit as st
import os

# --- 1. CONFIGURATION ET IMPORT DU LOGO ---
def charger_logo():
    if os.path.exists("logo.png"):
        return "logo.png"
    else:
        return "🚑"

st.set_page_config(
    page_title="Rachid VSAV", 
    page_icon=charger_logo(),
    layout="centered"
)

# --- 2. LOGIQUE GPS INTELLIGENTE (Compatible virgule) ---
# On récupère les paramètres de l'URL
query_params = st.query_params
distance_auto = query_params.get("km", None)

valeur_defaut = 30 # Valeur de départ si pas de GPS

if distance_auto:
    try:
        # Nettoyage : on enlève "km", on change la virgule en point, on enlève les espaces
        clean_dist = distance_auto.lower().replace("km", "").replace(",", ".").strip()
        # Conversion en nombre entier
        valeur_defaut = int(float(clean_dist))
        # Message de succès
        st.success(f"📍 Distance reçue du GPS : **{valeur_defaut} km**")
    except:
        st.warning(f"⚠️ Erreur lecture GPS (Reçu : '{distance_auto}'). Utilisation valeur par défaut.")

# --- 3. BARRE LATERALE (VOTRE MARQUE) ---
st.sidebar.title("Configuration")
if os.path.exists("logo.png"):
    st.sidebar.image("logo.png", width=150)
st.sidebar.caption("Développé par **Rachid AMIHA**")

# --- 4. INTERFACE UTILISATEUR ---
# --- 4. INTERFACE UTILISATEUR (TITRE AVEC LOGO) ---
# On crée deux colonnes : une petite pour l'image (1) et une grande pour le texte (5)
col_logo, col_texte = st.columns([1, 5])

with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=100) # Vous pouvez ajuster la taille ici
    else:
        st.write("🚑")

with col_texte:
    st.title("VSAV : Rachid AMIHA")
    st.write("Calculateur d'empreinte carbone connecté.")
st.write("Calculateur d'empreinte carbone connecté.")

st.write("---")
st.subheader("Données de la mission")

# Le curseur prend la valeur du GPS (valeur_defaut)
distance = st.slider("Distance (km)", 0, 300, valeur_defaut)
conso = st.select_slider("Consommation (L/100km)", options=[10, 15, 18, 20, 25], value=18)

# --- 5. CALCULS ---
facteur_diesel = 3.17 
co2 = (distance * conso / 100) * facteur_diesel

# --- 6. RÉSULTATS ---
st.write("---")
st.header("Résultat")
st.metric("Empreinte Carbone", f"{co2:.2f} kg CO2e")

nb_smartphones = int(co2 / 0.005)
st.info(f"📱 Équivalent à la recharge de **{nb_smartphones}** smartphones.")

