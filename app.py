import streamlit as st
import os

# --- 1. CONFIGURATION & BRANDING ---
def charger_logo():
    if os.path.exists("logo.png"):
        return "logo.png"
    else:
        return "🔬"

st.set_page_config(
    page_title="Agadir Dust-Health", 
    page_icon=charger_logo(),
    layout="centered"
)

# En-tête avec Logo
col_logo, col_texte = st.columns([1, 5])
with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=100)
    else:
        st.write("🔬")

with col_texte:
    st.title("Dr. Rachid AMIHA")
    st.subheader("Diagnostic Santé-Environnement : Agadir")

st.markdown("---")

# --- 2. BARRE LATÉRALE : PARAMÈTRES ---
st.sidebar.header("Dossier Patient")

# Quartiers basés sur votre étude (Table 1 de l'article : Anza, Adrar, Dakhla...)
quartier = st.sidebar.selectbox(
    "Localisation (Site de prélèvement)",
    [
        "Anza (Industriel/Côtier)",
        "Centre-Ville / Talborjt (Trafic Intense)",
        "Adrar / Tikiouine (Péri-urbain/Construction)",
        "Cité Suisse / Sonaba (Résidentiel)",
        "Dakhla / Hay Mohammadi (Dense)"
    ]
)

age_patient = st.sidebar.radio("Patient", ["Enfant (<10 ans)", "Adulte", "Senior (>65 ans)"])

# OPTION PÉDAGOGIQUE PUISSANTE
show_science = st.sidebar.checkbox("Afficher les données scientifiques (Source: Amiha et al.)", value=True)

# --- 3. MOTIFS DE CONSULTATION ---
st.write("### 🩺 Symptômes cliniques")

col1, col2 = st.columns(2)
with col1:
    symptomes_respi = st.multiselect(
        "Respiratoire",
        ["Toux sèche/irritative", "Crise d'asthme", "Bronchiolite", "Rhinite"]
    )
with col2:
    symptomes_cardio = st.multiselect(
        "Cardio-vasculaire / Autres",
        ["Palpitations", "Hypertension", "Irritations cutanées", "Allergies"]
    )

# --- 4. LE MOTEUR SCIENTIFIQUE (Basé sur votre Article 2022) ---
st.write("---")
st.write("### 🔍 Analyse Environnementale (Evidence-Based)")

if not (symptomes_respi or symptomes_cardio):
    st.info("👈 En attente des symptômes pour corrélation avec les données de poussières domestiques.")

else:
    # --- ANALYSE TRAFIC (CUIVRE/ZINC/FER) ---
    # Lien avec l'article : Particules issues des freins/pneus (Introduction + Discussion)
    if "Centre-Ville" in quartier or "Dakhla" in quartier:
        st.error("🚗 **Facteur de Risque : Poussières de Trafic (Métaux lourds)**")
        
        if show_science:
            st.caption("📚 **Données de l'étude (Bouchriti, Amiha et al. 2022) :**")
            st.info("""
            La caractérisation MEB-EDS montre des particules riches en **Fer (Fe), Cuivre (Cu) et Zinc (Zn)**.
            Origine identifiée : Abrasion des freins et pneus (Trafic intense).
            Risque : Inflammation systémique et impact cardio-vasculaire.
            """)
        
        st.markdown("**Question Anamnèse :** *'Le logement donne-t-il directement sur un boulevard fréquenté ? Aérez-vous aux heures de pointe ?'*")

    # --- ANALYSE COMBUSTION / INDUSTRIE (ANZA) ---
    # Lien avec l'article : Particules Sphériques (17.1%) & Carbonées
    elif "Anza" in quartier:
        st.error("🏭 **Facteur de Risque : Particules de Combustion (PM10)**")
        
        if show_science:
            st.caption("📚 **Données de l'étude (Tableau 2) :**")
            st.info("""
            Présence élevée de **particules sphériques (17.1%)** riches en Carbone (C) et Soufre (S).
            Origine : Combustion industrielle et émissions fossiles.
            Taille : PM10 dominantes (44.6% du total).
            """)
            
        st.markdown("**Question Anamnèse :** *'Voyez-vous des dépôts noirs (suies) sur les rebords de fenêtres ?'*")

    # --- ANALYSE CONSTRUCTION / SOL (ADRAR / TIKIOUINE) ---
    # Lien avec l'article : Particules Angulaires (26.3%) et Silice
    elif "Adrar" in quartier:
        st.warning("🏗️ **Facteur de Risque : Poussières Minérales (Silice/Quartz)**")
        
        if show_science:
            st.caption("📚 **Données de l'étude (Morphologie) :**")
            st.info("""
            Dominance de particules **Angulaires (26.3%)** et Sub-angulaires.
            Composition : Silice (Si) et Aluminium (Al).
            Origine : Érosion des sols et chantiers de construction (Urbanisation rapide).
            """)
        
        st.markdown("**Question Anamnèse :** *'Y a-t-il des travaux ou des terrains vagues poussiéreux à proximité immédiate ?'*")

    # --- RISQUE D'ACCUMULATION (GÉNÉRAL) ---
    # Lien avec l'article : Taux de dépôt (19.8 g/m²)
    if "Enfant" in age_patient:
        st.warning("👶 **Vigilance Pédiatrique : Ingestion & Inhalation**")
        if show_science:
            st.info(f"**Taux de dépôt mesuré à Agadir : 19.8 ± 7.4 g/m²/an.**\nC'est une charge élevée qui favorise la resuspension.")
        
        st.success("💡 **Conseil Scientifique :** Recommander le **nettoyage humide** (serpillère) plutôt que le balayage à sec qui remet les PM10 en suspension (cité dans l'article).")

# --- 5. FOOTER ---
st.write("---")
st.caption("Application basée sur l'article : *Household Dust from a City in Morocco: Characterization by SEM* (**Amiha et al., 2022**).")
