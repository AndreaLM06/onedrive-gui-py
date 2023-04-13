# Application Onedrive-GUI en Python

[![fr](https://img.shields.io/badge/lang-fr-blue.svg)](https://github.com/AndreaLM06/onedrive-gui/blob/main/README.fr.md)
[![GitHub](https://img.shields.io/github/license/AndreaLM06/onedrive-gui)](https://github.com/AndreaLM06/onedrive-gui/blob/main/LICENSE)

Une interface graphique simple pour le [Client OneDrive Linux](https://github.com/abraunegg/onedrive).

---

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Création d'un exécutable](#création-dun-exécutable)
- [Lancement de l'application](#lancement-de-lapplication)
- [Structure de l'application](#structure-de-lapplication)
- [Contribuer](#contribuer)
- [Licence](#licence)

---

## Fonctionnalités

- `Synchroniser` vos fichiers OneDrive
- `Créer` des liens partageables
- Afficher la `sortie de la synchronisation`

---

## Installation

### Installer Node JS

[![Téléchargements annuels du package Npm](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/en/download/current/)

### Installer Python

[![Téléchargements annuels du package Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)

### Installer les paquets

Avant de lancer l'application, assurez-vous d'installer les dépendances requises. Vous pouvez le faire en exécutant la
commande suivante :

```bash
pip install -r requirements.txt
```

---

## Création d'un exécutable

### Installer PyInstaller

[![PyInstaller](https://img.shields.io/badge/PyInstaller-4.0-000000?style=for-the-badge&logo=python&logoColor=white)](https://www.pyinstaller.org/)

### Créer l'exécutable

Pour créer l'exécutable, exécutez la commande suivante:

```bash
pyinstaller --onefile --windowed --icon=images/onedrive.ico src/main.py
```

---

## Lancement de l'application

### Lancer l'application

Pour lancer l'application, exécutez la commande suivante :

```bash
python src/main.py
```

### Lancer l'exécutable

Pour lancer l'exécutable, exécutez la commande suivante :

```bash
OneDrive.exe
```

---

## Structure de l'application

```bash
onedrive-gui
├── images
│   ├── onedrive.ico
│   └── onedrive.png
├── src
│   ├── main.py
│   ├── one_drive_gui.py
│   └── sync_thread.py
├── .gitignore
├── LICENSE
├── OneDrive.exe
├── README.md
└── requirements.txt
```

---

## Contribuer

Si vous souhaitez contribuer à ce projet, n'hésitez pas à soumettre une demande de fusion (pull request) ou à ouvrir une
issue sur GitHub.

---

## License

Ce projet est publié sous la licence MIT. Consultez le fichier [LICENSE](./LICENSE) pour plus de détails.