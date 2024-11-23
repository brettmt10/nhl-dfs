import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QHBoxLayout, QVBoxLayout, QPushButton, QLabel,
                             QScrollArea)
from PySide6.QtCore import Qt

from scraper import Scraper

class MainWindow(QMainWindow, Scraper):
    def __init__(self):
        super().__init__()
        Scraper.__init__(self) # get functions from custom scraper
        
        self.setWindowTitle("NHL DFS Assistant")
        
        # dark gray bg
        self.setStyleSheet("background-color: #1a1a1a;")
        
        # set central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # get matchup data
        self.matchups = self.get_daily_matchups()
        self.num_games = self.get_num_games()
        
        # main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # scrollable function for matchup bar
        scroll_area = QScrollArea()
        scroll_area.setStyleSheet("QScrollArea { background-color: #2a2a2a; border: none; }")
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll_area.setFixedHeight(96)
        
        # matchup bar
        scroll_widget = QWidget()
        scroll_widget.setStyleSheet("background-color: #2a2a2a;")
        scroll_layout = QHBoxLayout(scroll_widget)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(1)
        
        # display label for button clicks
        self.display_label = QLabel()
        self.display_label.setStyleSheet("color: white; font-size: 24px;")
        self.display_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # matchup containers
        for i in range(15):
            button = QPushButton(chr(65 + i))
            button.setStyleSheet("background-color: #333333; color: white; border: none;")
            button.setFixedWidth(200)
            button.setFixedHeight(96)
            button.clicked.connect(lambda checked, l=chr(65 + i): self.display_label.setText(l))
            scroll_layout.addWidget(button)
        
        # add widgets
        scroll_widget.setFixedHeight(96)
        scroll_area.setWidget(scroll_widget)

        main_layout.addWidget(scroll_area)
        main_layout.addWidget(self.display_label)
        main_layout.addStretch()       

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())