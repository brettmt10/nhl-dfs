import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QHBoxLayout, QVBoxLayout, QPushButton, QLabel)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NHL DFS Assistant")
        self.showMaximized()  # Set to fullscreen mode

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())