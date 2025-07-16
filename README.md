# Activité d'initiation à OpenSearch avec Docker


OpenSearch est un moteur de recherche open-source, conçu pour gérer de grands volumes de données. Il permet des recherches sur le texte intégral, des agrégations complexes et des analyses en temps réel sur des ensembles de données hétérogènes, comme des logs, des documents ou des métriques. Il s'intègre facilement avec d'autres outils et langages de programmation. Ce moteur repose fondamentalement sur Apache Lucene, une bibliothèque open-source de recherche qui fournit les algorithmes de base pour l'indexation et la récupération d'informations.
OpenSearch est un 'fork' (bifurcation) d'Elasticsearch.

Nous vous invitons à lire la page Wikipedia suivante: https://en.wikipedia.org/wiki/OpenSearch_(software)

## Docker

Pour installer Docker, vous pouvez suivre les ([instructions](https://docs.docker.com/get-docker/)) de l'entreprise Docker (en anglais). Vous pouvez aussi suivre le guide suivant.

### Installation de Docker sous Windows

Pour installer Docker sous Windows, commencez par vérifier que votre système répond aux exigences : Windows 10 (version 2004 ou ultérieure) ou Windows 11, avec la fonctionnalité Hyper-V activée pour les éditions Pro, Enterprise ou Education. Rendez-vous sur le site officiel de Docker (docker.com) et téléchargez **Docker Desktop** pour Windows. Exécutez le programme d’installation, qui vous guidera à travers un processus simple. Assurez-vous que l’option "Enable WSL 2" est sélectionnée si vous utilisez Windows Subsystem for Linux (WSL 2), car cela améliore les performances. Une fois l’installation terminée, redémarrez votre ordinateur si nécessaire. Lancez Docker Desktop, qui s’exécutera en arrière-plan, et vérifiez son bon fonctionnement en ouvrant un terminal (PowerShell ou Invite de commandes) et en tapant `docker --version`. Si la commande renvoie une version, Docker est prêt à être utilisé.


Après l’installation, vous pouvez exécuter des commandes Docker comme `docker run` depuis un terminal. Par exemple, pour tester, tapez `docker run hello-world`, ce qui télécharge une image de test et exécute un conteneur affichant un message de confirmation. Assurez-vous que Docker Desktop est en cours d’exécution, car il gère le moteur Docker. Si vous utilisez WSL 2, vous pouvez également exécuter des commandes Docker depuis une distribution Linux installée (comme Ubuntu) via le terminal WSL. Les commandes comme `docker pull` (pour télécharger une image), `docker build` (pour créer une image à partir d’un Dockerfile) ou `docker ps` (pour lister les conteneurs en cours) fonctionnent de la même manière que sur d’autres systèmes. Consultez la documentation officielle pour explorer les options de `docker run`, comme le mappage de ports ou de volumes.

### Installation de Docker sous macOS

Sur macOS, Docker s’installe via **Docker Desktop** pour Mac, compatible avec macOS 10.15 (Catalina) ou versions ultérieures. Téléchargez l’installateur depuis le site officiel de Docker. Deux versions sont proposées : une pour les processeurs Intel et une pour les puces Apple Silicon (M1/M2). Choisissez celle correspondant à votre matériel. Une fois téléchargé, ouvrez le fichier .dmg, faites glisser l’icône Docker dans le dossier Applications et lancez Docker Desktop. Lors du premier démarrage, macOS peut demander une autorisation pour exécuter le logiciel. Docker Desktop s’intègre au système via HyperKit (pour Intel) ou la virtualisation native d’Apple (pour M1/M2). Après le lancement, vérifiez l’installation en ouvrant un terminal et en tapant `docker --version`. Si une version s’affiche, l’installation est réussie.


Une fois Docker Desktop lancé sur macOS, vous pouvez utiliser des commandes comme `docker run` dans le terminal. Par exemple, exécutez `docker run hello-world` pour tester votre configuration : cela télécharge une image légère et affiche un message confirmant que Docker fonctionne. Les commandes Docker sont identiques à celles sous Windows ou Linux, comme `docker run -d -p 80:80 nginx` pour lancer un conteneur Nginx accessible via un navigateur sur le port 80. Assurez-vous que Docker Desktop est actif, car il gère le moteur Docker en arrière-plan. Pour des tâches avancées, explorez des options comme `docker run --rm` (pour supprimer automatiquement le conteneur après son arrêt) ou `docker run -v` (pour monter des volumes). La documentation Docker fournit des exemples détaillés pour personnaliser ces commandes selon vos besoins.


## Python

### Installation de Python sous Windows

1. Rendez-vous sur le site officiel : [python.org/downloads](https://www.python.org/downloads/windows/)
2. Téléchargez la dernière version stable (bouton "Download Python ...")
3. Lancez l'installateur téléchargé.
4. **Important** : cochez l'option "Add Python to PATH" avant de cliquer sur "Install Now".
5. Suivez les étapes d'installation.
6. Vérifiez l'installation en ouvrant l'invite de commande (cmd) et en tapant :

   ```bat
   python --version
   ```
   ou
   ```bat
   py --version
   ```
   Si une version s'affiche, Python est installé.

### Installation de Python sous macOS

1. Ouvrez le site officiel : [python.org/downloads](https://www.python.org/downloads/macos/)
2. Téléchargez la dernière version stable pour macOS.
3. Ouvrez le fichier .pkg téléchargé et suivez les instructions d'installation.
4. Une fois installé, ouvrez le Terminal et tapez :

   ```sh
   python3 --version
   ```
   Si une version s'affiche, Python est installé.

**Remarque** : Sur macOS, il est recommandé d'utiliser `python3` au lieu de `python`.

## Prérequis
- Avoir Docker installé sur votre machine ([instructions](https://docs.docker.com/get-docker/))
- Savoir utiliser un terminal
- Avoir installé Python sur votre machine.



## Étapes

### 1. Lancer OpenSearch avec Docker

Dans un terminal, lancez :

```sh
docker compose up -d
```

Vous devez être dans le dossier du projet (contenant le fichier docker-compose.yml.)

- OpenSearch sera accessible sur [http://localhost:9200](http://localhost:9200)

OpenSearch s'utilise comme un service web. Il faut donc créer votre propre application.
Par exemple, vous pouvez interagir avec OpenSearch à partir d'une application web.
Nous utiliserons une approche plus simple.

### 2. Préparer l'environnement Python et extraire le texte des PDF

#### a) Créer un environnement virtuel Python

**macOS / Linux**

Ouvrez un terminal à la racine du projet et lancez :

```sh
python3 -m venv venv
source venv/bin/activate
```

**Windows**

Ouvrez l'invite de commande (cmd) à la racine du projet et lancez :

```bat
python -m venv venv
venv\Scripts\activate
```

#### b) Installer les dépendances

Installez les modules nécessaires avec :

```sh
pip install -r requirements.txt
```

#### c) Extraire et indexer les PDF

Exécutez le script Python `extract_and_index.py` qui :
- Parcourt le dossier `data/`
- Extrait le texte de chaque PDF
- Indexe le texte dans OpenSearch

Lancez le script :

```sh
python extract_and_index.py
```

ou

```sh
python3 extract_and_index.py
```



### 3. Rechercher dans les PDF indexés avec un script Python

Vous pouvez interroger OpenSearch directement en Python. 

Lancez le script :

```sh
python query.py
```

ou

```sh
python3 query.py
```

Lancez ce script, puis saisissez le mot-clé à rechercher (par ex., Bitmap). Les résultats afficheront le nom du fichier et un extrait du contenu trouvé.


### 4. Pour aller plus loin
- Essayez d'indexer d'autres types de documents
- Testez des recherches booléennes ou par phrase


### 5. Stopper OpenSearch


Vous pouvez stopper le service avec

```sh
docker compose down
```

---

## Elasticsearch

Vous pouvez aussi faire cette activité avec Elasticsearch, voir https://github.com/lemire/elastic_demo



**Fichiers à disposition :**
- Les PDF à indexer sont dans le dossier `data/`.
- Le fichier `docker-compose.yml` pour lancer OpenSearch
- Le script Python pour les requêtes : `query.py`
- Le script Python d'indexation : `extract_and_index.py`

Bon courage !
