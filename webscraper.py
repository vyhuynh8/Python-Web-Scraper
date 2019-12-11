import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://en.wikipedia.org/wiki/Atlantic_Records_discography').text
soup = BeautifulSoup(page, 'lxml')
table = soup.find('table', {'class':'wikitable sortable'})

artists = []
catalog = []
album = []

rows = table.find_all('tr')
for row in rows:
	cells = row.find_all('td')
	if len(cells) >= 3:
		catalog.append(cells[0].get_text().rstrip())
		artists.append(cells[1].get_text().rstrip())
		album.append(cells[2].get_text().rstrip())

discography = pd.DataFrame(
	{
		'Catalog' : catalog,
		'Artist' : artists,
		'Album' : album
	})

discography.to_csv("discography.csv")