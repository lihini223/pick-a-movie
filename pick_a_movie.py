from requests import get
from requests.models import Response
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

Response = get(url)

# print(Response.text[:500])

html_soup = BeautifulSoup(Response.text, 'html.parser')

print(type(html_soup))

movie_containers = html_soup.findAll('div', class_='lister-item mode-advanced')


