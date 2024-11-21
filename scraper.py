import requests
from bs4 import BeautifulSoup
import teamLinks
import pandas

url = teamLinks.calgary
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "lxml")

player_stats = pandas.DataFrame()

# scrape wanted elements
html_div = soup.find('div', {"id": "div_player_stats"}) # div containing the table
html_table_headers = html_div.find('table').find('thead').find_all('tr')[1].find_all('th') # headers of table
html_table_body = html_div.find('table').find('tbody') # body of the table
html_rows = html_table_body.find_all('tr') # all rows of the table

# put all data including headers into list of lists
headers = []
for header_value in html_table_headers:
    headers.append(header_value.text.strip())
    
print(headers)