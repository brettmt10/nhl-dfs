import sys
import requests

from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, 
                             QHBoxLayout, QVBoxLayout, QPushButton, QLabel,
                             QScrollArea, QSpacerItem, QSizePolicy)
from PySide6.QtCore import Qt, QByteArray
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtGui import QPixmap, QFont

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
        self.main_layout = QVBoxLayout(central_widget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)
        
        self.matchups_area = QScrollArea()
        self.matchups_scroll_widget = QWidget()
        self.selected_matchup_area = QWidget()
        self.player_data_container = QWidget()
        
        
    def config_matchups_bar(self):
        # scrollable function for matchup bar
        self.matchups_area.setStyleSheet("QScrollArea { background-color: #111111; border: 1px solid #000000; }")
        self.matchups_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.matchups_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.matchups_area.setFixedHeight(96)
        
        # matchups layout with widget    
        self.matchups_scroll_widget.setStyleSheet("background-color: #111111;")
        self.matchups_scroll_widget.setFixedHeight(96)
        matchups_scroll_layout = QHBoxLayout(self.matchups_scroll_widget)
        matchups_scroll_layout.setContentsMargins(0, 0, 0, 0)
        matchups_scroll_layout.setSpacing(1)
        
        # container for each matchup
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
            matchup_section_button.clicked.connect(lambda checked: self.change_selected_matchup_bar())
            matchups_scroll_layout.addWidget(matchup_section_button)
            
    def config_selected_matchup_bar(self):
        # create second bar for selected matchup
        self.selected_matchup_area.setStyleSheet("background-color: #111111;")
        self.selected_matchup_area.setFixedHeight(96)
        selected_matchup_layout = QHBoxLayout(self.selected_matchup_area)
        selected_matchup_layout.setContentsMargins(0, 0, 0, 0)
        selected_matchup_layout.setSpacing(1)
        
        # create two containers for each team in second bar
        for i in range(2):
            team_container = QWidget()
            team_container.setStyleSheet("background-color: #111111;")
            selected_matchup_layout.addWidget(team_container)
            
            # vertical line between two selected teams
            if i == 0:
                line = QWidget()
                line.setStyleSheet("background-color: white;")
                line.setFixedWidth(1)
                selected_matchup_layout.addWidget(line)
      
    def config_team_player_data_sections(self):  
        # create bottom container that fills remaining space for player data of selected teams
        self.player_data_container.setStyleSheet("background-color: #ffffff;")
        player_data_layout = QHBoxLayout(self.player_data_container)
        player_data_layout.setContentsMargins(0, 0, 0, 0)
        player_data_layout.setSpacing(1)  # maintains the 1px gap like other containers

        # create a container for the two selected teams that fills the bottom container
        for i in range(2):
            team_container = QWidget()
            team_container.setStyleSheet("background-color: #0c0c0c;")
            player_data_layout.addWidget(team_container)
    
    # when a game is selected, change the background colors of the selected matchup containers
    def change_selected_matchup_bar_backgrounds(self):
        team_containers = [self.selected_matchup_area.layout().itemAt(i).widget() 
                            for i in (0, 2)]
        
        team_containers[0].setStyleSheet(f"background-color: blue;")
        team_containers[1].setStyleSheet(f"background-color: green;")
        
    def change_selected_matchup_bar_name_and_logo(self):
        team_containers = [self.selected_matchup_area.layout().itemAt(i).widget() 
                            for i in (0, 2)]

        for idx, container in enumerate(team_containers):
            if idx == 0:
                away_layout = QHBoxLayout(container)
                away_layout.setAlignment(Qt.AlignVCenter)
                away_layout.setContentsMargins(40,0,10,0)
                away_layout.setSpacing(30)
                
                # Create label for team name
                team_record = QLabel("11-1-1")
                font = QFont("Arial", 20, QFont.Weight.Bold)
                font.setItalic(True)
                team_record.setFont(font)
                team_record.setStyleSheet("""
                    color: white;
                    font-weight: 900;
                """)
                
                away_layout.addWidget(team_record)

                # Create label for team name
                team_name = QLabel("WINNIPEG")
                font = QFont("Arial", 50, QFont.Weight.Bold)
                font.setItalic(True)
                team_name.setFont(font)
                team_name.setStyleSheet("""
                    color: white;
                    font-weight: 900;
                """)

                away_layout.addWidget(team_name)
                                                                           
                logo_widget = QSvgWidget("./img/logo_winnipeg.svg")
                logo_widget.setFixedSize(100, 100)
                        
                renderer = logo_widget.renderer()
                renderer.setAspectRatioMode(Qt.KeepAspectRatio)

                away_layout.addWidget(logo_widget)

            else:
                pass
                
                  
    def change_selected_matchup_bar(self):
        self.change_selected_matchup_bar_backgrounds()
        self.change_selected_matchup_bar_name_and_logo()
        
    def create_gui(self):     
        # add all widgets to main layout
        self.config_matchups_bar()
        self.config_selected_matchup_bar()
        self.config_team_player_data_sections()
        self.main_layout.addWidget(self.matchups_area)
        self.matchups_area.setWidget(self.matchups_scroll_widget)
        self.main_layout.addWidget(self.matchups_area)
        self.main_layout.addWidget(self.selected_matchup_area)
        self.main_layout.addWidget(self.player_data_container)      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.create_gui()
    window.showMaximized()
    sys.exit(app.exec())