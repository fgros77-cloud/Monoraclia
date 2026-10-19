import streamlit as st
import streamlit.components.v1 as components
import time
import os
import random
from datetime import datetime
from openai import OpenAI


# =========================
# 🔮 INTRO (UNE SEULE FOIS)
# =========================
if "tirages_count" not in st.session_state:
    st.session_state.tirages_count = 0
if "intro_done" not in st.session_state:
    st.session_state.intro_done = False

if not st.session_state.intro_done:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown(
            "<h1 style='text-align:center;color:#a78bfa;'>🔮 MONORACLIA</h1>",
            unsafe_allow_html=True
        )
    st.markdown("""
    <div style="
        position:fixed;
        top:0;left:0;
        width:100vw;height:100vh;
        background:black;
        display:flex;
        justify-content:center;
        align-items:center;
        flex-direction:column;
        z-index:9999;
        color:white;
    ">
        <p>Connexion aux énergies...L'oracle vous guide</p>
                
        ✨
    </div>
    """, unsafe_allow_html=True)

    time.sleep(2)

    st.session_state.intro_done = True
    st.rerun()




# 💥 ICI TON APP NORMALE (TRÈS IMPORTANT)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def interpretation_oracle_ia(question, cartes, numerologie, pendule):

    chemin_vie, annee_perso = numerologie if numerologie else ("?", "?")

    prompt = f"""
Tu es un oracle spirituel puissant, précis et bienveillant.

Ta mission :
Donner une lecture profonde et cohérente en reliant TOUS les éléments.

Question du consultant :
{question}

Cartes tirées :
{cartes}

Numérologie :
Chemin de vie = {chemin_vie}
Année personnelle = {annee_perso}

Réponse du pendule :
{pendule}

Instructions :

1. Analyse les cartes comme des symboles (pas juste descriptif)
2. Relie-les à la numérologie (cycle de vie, énergie actuelle)
3. Confirme ou nuance avec le pendule
4. Donne UNE lecture globale cohérente (pas 3 blocs séparés)
5. Ton style :
   - fluide
   - profond
   - intuitif
   - humain
   - jamais robotique

Structure :

- Une ouverture personnalisée
- Une lecture globale connectée
- Une guidance claire
- Une phrase finale marquante

Interdits :
- pas de listes
- pas de répétitions
- pas de banalités

Réponds en français.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9
    )

    return response.choices[0].message.content

st.set_page_config(layout="centered")

# =========================
# 🔮 TITRE PROPRE (SANS BUG)
# =========================
st.markdown("""
<h1 style='text-align:center;
font-size:52px;
color:#c084fc;
text-shadow:
    0 0 5px #a78bfa,
    0 0 15px #8c64ff,
    0 0 30px rgba(140,100,255,0.8);
animation: fadeIn 2s ease-in-out;
'>
🔮 MONORACLIA
</h1>

<style>
@keyframes fadeIn {
    from {opacity:0; transform: translateY(-10px);}
    to {opacity:1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)
# =========================
# 🎨 STYLE PROPRE
# =========================
st.markdown("""
<style>
/* 🔮 INPUTS (date + question) */
input {
    font-size: 20px !important;     /* taille texte */
    padding: 12px !important;       /* espace intérieur */
    border-radius: 10px !important;

    background: rgba(255,255,255,0.08) !important;
    color: #ffd87e;

    border: 1px solid rgba(140,100,255,0.4) !important;
}

/* ✨ focus (quand on clique dedans) */
input:focus {
    outline: none !important;

    border: 1px solid #8c64ff !important;

    box-shadow: 0 0 10px rgba(140,100,255,0.8);
}

/* 🏷 labels */
label {
    font-size: 16px !important;
    color: #cccccc !important;
}

/* TABS VISIBLES */
/* =========================
   🔮 ONGLET ORACLE STYLE
========================= */
            
/* 🔮 boutons principaux (oracle) */
.stButton > button {

    background: linear-gradient(135deg, #1a1a2e, #2a2a4a) !important;
    color: #a78bfa !important;

    border: 1px solid rgba(140,100,255,0.5) !important;
    border-radius: 12px !important;

    padding: 10px 20px !important;

    box-shadow: 0 0 10px rgba(140,100,255,0.4);

    transition: all 0.3s ease;
}

/* ✨ hover */
.stButton > button:hover {
    background: linear-gradient(135deg, #3b2fff, #8c64ff) !important;
    color: white !important;

    box-shadow: 0 0 25px rgba(140,100,255,0.9);

    transform: scale(1.05);
}

/* 💥 clic */
.stButton > button:active {
    transform: scale(0.95);
}

button[data-baseweb="tab"] {
    font-size: 30px !important;
    font-weight: 600 !important;
    color: rgba(255,255,255,0.6) !important;
    padding: 20px 40px !important;

    background: transparent !important;
    border: none !important;

    transition: all 0.3s ease;
}

/* ✨ hover */
button[data-baseweb="tab"]:hover {
    color: #a78bfa !important;
    text-shadow: 0 0 10px rgba(167,139,250,0.8);
    transform: translateY(-2px);
}

/* 🔥 onglet actif */
button[data-baseweb="tab"][aria-selected="true"] {

    color: ##b5bbf3 !important;

    /* néon glow */
    text-shadow:
        0 0 5px #a78bfa,
        0 0 10px #8c64ff,
        0 0 20px #8c64ff,
        0 0 40px rgba(140,100,255,0.8);

    position: relative;
}

/* ligne néon animée dessous */
button[data-baseweb="tab"][aria-selected="true"]::after {
    content: "";
    position: absolute;
    left: 20%;
    bottom: 0;
    width: 60%;
    height: 3px;

    background: linear-gradient(90deg, #da8531 #a78bfa);

    border-radius: 5px;

    box-shadow: 0 0 10px #a5e3bb, 0 0 20px #a5e3bb;

    animation: glowLine 1.5s infinite alternate;
}

/* animation glow */
@keyframes glowLine {
    from {
        opacity: 0.6;
        box-shadow: 0 0 5px #8c64ff;
    }
    to {
        opacity: 1;
        box-shadow: 0 0 20px #a78bfa;
    }
}

/* espace */
.stTabs {
    margin-top: 20px;
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #0f0f1a, #1a1a2e);
    color: #a5e3bb;
}
.block-container {
    max-width: 1100px;
    margin: auto;
}
img {
    border-radius: 12px;
}

/* 🎴 boutons cartes */
div[data-testid="column"] button {
    height: 70px !important;
    width: 70px !important;
    border-radius: 50% !important;

    background: rgba(140,100,255,0.1) !important;
    border: 1px solid rgba(140,100,255,0.3) !important;

    transition: 0.2s;
}

div[data-testid="column"] button:hover {
    box-shadow: 0 0 15px rgba(140,100,255,0.8);
    transform: scale(1.1);
}
</style>
""", unsafe_allow_html=True)

# =========================
# 📦 CARTES
# =========================
def interpretation_belline(cartes, question):

    messages = {
        "hasard": "Une part d’imprévu influence ta situation.",
        "héritage": "Un poids du passé ou une transmission joue un rôle.",
        "trahison": "Une méfiance ou une rupture doit être observée.",
        "étoilefemme": "Une énergie féminine guide ou influence ton chemin."
    }

    texte = "🔮 Lecture du tirage :\n\n"

    for c in cartes:
        texte += f"• {messages.get(c.lower(), 'Une énergie agit en profondeur.')}\n"

    if question:
        texte += f"\n👉 Par rapport à ta question, une évolution se dessine progressivement.\n"

    texte += "\n✨ Fais confiance au mouvement en cours."

    return texte
def charger_cartes():
    if not os.path.exists("images"):
        return {}

    fichiers = os.listdir("images")
    cartes = {}

    for f in fichiers:
        if f.endswith(".jpg") and f != "dos.jpg":
            cartes[f.replace(".jpg", "")] = f

    return cartes

cartes = charger_cartes()

# =========================
# 🔄 SESSION
# =========================
if "selected" not in st.session_state:
    st.session_state.selected = []

# =========================
# 🔮 INPUT
# =========================

st.markdown("## 🔮 Tes informations")

col1, col2 = st.columns(2)

with col1:
    date_str = st.text_input("Date de naissance", "01/01/1990")

    

with col2:
    question = st.text_input("Ta question (Laisse ton intuition s'ouvrir)", "", key="question_unique")
# 🔄 RESET si nouvelle question
if "last_question" not in st.session_state:
    st.session_state.last_question = ""

if question != st.session_state.last_question:
    st.session_state.tirages_count = 0
    st.session_state.last_question = question

    
try:
    date_naissance = datetime.strptime(date_str, "%d/%m/%Y").date()
    
    
except:
    date_naissance = None

st.markdown("---")
def interpretation_numerologie(chemin_vie, annee_perso):

    interpretations = {
        1: "Nouveau départ, leadership, indépendance.",
        2: "Relations, patience, sensibilité.",
        3: "Créativité, communication, joie.",
        4: "Stabilité, travail, construction.",
        5: "Changement, liberté, mouvement.",
        6: "Famille, responsabilités, harmonie.",
        7: "Introspection, spiritualité, recul.",
        8: "Pouvoir, réussite matérielle.",
        9: "Fin de cycle, transformation."
    }

    texte_cv = interpretations.get(chemin_vie, "")
    texte_ap = interpretations.get(annee_perso, "")

    return f"""
✨ Ton chemin de vie indique : {texte_cv}

📅 Ton année personnelle annonce : {texte_ap}

👉 C’est une période clé pour avancer en conscience.
"""

# =========================
# 🧭 TABS
# =========================
tab1, tab2, tab3 = st.tabs(["🔢 Numérologie", "🃏 Belline", "🧿 Pendule"])

# =========================
# 🔢 NUMÉROLOGIE
# =========================
with tab1:

    st.markdown("## 🔢 Numérologie")

    if date_naissance:
        st.write("Numérologie OK")

        chiffres = [int(c) for c in date_naissance.strftime("%d%m%Y")]
        total = sum(chiffres)
        

        while total > 9:
            total = sum(int(c) for c in str(total))

        annee = datetime.now().year
        total_annee = sum(int(c) for c in date_naissance.strftime("%d%m")) + sum(int(c) for c in str(annee))

        while total_annee > 9:
            total_annee = sum(int(c) for c in str(total_annee))
            st.session_state.result_numerologie = (total, total_annee)

        st.success(f"✨ Chemin de vie : {total} | 📅 Année perso : {total_annee}")
        st.markdown("### ✨ Interprétation")

texte = interpretation_numerologie(total, total_annee)


st.markdown(f"""
<div style="
font-size:28px;
padding:25px;
border-radius:15px;
background:linear-gradient(90deg,#1f4037,#99f2c8);
text-align:center;
color:bc6c25;
font-weight:600;
text-shadow: 0 0 10px rgba(gold,0.8);
">
✨ Chemin de vie : <b>{total}</b> &nbsp;&nbsp;
📅 Année perso : <b>{total_annee}</b>
</div>
""", unsafe_allow_html=True)
        

# =========================
# 🃏 BELLINE
# =========================

with tab2:

    st.markdown("## 🃏 Tirage Belline")
    st.markdown("Clique sur 4 cartes")

    cartes_list = list(cartes.keys())

    nb_cols = 10

    for row in range(0, len(cartes_list), nb_cols):

        cols = st.columns(nb_cols)

        for i, carte in enumerate(cartes_list[row:row+nb_cols]):

            idx = row + i

            with cols[i]:

                st.image("images/dos.jpg", width=80)

                if st.button("✨", key=f"card_{idx}"):

                    if carte not in st.session_state.selected and len(st.session_state.selected) < 4:
                        st.session_state.selected.append(carte)
                        st.rerun()

    # 🔮 TIRAGE
    
    if len(st.session_state.selected) == 4:
        st.session_state.result_belline = st.session_state.selected
        

        st.markdown("## 🔮 Ton tirage")

    cols = st.columns(4)
    placeholders = [col.empty() for col in cols]

    # étape 1 → dos
    for i in range(4):
        placeholders[i].image("images/dos.jpg", width=150)

    time.sleep(0.5)

    # étape 2 → flip
    for i, carte in enumerate(st.session_state.selected):

        placeholders[i].image("images/dos.jpg", width=150)
        time.sleep(0.3)

        placeholders[i].image(f"images/{cartes[carte]}", width=150)
        time.sleep(0.4)

    # étape 3 → affichage final
    for i, carte in enumerate(st.session_state.selected):

        placeholders[i].image(f"images/{cartes[carte]}", width=150)
        placeholders[i].caption(carte.capitalize())

      # 🔮 INTERPRÉTATION (ICI UNIQUEMENT)

st.markdown("### ✨ Interprétation")

texte = interpretation_belline(st.session_state.selected, question)

st.markdown(f"""
<div style="
padding:20px;
background:rgba(255,255,255,0.05);
border-radius:15px;
font-size:18px;
line-height:1.6;
">
{texte}
</div>
""", unsafe_allow_html=True)  
         


    # 🔄 RESET (UNE SEULE FOIS)
if st.button("🔄 Refaire un tirage"):

        st.session_state.selected = []
        st.rerun()

# =========================
# 🧿 PENDULE
# =========================
with tab3:

    st.markdown("## 🧿 Pendule")

    q = st.text_input("Pose ta question""Les guides se connectent à toi...", key="pendule_question")

    if st.button("🔮 Interroger le pendule", key="pendule_btn"):

        if q.strip() == "":
            st.warning("Pose une question 😉")

        else:
            st.markdown("✨ Le pendule se connecte...")

            st.image("images/pendule.gif", width=200)
            time.sleep(2)

            resultat = random.choice(["OUI", "NON", "PEUT-ÊTRE"])

            # 👉 STOCKAGE POUR SYNTHÈSE
            st.session_state.result_pendule = resultat

            # 👉 COULEUR
            couleur = {
                "OUI": "lightgreen",
                "NON": "salmon",
                "PEUT-ÊTRE": "gold"
            }

            st.markdown(
                f"<h2 style='text-align:center;color:{couleur[resultat]}'>{resultat}</h2>",
                unsafe_allow_html=True
            )

            # 🔮 INTERPRÉTATION
            interpretation = {
                "OUI": "Les énergies sont favorables. Une ouverture est possible.",
                "NON": "Il y a un blocage ou une résistance actuellement.",
                "PEUT-ÊTRE": "La situation évolue encore. Rien n’est figé."
            }

            st.markdown("### ✨ Interprétation")

            st.markdown(f"""
            <div style="
            padding:20px;
            background:rgba(255,255,255,0.05);
            border-radius:15px;
            text-align:center;
            font-size:18px;
            ">
            {interpretation[resultat]}
            </div>
            """, unsafe_allow_html=True)
            st.markdown("---")

if st.button("🔮 Révélation complète de l'oracle"):
    if st.session_state.tirages_count >= 3:
        st.warning("✨ L’oracle a déjà parlé... prends le temps d’intégrer le message.")
        st.stop()

    st.session_state.tirages_count += 1

    with st.spinner("✨ Connexion aux énergies..."):

        texte = interpretation_oracle_ia(
            question,
            st.session_state.get("result_belline"),
            st.session_state.get("result_numerologie"),
            st.session_state.get("result_pendule")
        )

    st.markdown("## 🔮 Message de l’oracle")

    st.markdown(f"""
    <div style="
    padding:25px;
    background:linear-gradient(90deg,#1f4037,#6a56a8);
    border-radius:15px;
    font-size:18px;
    line-height:1.7;
    ">
    {texte}
    </div>
    """, unsafe_allow_html=True)
    st.write("FIN APP")