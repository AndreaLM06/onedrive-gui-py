# Onedrive-GUI Python Application

[![fr](https://img.shields.io/badge/lang-fr-blue.svg)](https://github.com/AndreaLM06/onedrive-gui-py/blob/main/README.fr.md)
[![GitHub](https://img.shields.io/github/license/AndreaLM06/onedrive-gui-py)](https://github.com/AndreaLM06/onedrive-gui-py/blob/main/LICENSE)

A simple GUI for [Linux OneDrive Client](https://github.com/abraunegg/onedrive).

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Creating an Executable](#creating-an-executable)
- [Running the Application](#running-the-application)
- [Application Structure](#application-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- `Synchronize` your Onedrive files
- `Create` shareable links
- View the `synchronization output`

---

## Installation

### Install Node JS

[![Npm package yearly downloads](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)](https://nodejs.org/en/download/current/)

### Install Python

[![Python package yearly downloads](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)

### Install packages

Before running the application, make sure to install the required dependencies. You can do this by running the following
command:

```bash
pip install -r requirements.txt
```

---

## Creating an Executable

### Install PyInstaller

[![PyInstaller](https://img.shields.io/badge/PyInstaller-4.0-000000?style=for-the-badge&logo=python&logoColor=white)](https://www.pyinstaller.org/)

### Create the Executable

To create the executable, run the following command:

```bash
pyinstaller --onefile --windowed --icon=images/onedrive.ico src/main.py
```

---

## Running the Application

### Run the Application

To run the application, run the following command:

```bash
python src/main.py
```

### Run the Executable

To run the executable, run the following command:

```bash
onedrive-gui.exe
```

---

## Application Structure

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

## Contributing

If you'd like to contribute to this project, please feel free to submit a pull request or open an issue on GitHub.

---

## License

This project is released under the MIT License. See the [LICENSE](./LICENSE) file for details.