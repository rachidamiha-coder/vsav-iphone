# --- RECUPERATION AUTOMATIQUE (GPS VIA URL) ---
# On regarde si l'URL contient ?km=50
parametres = st.query_params
distance_auto = parametres.get("km", None)

# Gestion de la distance par défaut
valeur_defaut = 30 # Valeur si pas de GPS

if distance_auto:
    try:
        # 1. On nettoie le texte (on enlève "km" si présent)
        # 2. On remplace la virgule par un point (pour le format français)
        clean_dist = distance_auto.lower().replace("km", "").replace(",", ".").strip()
        
        # 3. On convertit en nombre
        valeur_defaut = int(float(clean_dist))
        
        st.success(f"📍 Distance reçue du GPS : **{valeur_defaut} km**")
    except:
        # Si vraiment ça ne marche pas, on affiche l'erreur mais on ne plante pas
        st.warning(f"Erreur de lecture GPS (Reçu : '{distance_auto}')")
