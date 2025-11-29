import streamlit as st

# --- CONFIGURATION IOS ---
# Configuration pour que ça ressemble à une App native
st.set_page_config(page_title="VSAV Carbone", page_icon="🚑", layout="centered")

# --- EN-TÊTE ---
st.title("🚑 VSAV : Urgence")
st.caption("Calculateur d'empreinte carbone (Scope 1 - Diesel)")

# --- VARIABLES DU GIEC (IPCC) ---
# Facteur d'émission Diesel (Combustion + Amont)
# Source approx IPCC/Base Carbone : ~3.17 kg CO2e par Litre de Diesel
FACTEUR_IPCC_DIESEL = 3.17 

# --- SAISIE (INTERFACE SIMPLE) ---
st.write("---")
st.subheader("📍 Données de l'intervention")

# Saisie tactile adaptée aux doigts sur iPhone
distance = st.number_input("Distance A/R (km)", min_value=1, value=30, step=1)

# Curseur pour la consommation (Mode Urgence = consommation élevée)
# Un VSAV en urgence consomme entre 15L et 20L/100km
conso_reelle = st.slider("Consommation (L/100km)", min_value=10, max_value=30, value=18)

# --- MOTEUR DE CALCUL ---
litres_consommes = (distance * conso_reelle) / 100
co2_total = litres_consommes * FACTEUR_IPCC_DIESEL

# --- AFFICHAGE RESULTATS ---
st.write("---")
st.header("Résultat")

# Affichage en gros chiffres pour lecture rapide
st.metric(label="Empreinte Carbone Totale", value=f"{co2_total:.2f} kg CO2e")

# --- EQUIVALENCE (PEDAGOGIQUE) ---
# Hypothèse : 1 recharge de smartphone ≈ 5g de CO2 (0.005 kg)
nb_smartphones = co2_total / 0.005

st.success(f"📱 C'est l'équivalent de **{int(nb_smartphones)}** recharges de smartphone.")

# --- NOTE PEDAGOGIQUE ---
with st.expander("ℹ️ Comprendre le calcul (IPCC)"):
    st.write(f"""
    Ce calcul prend en compte la combustion du Diesel d'un VSAV.
    - **Scénario :** Urgence (conduite dynamique).
    - **Facteur d'émission :** {FACTEUR_IPCC_DIESEL} kg CO2e/Litre.
    - **Formule :** (Dist x Conso / 100) x Facteur.
    """)