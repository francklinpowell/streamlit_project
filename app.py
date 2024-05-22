import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Rapport de campagne publicitaire", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----
@st.cache_data
def get_data_from_excel():
 df = pd.read_excel(
    io="Suivi Performance Campagne.xlsx",
    engine="openpyxl",
    sheet_name="Rapport",
    usecols="A:K",
    nrows=6,
    )
 return df

df = get_data_from_excel()

# ---- SIDEBAR ----
st.sidebar.header("Veuillez filtrer ici:")

# Assurez-vous que les noms de colonnes utilisés ici correspondent exactement à ceux de votre fichier Excel
acteurs = st.sidebar.multiselect(
    "Sélectionnez les acteurs:",
    options=df["Acteurs "].unique(),
    default=df["Acteurs "].unique()
)

# ---- Filtrage des données ----
df_selection = df[df["Acteurs "].isin(acteurs)]

# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("Aucune donnée disponible en fonction des paramètres de filtre actuels!")
    st.stop()  # This will halt the app from further execution.

# Calcul du taux de conversion
if 'Recrues' in df_selection.columns and 'Arrivees ' in df_selection.columns:
    df_selection["Taux de conversion"] = df_selection["Recrues"] / df_selection["Arrivees "]
else:
    st.error("Les colonnes nécessaires pour calculer le Taux de conversion sont manquantes.")

# ---- MAINPAGE ----
st.title(":bar_chart: Rapport de campagne publicitaire")
st.markdown("##")

# TOP KPI's
total_recrues = int(df_selection["Recrues"].sum())
average_cost_per_recrue = round(df_selection["Cout par recrue"].mean(), 2)
total_budget = int(df_selection["Budget depense"].sum())
average_conversion_rate = round(df_selection["Taux de conversion"].mean(), 2) if "Taux de conversion" in df_selection.columns else 0

left_column, middle_column, right_column, conversion_column = st.columns(4)
with left_column:
    st.subheader("Total Recrues :busts_in_silhouette:")
    st.subheader(f"{total_recrues}")
with middle_column:
    st.subheader("Coût moyen par recrue :euro:")
    st.subheader(f"€ {average_cost_per_recrue}")
with right_column:
    st.subheader("Budget total dépensé :moneybag:")
    st.subheader(f"€ {total_budget}")
with conversion_column:
    st.subheader("Taux de conversion moyen :chart_with_upwards_trend:")
    st.subheader(f"{average_conversion_rate * 100:.2f}%")

st.markdown("""---""")

# RECRUES PAR ACTEURS [BAR CHART]
recrues_par_acteurs = df_selection.groupby(by=["Acteurs "])[["Recrues"]].sum().sort_values(by="Recrues")
fig_recrues_acteurs = px.bar(
    recrues_par_acteurs,
    x=recrues_par_acteurs.index,
    y="Recrues",
    title="<b>Recrues par acteurs</b>",
    color_discrete_sequence=["#0083B7"] * len(recrues_par_acteurs),
    template="plotly_white",
)
fig_recrues_acteurs.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=dict(showgrid=False)
)

# BUDGET DEPENSE ET COUT PAR RECRUE [COMBINED CHART]
fig_budget_cout = px.bar(
    df_selection,
    x="Acteurs ",
    y="Budget depense",
    title="<b>Budget dépensé et coût par recrue</b>",
    color_discrete_sequence=["#0083B7"] * len(df_selection),
    template="plotly_white",
)
fig_budget_cout.add_scatter(
    x=df_selection["Acteurs "],
    y=df_selection["Cout par recrue"],
    mode='lines+markers',
    name="Coût par recrue",
    marker=dict(color="red")
)
fig_budget_cout.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    yaxis=dict(showgrid=False)
)

left_column, right_column = st.columns(2)
left_column.plotly_chart(fig_recrues_acteurs, use_container_width=True)
right_column.plotly_chart(fig_budget_cout, use_container_width=True)

# ---- VISUALISATIONS COMPLÉMENTAIRES ----

# Vérification des colonnes nécessaires pour la visualisation complémentaire
if 'Acteurs ' in df_selection.columns and 'Pourcentage du budget total' in df_selection.columns:
    # Acteurs et pourcentage du budget total (Graphique à barres empilées)
    fig_budget_pourcentage = px.bar(
        df_selection,
        x="Acteurs ",
        y="Pourcentage du budget total",
        title="<b>Pourcentage du budget total par acteurs</b>",
        color="Acteurs ",
        template="plotly_white"
    )
    fig_budget_pourcentage.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(showgrid=False)
    )
else:
    st.error("Les colonnes nécessaires pour le graphique à barres empilées sont manquantes.")

if 'Acteurs ' in df_selection.columns and 'Taux de conversion' in df_selection.columns:
    # Graphique à barres pour le Taux de conversion par acteurs
    fig_taux_conversion = px.bar(
        df_selection,
        x="Acteurs ",
        y="Taux de conversion",
        title="<b>Taux de conversion par acteurs</b>",
        color="Acteurs ",  # Ajout de la couleur basée sur les acteurs
        template="plotly_white"
    )
    fig_taux_conversion.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(showgrid=False)
    )
else:
    st.error("Les colonnes nécessaires pour le graphique à barres du taux de conversion par acteurs sont manquantes.")

if 'Acteurs ' in df_selection.columns and 'Impressions' in df_selection.columns:
    # Acteurs et impressions (Graphique à barres)
    fig_impressions = px.bar(
        df_selection,
        x="Acteurs ",
        y="Impressions",
        title="<b>Impressions par acteurs</b>",
        color="Acteurs ",
        template="plotly_white"
    )
    fig_impressions.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(showgrid=False)
    )
else:
    st.error("Les colonnes nécessaires pour le graphique à barres des impressions sont manquantes.")

if 'Acteurs ' in df_selection.columns and 'Taux de clics' in df_selection.columns:
    # Acteurs et taux de clics (Graphique en courbes)
    fig_taux_clics = px.line(
        df_selection,
        x="Acteurs ",
        y="Taux de clics",
        title="<b>Taux de clics par acteurs</b>",
        markers=True,
        template="plotly_white"
    )
    fig_taux_clics.update_layout(
        plot_bgcolor="rgba(0,0,0,0)",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False)
    )
else:
    st.error("Les colonnes nécessaires pour le graphique en courbes sont manquantes.")

# Affichage des graphiques supplémentaires
st.markdown("## Visualisations Complémentaires")
col1, col2 = st.columns(2)
if 'fig_budget_pourcentage' in locals():
    col1.plotly_chart(fig_budget_pourcentage, use_container_width=True)
if 'fig_taux_conversion' in locals():
    col2.plotly_chart(fig_taux_conversion, use_container_width=True)

col3, col4 = st.columns(2)
if 'fig_impressions' in locals():
    col3.plotly_chart(fig_impressions, use_container_width=True)
if 'fig_taux_clics' in locals():
    col4.plotly_chart(fig_taux_clics, use_container_width=True)

# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
