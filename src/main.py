import sys
from PySide6.QtWidgets import QApplication

from one_drive_gui import OneDriveGUI

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OneDriveGUI()
    window.show()
    sys.exit(app.exec())
