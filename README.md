# Création d'une Web App en streamlit présentant le suivi de performance des campagnes publicitaires d'entreprises 

Bienvenue sur ma Web application en streamlit présentant des dashboards issu d'un fichier Excel.

<strong>
<ul>
  <li>Le fichier Excel est constitué de 6 lignes et 12 colonnes.</li>
</ul>
</strong>
Chaque ligne du fichier Excel représente les acteurs engagés pour la campagne publicitaire de recrutement. C'est sur ces acteurs que va se baser notre analyse des données.
Les 12 colonnes représentent des indicateurs clés pour le suivi de la campagne publicitaire effectué par les 6 acteurs du marché.

<img width="951" alt="Capture d'écran 2024-05-22 125918" src="https://github.com/francklinpowell/streamlit_project/assets/170517545/adcbfc4e-2d1b-445c-b079-abf7e8b86786">




<strong> Présentation de mon application web developpé avec streamlit de Python </strong>
<strong> 
<ul>
  <li>Code Source de mon application.</li>
</ul>
 </strong>

 Voici le repertoire de mon application sur Visual Studio Code


 <img width="222" alt="Capture d'écran 2024-05-22 130822" src="https://github.com/francklinpowell/streamlit_project/assets/170517545/cf89758f-3a10-4699-ac87-64543fc4274e">

 <ul>
  <li>Le fichier app.py</li>
</ul>


 <br>
<img width="747" alt="Capture d'écran 2024-05-22 131052" src="https://github.com/francklinpowell/streamlit_project/assets/170517545/fdee1e63-3705-40d8-8082-15acd1abb641">

Ce fichier app.py présente une application de tableau de bord interactive pour l'analyse des performances de campagnes publicitaires. Voici un résumé de son contenu et de ses fonctionnalités principales :

 <br>
<strong>Importations et Configuration </strong>

<p>
<strong>
<ul>  
1. Importations : 
</ul>
</strong>
</p>
  
<strong>
<ul>
<li>Pandas pour la manipulation des données. </li>
<li>Plotly Express pour la visualisation des données. </li>
<li>Streamlit pour créer l'application web interactive. </li>
</ul>
</strong>



<p>
<strong>
<ul> 
2. Configuration de la page : 
</ul>
</p>
</strong>
<ul>
<li>Définition du titre, de l'icône et de la mise en page de l'application avec <strong> 'st.set_page_config'.</strong> </li> 

<p>
<strong> 
<li>Lecture des Données : </li>
</strong>
</p>

<p>
<strong>
3. Lecture des données Excel : 
</p>
</strong>
<li>Utilisation de <strong> 'pandas'</strong> pour lire les données d'un fichier Excel. </li> 
<li>Mise en cache des données pour améliorer les performances avec <strong> '@st.cache_data'</strong>. </li> 

<br>
<p>
<strong> 
Interface Utilisateur : 
</strong>
</p>

<p>
<strong>
4. Barre latérale (Sidebar) : 
</p>
</strong>
<li>Ajout d'une fonctionnalité de filtrage pour sélectionner les acteurs spécifiques à partir d'une liste déroulante. </li> 

<br>
<p>
<strong> 
Filtrage et Calculs : 
</strong>
</p>

<p>
<strong>
5. Filtrage des données : 
</p>
</strong>
<li>Filtrage des données en fonction des acteurs sélectionnés. </li> 
<li>Vérification si le filtre retourne des données vides et affichage d'un avertissement le cas échéant. </li> 
