import os
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QPlainTextEdit, QFileDialog

from sync_thread import SyncThread


class OneDriveGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.clear_button = None
        self.output = None
        self.setWindowTitle("OneDrive GUI")
        self.init_ui()
        self.threads = []

    def init_ui(self):
        layout = QVBoxLayout()

        sync_button = QPushButton("Synchronize")
        sync_button.clicked.connect(self.sync)
        layout.addWidget(sync_button)

        download_only_button = QPushButton("Download Only")
        download_only_button.clicked.connect(self.download_only)
        layout.addWidget(download_only_button)

        display_sync_status_button = QPushButton("Display Sync Status")
        display_sync_status_button.clicked.connect(self.display_sync_status)
        layout.addWidget(display_sync_status_button)

        create_share_link_button = QPushButton("Create Share Link")
        create_share_link_button.clicked.connect(self.create_share_link)
        layout.addWidget(create_share_link_button)

        self.clear_button = QPushButton("Clear Output", self)
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
