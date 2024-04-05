### imports
import requests
from bs4 import BeautifulSoup

start = 1962
finish = 1963

path = "farmers_leage_dataset.csv"

leagues = ['eng-premier-league-', 'ita-serie-a-', 'por-primerialiga-', 'esp-primera-division-', 'fra-ligue-1-', 'ned-eredivisie-']

baseurl_start = 'www.worldfootball.net/schedule/'
baseurl_end = '-spieltag/38/'

# for league in leagues:

#     for i in range(61):
#         year = f"{start}-{finish}"
#         start += 1
#         finish += 1
#         url = baseurl_start + league + year + baseurl_end
#         page = requests.get(url)
#         soup = BeautifulSoup(page.text)
#         table = soup.find_all("table", {"class": "standard_tabelle"})


#     start = 1962
#     finish = 1963
    
'''
[
    {
        champion: man city,
        champion_points = x,
        champ_margin = y (x - d), 
        list_teams = []
    }
]
'''


page = requests.get('http://www.worldfootball.net/schedule/eng-premier-league-2022-2023-spieltag/38/')
soup = BeautifulSoup(page.text)
table = soup.find_all("table", {"class": "standard_tabelle"})
table = table[1]
test = table.find_all("a")
test2 = [i['title'] for i in test]
for x in test2:
    print(x)