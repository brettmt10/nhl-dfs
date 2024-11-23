import requests
from bs4 import BeautifulSoup
import teamLinks
import pandas as pd
from io import StringIO
from nhlpy import NHLClient
from datetime import datetime, timedelta
import pytz

class Scraper():
    def __init__(self):
        self.client = NHLClient()
        self.schedule = self.client.schedule.get_schedule(date="2024-11-22").get('games')
        self.num_games = len(self.schedule)
        self.matchups = []
            
    def get_daily_matchups(self):
        return self.matchups
    
    def get_num_games(self):
        return self.num_games
    
    # get time for each match up, based on utc values
    def get_matchup_time(self, match_time):
        # parse UTC string
        time = datetime.strptime(match_time, '%Y-%m-%dT%H:%M:%SZ')
        time = pytz.utc.localize(time)
        
        # convert format time into EST
        timezone = pytz.timezone('America/New_York')
        formatted_match_time = time.astimezone(timezone).strftime('%I:%M %p')
        
        return(formatted_match_time)
    
    
    # get matchup info (not player data)
    def get_matchup(self, schedule, i):
        # json paths to extract matchups
        away_team = schedule[i].get('awayTeam').get('placeName')['default'].lower()
        home_team = schedule[i].get('homeTeam').get('placeName')['default'].lower()
        logo_away_team = schedule[i].get('homeTeam').get('logo')
        logo_home_team = schedule[i].get('awayTeam').get('logo')
        
        matchup_utc = schedule[i].get('startTimeUTC')
        matchup_start_time = self.get_matchup_time(matchup_utc)
        
        return {"away_team": {"city": away_team, "logo": logo_away_team},
                "home_team": {"city": home_team, "logo": logo_home_team},
                "start_time": matchup_start_time}
        
    # get each matchup's info 
    def get_all_matchups(self):
        for i in range(self.num_games):
            self.matchups.append(self.get_all_matchups(self.schedule, i))
                
    def get_team_player_data():
        # source set up
        url = teamLinks.links["seattle"]
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "lxml")

        # scrape wanted elements
        html_div = soup.find('div', {"id": "div_player_stats"}) # div containing the table
        html_table_headers = html_div.find('table').find('thead').find_all('tr')[1].find_all('th') # headers of table
        html_table_body = html_div.find('table') # body of the table
        html_table_str = StringIO(str(html_table_body)) # table as a StringIO input for pandas

        # create clean list of headers
        clean_headers = []
        for header_value in html_table_headers:
            clean_headers.append(header_value.text.strip())

        # convert to pandas, replace headers with clean headers
        player_data = pd.DataFrame(pd.read_html(html_table_str)[0])
        player_data.columns=clean_headers

        # remove unneccesary columns
        player_data = player_data.drop(["Rk", "Awards"], axis=1)

        # remove team totals row
        player_data = player_data.iloc[:-1]