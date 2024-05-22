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




<strong>I. Présentation de mon application web developpé avec streamlit de Python </strong>
<strong> 
<ul>
  <li>Code Source de mon application.</li>
</ul>
 </strong>

 Voici le repertoire de mon application sur Visual Studio Code


 <img width="222" alt="Capture d'écran 2024-05-22 130822" src="https://github.com/francklinpowell/streamlit_project/assets/170517545/cf89758f-3a10-4699-ac87-64543fc4274e">

<strong>
 <br>
 <p>
 <ul>
  <li>Le fichier app.py</li>
</ul>
</p>
</strong>

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

<br>
<p>
<strong>
6. Calcul des KPI : 
</p>
</strong>
<li>Calcul des principaux indicateurs de performance (KPI) : total des recrues, coût moyen par recrue, budget total dépensé et taux de conversion moyen. </li> 
<li>Affichage de ces KPI dans une disposition en colonnes. </li> 

<br>
<p>
<strong> 
Visualisations
</strong>
</p>

<br>
<p>
<strong>
7. Graphiques principaux :
</p>
</strong>
<li>Graphique en barres des recrues par acteur. </li> 
<li>Graphique combiné montrant le budget dépensé et le coût par recrue par acteur. </li> 

<br>
<p>
<strong>
8. Visualisations complémentaires :
</p>
</strong>

<li>Graphiques supplémentaires pour les pourcentages de budget, taux de conversion, impressions, et taux de clics par acteur. </li> 
<li>Vérification de la présence des colonnes nécessaires pour ces visualisations et affichage d'erreurs en cas de données manquantes. </li> 

<br>
<p>
<strong> 
Personnalisation de l'Interface
</strong>
</p>


<p>
<strong>
9. Masquage des éléments par défaut de Streamlit :
</p>
</strong>
<li>Masquage du menu principal, du pied de page et de l'en-tête de Streamlit pour une présentation plus propre. </li> 

<br>
<p>
<strong> 
Conclusion
</strong>
</p>


Le code source fournit une application web interactive qui permet aux utilisateurs de visualiser et d'analyser les performances des campagnes publicitaires par différents acteurs. Les utilisateurs peuvent filtrer les données, afficher les principaux indicateurs de performance et examiner plusieurs graphiques interactifs pour mieux comprendre les résultats des campagnes.




<p>
<strong> 
<li>Le Dockerfile : </li>
</strong>
</p>

<img width="535" alt="Capture d'écran 2024-05-22 192608" src="https://github.com/francklinpowell/streamlit_project/assets/170517545/26467a29-bea8-41f5-8593-f69f6d44bddd">

<br>
<p>
<strong> 
Commandes basiques de Docker en ligne de commande 
</strong>
</p>
<img width="441" alt="Capture d'écran 2024-05-21 171844" src="https://github.com/francklinpowell/streamlit_project/assets/170517545/81862c4c-dd09-48ef-b468-f52e4a7b086d">
<img width="613" alt="Capture d'écran 2024-05-21 171907" src="https://github.com/francklinpowell/streamlit_project/assets/170517545/7dfb1ab8-579f-465d-a8c7-9ba8797ac03f">
<img width="667" alt="Capture d'écran 2024-05-21 171937" src="https://github.com/francklinpowell/streamlit_project/assets/170517545/abc513ee-03c0-45e8-99ad-b9665f7d5d9e">
<img width="397" alt="Capture d'écran 2024-05-21 172044" src="https://github.com/francklinpowell/streamlit_project/assets/170517545/6ebf0495-b460-42b7-8296-f1fe25aea396">
<img width="755" alt="Capture d'écran 2024-05-21 172159" src="https://github.com/francklinpowell/streamlit_project/assets/170517545/df0aee4f-aed0-40d0-90f1-20350186968d">
<br>
<br>



<strong>II. Déploiement de mon application Web Streamlit sur Docker </strong>
<br>
<img width="739" alt="Capture d'écran 2024-05-22 084241" src="https://github.com/francklinpowell/streamlit_project/assets/170517545/311a481c-1a70-40bf-bf80-7813ed44a8ce">


<p>
Cette commande construit une image Docker à partir d'un Dockerfile situé dans le répertoire courant et tague cette image avec le nom francklinprojetstreamlit. Une fois l'image construite, nous pouvez l'exécuter, la partager ou la déployer dans un environnement Docker.
</p>
