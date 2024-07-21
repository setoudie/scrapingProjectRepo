### 1. Identification de la Problématique

**Sujet du projet** : Extraction de données sur les offres d'emploi dans le domaine de la technologie.

**Objectifs spécifiques** :

- **Scraper des offres d'emploi** pour collecter des informations telles que le **titre de l'emploi**, la **société**, le **lieu**, le **salaire** et les **exigences**.
- **Analyser les tendances** du marché de l'emploi dans le secteur technologique.
- **Comparer les données** extraites des pages web avec celles fournies par une API spécialisée dans les offres d'emploi.

### 2. Sélection de Pages Web

**Pages Web à scraper** :

1. **Page accessible sans connexion** :
    - Site : Indeed
    - URL : https://www.indeed.com/jobs?q=technology&l=
2. **Page nécessitant une connexion** :
    - Site : LinkedIn
    - URL : https://www.linkedin.com/jobs/search/?keywords=technology
3. **Page de réseau social** :
    - Site : Twitter (utilisation de hashtags liés aux offres d'emploi technologiques)
    - URL : Utilisation de l'API Twitter pour rechercher des tweets avec les hashtags #TechJobs, #HiringTech

### 3. Sélection d'une API

**API sélectionnée** :

- **API** : LinkedIn Jobs API —> https://learn.microsoft.com/en-us/linkedin/shared/authentication/getting-access?context=linkedin%2Fcontext
- **Description** : Cette API fournit des données détaillées sur les offres d'emploi publiées sur LinkedIn, y compris les intitulés de postes, les descriptions, les exigences et les informations sur l'employeur.
- **Documentation** : [LinkedIn Jobs API](https://developer.linkedin.com/docs/guide/v2/jobs)

### Plan de Réalisation

1. **Identification de la problématique et des objectifs** : Complété
2. **Sélection des pages web** : Complété
3. **Sélection de l'API** : Complété
4. **Configuration de l'environnement de scraping** :
    - Installer et configurer les outils nécessaires (BeautifulSoup, Selenium, Tweepy).
    - Obtenir les clés API pour accéder à LinkedIn JoTbs API et Twitter API.
5. **Implémentation du scraper** :
    - Développer des scripts pour extraire les données des pages web sélectionnées.
    - Gérer les sessions de connexion pour accéder aux données nécessitant une authentification.
6. **Comparaison des données** :
    - Analyser les données extraites des pages web et de l'API.
    - Générer des rapports sur les tendances du marché de l'emploi technologique.

Cette structuration permet de garantir que toutes les étapes nécessaires pour réaliser le projet de scraping sont couvertes.