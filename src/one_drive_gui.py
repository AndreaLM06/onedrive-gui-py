import os
from functools import partial

from PySide6.QtGui import QActionGroup
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QPlainTextEdit, QFileDialog, QMenuBar, \
    QMenu, QToolBar

from sync_thread import SyncThread


class OneDriveGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.display_sync_status_button = None
        self.download_only_button = None
        self.sync_button = None
        self.create_share_link_button = None
        self.file_menu = None
        self.clear_button = None
        self.output = None
        self.setWindowTitle("OneDrive GUI")
        self.resize(700, 400)

        self.translations = {
            "en": {"file_menu": "File", "synchronize": "Synchronize",
                   "download_only": "Download Only",
                   "display_sync_status": "Display Sync Status", "create_share_link": "Create Share Link",
                   "clear_output": "Clear Output", "language": "English"},

            "fr": {"file_menu": "Fichier", "synchronize": "Synchroniser",
                   "download_only": "Télécharger seulement",
                   "display_sync_status": "Afficher l'état de synchronisation",
                   "create_share_link": "Créer un lien de partage",
                   "clear_output": "Effacer la sortie", "language": "Français"},

            "it": {"file_menu": "File", "synchronize": "Sincronizza",
                   "download_only": "Scarica solo",
                   "display_sync_status": "Mostra stato sincronizzazione",
                   "create_share_link": "Crea link di condivisione",
                   "clear_output": "Cancella output", "language": "Italiano"},

            "es": {"file_menu": "Archivo", "synchronize": "Sincronizar",
                   "download_only": "Descargar solo",
                   "display_sync_status": "Mostrar estado de sincronización",
                   "create_share_link": "Crear enlace para compartir",
                   "clear_output": "Borrar salida", "language": "Español"},

            "de": {"file_menu": "Datei", "synchronize": "Synchronisieren",
                   "download_only": "Nur herunterladen",
                   "display_sync_status": "Synchronisationsstatus anzeigen",
                   "create_share_link": "Freigabelink erstellen",
                   "clear_output": "Ausgabe löschen", "language": "Deutsch"}
        }

        self.language = "en"

        self.init_ui()
        self.set_language(self.language)

        self.threads = []

    def set_language(self, language):
        self.language = language
        self.update_ui()

    def update_ui(self):
        tr = self.translations[self.language]
        self.file_menu.setTitle(tr["file_menu"])
        self.sync_button.setText(tr["synchronize"])
        self.download_only_button.setText(tr["download_only"])
        self.display_sync_status_button.setText(tr["display_sync_status"])
        self.create_share_link_button.setText(tr["create_share_link"])
        self.clear_button.setText(tr["clear_output"])

    def init_ui(self):
        layout = QVBoxLayout()

        # Create a menu bar
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        # Create the File menu
        self.file_menu = QMenu(self)
        menu_bar.addMenu(self.file_menu)

        # Add exit action to the File menu
        exit_action = self.file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

        # Create the Language menu
        language_menu = QMenu("Language", self)
        language_action_group = QActionGroup(self)

        menu_bar.addMenu(language_menu)

        for lang in self.translations.keys():
            lang_action = language_menu.addAction(self.translations[lang]["language"])
            lang_action.setCheckable(True)
            lang_action.setChecked(lang == self.language)
            lang_action.triggered.connect(partial(self.set_language, lang))
            language_action_group.addAction(lang_action)

        # Create a toolbar
        toolbar = QToolBar(self)
        self.addToolBar(toolbar)

        # Add buttons to toolbar
        self.sync_button = QPushButton()
        self.sync_button.clicked.connect(self.sync)
        toolbar.addWidget(self.sync_button)

        self.download_only_button = QPushButton()
        self.download_only_button.clicked.connect(self.download_only)
        toolbar.addWidget(self.download_only_button)

        self.display_sync_status_button = QPushButton()
        self.display_sync_status_button.clicked.connect(self.display_sync_status)
        toolbar.addWidget(self.display_sync_status_button)

        self.create_share_link_button = QPushButton()
        self.create_share_link_button.clicked.connect(self.create_share_link)
        toolbar.addWidget(self.create_share_link_button)

        self.clear_button = QPushButton()
        self.clear_button.clicked.connect(self.clear_output)
        layout.addWidget(self.clear_button)

        self.output = QPlainTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(self.output)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def update_output(self, text):
        self.output.appendPlainText(text)

    def sync(self):
        self.output.appendPlainText("\nSynchronizing OneDrive...")
        sync_thread = SyncThread(["onedrive", "--synchronize"])
        sync_thread.output_signal.connect(self.update_output)
        sync_thread.start()
        self.threads.append(sync_thread)

    def download_only(self):
        self.output.appendPlainText("\nSynchronizing OneDrive with Download Only...")
        download_only_thread = SyncThread(["onedrive", "--synchronize", "--download-only"])
        download_only_thread.output_signal.connect(self.update_output)
        download_only_thread.start()
        self.threads.append(download_only_thread)

    def display_sync_status(self):
        self.output.appendPlainText("\nDisplaying OneDrive sync status...")
        sync_thread = SyncThread(["onedrive", "--display-sync-status"])
        sync_thread.output_signal.connect(self.update_output)
        sync_thread.start()
        self.threads.append(sync_thread)

    def create_share_link(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)  # Pour sélectionner un fichier
        # file_dialog.setFileMode(QFileDialog.Directory)  # Pour sélectionner un dossier

        if file_dialog.exec():
            file_name = file_dialog.selectedFiles()[0]  # Récupère le fichier ou le dossier sélectionné
            onedrive_path = os.path.relpath(file_name, "/home/andrea/OneDrive")  # Obtenir le chemin relatif à OneDrive
            onedrive_path = onedrive_path.replace("\\", "/")  # Remplacer les antislashs par des slashs
            self.output.appendPlainText(f"\nCreating share link for '{onedrive_path}'...")
            sync_thread = SyncThread(["onedrive", "--create-share-link", onedrive_path,
                                      "--verbose"])
            sync_thread.output_signal.connect(self.update_output)
            sync_thread.start()
            self.threads.append(sync_thread)

    def clear_output(self):
        self.output.clear()
