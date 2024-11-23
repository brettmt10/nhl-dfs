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
        self.setStyleSheet("background-color: #000000;")
        
        # set central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # get matchup data
        self.matchups = self.get_all_matchups()
        self.num_games = self.get_num_games()
        
        # main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # scrollable function for matchup bar
        matchups_area = QScrollArea()
        matchups_area.setStyleSheet("QScrollArea { background-color: #111111; border: 1px solid #000000; }")
        matchups_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        matchups_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        matchups_area.setFixedHeight(96)
        
        # matchup bar
        matchups_scroll_widget = QWidget()
        matchups_scroll_widget.setStyleSheet("background-color: #111111;")
        matchups_scroll_layout = QHBoxLayout(matchups_scroll_widget)
        matchups_scroll_layout.setContentsMargins(0, 0, 0, 0)
        matchups_scroll_layout.setSpacing(1)
        
        # matchup containers
        for i in range(15):
            matchup_section_button = QPushButton(chr(65 + i))
            matchup_section_button.setStyleSheet("""
                QPushButton {
                    background-color: #333333;
                    color: white;
                    border: 1px solid black;
                    border-radius: 0px;
                }
                QPushButton:hover {
                    background-color: #333333;
                }
                QPushButton:pressed {
                    background-color: #333333;
                }
            """)
            matchup_section_button.setFixedWidth(200)
            matchup_section_button.setFixedHeight(96)
            matchup_section_button.clicked.connect(lambda checked, l=chr(65 + i): print(l))
            matchups_scroll_layout.addWidget(matchup_section_button)
            
        # create second bar for selected matchup
        selected_matchup_area = QWidget()
        selected_matchup_area.setStyleSheet("background-color: #111111;")
        selected_matchup_area.setFixedHeight(96)
        selected_matchup_layout = QHBoxLayout(selected_matchup_area)
        selected_matchup_layout.setContentsMargins(0, 0, 0, 0)
        selected_matchup_layout.setSpacing(1)
        
        # create two containers for second bar
        for i in range(2):
            team_container = QWidget()
            team_container.setStyleSheet("background-color: #111111;")
            selected_matchup_layout.addWidget(team_container)
            
            # Add vertical line after first container
            if i == 0:
                line = QWidget()
                line.setStyleSheet("background-color: white;")
                line.setFixedWidth(1)  # 1px wide line
                selected_matchup_layout.addWidget(line)
            
        # create bottom container that fills remaining space
        player_data_container = QWidget()
        player_data_container.setStyleSheet("background-color: #ffffff;")
        player_data_layout = QHBoxLayout(player_data_container)
        player_data_layout.setContentsMargins(0, 0, 0, 0)
        player_data_layout.setSpacing(1)  # maintains the 1px gap like other containers

        # create two equal-width containers
        for i in range(2):
            team_container = QWidget()
            team_container.setStyleSheet("background-color: #0c0c0c;")
            player_data_layout.addWidget(team_container)
                    
        # add all widgets to main layout
        main_layout.addWidget(matchups_area)
        matchups_scroll_widget.setFixedHeight(96)
        matchups_area.setWidget(matchups_scroll_widget)

        main_layout.addWidget(matchups_area)
        main_layout.addWidget(selected_matchup_area)
        main_layout.addWidget(player_data_container)      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())