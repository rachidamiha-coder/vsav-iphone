import streamlit as st
import os

# --- 1. CONFIGURATION & BRANDING ---
def charger_logo():
    if os.path.exists("logo.png"):
        return "logo.png"
    else:
        return "🌊" # Vague pour Agadir

st.set_page_config(
    page_title="Agadir Santé-Env", 
    page_icon=charger_logo(),
    layout="centered"
)

# En-tête avec Logo
col_logo, col_texte = st.columns([1, 5])
with col_logo:
    if os.path.exists("logo.png"):
        st.image("logo.png", width=100)
    else:
        st.write("🌊")

with col_texte:
    st.title("Dr. Rachid AMIHA")
    st.subheader("Diagnostic Environnemental : Grand Agadir")

st.markdown("---")

# --- 2. PROFIL PATIENT (SPÉCIAL AGADIR) ---
st.sidebar.header("📍 Localisation du Patient")

# Le choix du quartier change tout le diagnostic !
quartier = st.sidebar.selectbox(
    "Quartier de Résidence",
    [
        "Anza / Port (Industriel)",
        "Centre-Ville / Talborjt (Urbain dense)",
        "Cité Suisse / Sonaba (Humide/Côtier)",
        "Tikiouine / Drarga (Péri-urbain/Poussière)",
        "Haut Founty / Illigh (Résidentiel)"
    ]
)

age_patient = st.sidebar.radio("Patient", ["Enfant", "Adulte", "Senior (>65 ans)"])
mode_vie = st.sidebar.checkbox("Exposition professionnelle (Travail extérieur/Usine)?")

# --- 3. MOTIFS DE CONSULTATION (SYMPTÔMES) ---
st.write("### 🩺 Motifs de consultation")

col1, col2 = st.columns(2)

with col1:
    symptomes_respi = st.multiselect(
        "Sphère Respiratoire & ORL",
        ["Toux chronique", "Crise d'asthme", "Rhinite allergique", "Essoufflement (Dyspnée)"]
    )

with col2:
    symptomes_autres = st.multiselect(
        "Autres Sphères",
        ["Irritation des yeux/peau", "Troubles digestifs", "Maux de tête chroniques", "Fatigue inexpliquée"]
    )

# --- 4. LE CERVEAU D'AGADIR (LOGIQUE MÉTIER) ---
st.write("---")
st.write("### 🔍 Analyse & Enquête Environnementale")

# Si rien n'est coché
if not (symptomes_respi or symptomes_autres):
    st.info("👈 Veuillez renseigner le quartier et les symptômes pour lancer l'analyse contextuelle.")

else:
    # --- CAS 1 : RESPIRATOIRE + QUARTIER INDUSTRIEL (ANZA) ---
    if "Anza" in quartier and symptomes_respi:
        st.error("🏭 **Risque Majeur : Pollution Industrielle & Trafic Poids Lourds**")
        st.write("Le patient réside dans une zone à forte densité de particules fines (PM10/PM2.5) et rejets industriels.")
        
        with st.expander("🗣️ L'Interrogatoire Ciblé (Anza)", expanded=True):
            st.markdown("""
            *   "L'appartement est-il exposé directement à la route nationale (camions) ?"
            *   "Sentez-vous des odeurs chimiques (farine de poisson/solvants) le soir ?"
            *   "Avez-vous remarqué des dépôts gras ou noirs sur le linge qui sèche dehors ?"
            """)
        st.warning("👉 **Action :** Vérifier corrélation des crises avec les heures d'activité portuaire.")

    # --- CAS 2 : RESPIRATOIRE + HUMIDITÉ (CÔTIER / SONABA) ---
    elif ("Sonaba" in quartier or "Centre" in quartier) and ("Rhinite allergique" in symptomes_respi or "Crise d'asthme" in symptomes_respi):
        st.warning("💧 **Risque : Moisissures & Acariens (Climat Océanique)**")
        st.write("Le taux d'humidité à Agadir favorise le développement d'allergènes intérieurs.")
        
        with st.expander("🗣️ L'Interrogatoire Ciblé (Humidité)", expanded=True):
            st.markdown("""
            *   "Avez-vous des traces de moisissures (taches noires) aux murs ou plafonds ?"
            *   "La ventilation (VMC) fonctionne-t-elle ou ouvrez-vous les fenêtres le matin ?"
            *   "Les symptômes diminuent-ils quand vous quittez Agadir quelques jours ?"
            """)

    # --- CAS 3 : RESPIRATOIRE + POUSSIÈRE (TIKIOUINE / DRARGA) ---
    elif ("Tikiouine" in quartier) and symptomes_respi:
        st.warning("🌪️ **Risque : Poussières Terrigènes & Pollens**")
        st.write("Zone exposée aux vents de terre et proximité des zones semi-arides/agricoles.")
        
        with st.expander("🗣️ L'Interrogatoire Ciblé", expanded=True):
            st.markdown("""
            *   "Les crises surviennent-elles lors des jours de Chergui (vent d'Est) ?"
            *   "Y a-t-il des chantiers ou des terrains vagues poussiéreux à proximité immédiate ?"
            """)

    # --- CAS 4 : DIGESTIF (TOUT AGADIR) ---
    elif "Troubles digestifs" in symptomes_autres:
        st.warning("🍽️ **Risque : Hygiène Alimentaire / Eau**")
        
        with st.expander("🗣️ L'Interrogatoire Ciblé", expanded=True):
            st.markdown("""
            *   "Avez-vous consommé des coquillages/fruits de mer récemment ?" (Risque biotoxines marines)
            *   "Utilisez-vous l'eau du robinet ou de l'eau stockée ?"
            *   "Avez-vous mangé dans la restauration ambulante ?"
            """)

    # --- CAS 5 : PEAU / YEUX (TOUT AGADIR) ---
    elif "Irritation des yeux/peau" in symptomes_autres:
        if "Anza" in quartier:
            st.error("⚠️ **Suspicion : Retombées atmosphériques irritantes**")
        else:
            st.info("ℹ️ **Investigation :**")
        
        st.markdown("""
        *   "Vous baignez-vous dans des zones non surveillées ?"
        *   "Y a-t-il utilisation de produits phytosanitaires (jardinage/agriculture) à proximité ?"
        """)

    # --- CAS 6 : MAUX DE TÊTE (URBAIN) ---
    elif "Maux de tête chroniques" in symptomes_autres:
        st.info("🚗 **Piste : Monoxyde de Carbone ou Bruit**")
        st.write("En zone urbaine dense, penser à la pollution sonore ou au chauffage défectueux.")
        st.markdown("""
        *   "Utilisez-vous un chauffe-eau à gaz sans évacuation extérieure ?" (Urgent)
        *   "Le logement est-il bruyant la nuit (trafic, commerces) ?"
        """)

# --- 5. CONCLUSION PÉDAGOGIQUE ---
st.write("---")
if symptomes_respi or symptomes_autres:
    st.success(f"✅ **Synthèse pour l'étudiant :** Pour un {age_patient} habitant à **{quartier.split('(')[0]}**, l'origine environnementale doit être explorée avant de traiter uniquement le symptôme.")
