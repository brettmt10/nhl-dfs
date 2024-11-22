import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QHBoxLayout, QVBoxLayout, QPushButton, QLabel)
from PySide6.QtCore import Qt

class LetterBox(QPushButton):
    def __init__(self, letters, parent=None):
        super().__init__(parent)
        self.letters = letters
        self.setText(letters)
        self.setFixedSize(50, 50)
        self.setStyleSheet("""
            QPushButton {
                border: 2px solid black;
                border-radius: 5px;
                background-color: white;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Letter Boxes")
        self.setMinimumSize(600, 400)

        # Create main widget and layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)

        # Create horizontal layout for letter boxes
        box_layout = QHBoxLayout()
        box_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # Sample letter pairs
        letter_pairs = ["AB", "CD", "EF", "GH", "IJ", "KL"]
        
        # Create letter boxes
        for letters in letter_pairs:
            box = LetterBox(letters)
            box.clicked.connect(lambda checked, l=letters: self.show_text(l))
            box_layout.addWidget(box)

        # Add box layout to main layout
        main_layout.addLayout(box_layout)

        # Create text display label
        self.text_display = QLabel()
        self.text_display.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.text_display.setStyleSheet("""
            QLabel {
                font-size: 18px;
                margin: 20px;
                min-height: 200px;
            }
        """)
        main_layout.addWidget(self.text_display)

    def show_text(self, letters):
        # Dictionary of text to display for each letter pair
        text_dict = {
            "AB": "Alpha and Beta are the first two letters of the Greek alphabet.",
            "CD": "CD-ROM was a revolutionary storage medium in the 1990s.",
            "EF": "EF stands for 'Extra Fine' in pencil grades.",
            "GH": "GH is commonly used as an abbreviation for 'Growth Hormone'.",
            "IJ": "IJ is a digraph found in Dutch spelling.",
            "KL": "KL is the airport code for Kuala Lumpur International Airport."
        }
        self.text_display.setText(text_dict.get(letters, "No text available for these letters."))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())