import requests
from bs4 import BeautifulSoup
import teamLinks
import pandas as pd
from io import StringIO

# source set up
url = teamLinks.calgary
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