import subprocess
from PySide6.QtCore import QThread, Signal


class SyncThread(QThread):
    output_signal = Signal(str)

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        try:
            process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            while True:
                line = process.stdout.readline()
                if not line:
                    break
                self.output_signal.emit(line.strip())
            process.wait()
        except Exception as e:
            self.output_signal.emit(f"Error: {e}")
