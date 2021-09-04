from requests import get
from requests.models import Response
from bs4 import BeautifulSoup

url = 'https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

Response = get(url)

# print(Response.text[:500])

html_soup = BeautifulSoup(Response.text, 'html.parser')

print(type(html_soup))

movie_containers = html_soup.findAll('div', class_='lister-item mode-advanced')

print(type(movie_containers))
print(len(movie_containers))

first_movie = movie_containers[0]
first_name = first_movie.h3.a.text
first_year = (first_movie.h3.find(
    'span', class_='lister-item-year text-muted unbold')).text
first_imdb = float(first_movie.strong.text)
first_mscore = (first_movie.find('span', class_='metascore favorable')).text
first_votes = first_movie.find('span', attrs = {'name':'nv'})
print(first_mscore)
