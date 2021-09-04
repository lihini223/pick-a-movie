from requests import get
from requests.models import Response
from bs4 import BeautifulSoup
import pandas as pd
from random import randint

# Lists to save scraping data
movie_names = []
years = []
imdb_ratings = []
metascore = []
votes = []


url = 'https://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

Response = get(url)

# print(Response.text[:500])

html_soup = BeautifulSoup(Response.text, 'html.parser')

# print(type(html_soup))

movie_containers = html_soup.findAll('div', class_='lister-item mode-advanced')

# print(type(movie_containers))
# print(len(movie_containers))

first_movie = movie_containers[0]
first_name = first_movie.h3.a.text
first_year = (first_movie.h3.find(
    'span', class_='lister-item-year text-muted unbold')).text
first_imdb = float(first_movie.strong.text)
first_mscore = (first_movie.find('span', class_='metascore favorable')).text
first_votes = int(first_movie.find('span', attrs={'name': 'nv'})['data-value'])
# print(f'Fisrt Movie : {first_name} \n first_year : {first_year} \n first_imdb : {first_imdb} \n first_mscore : {first_mscore} \n first_votes : {first_votes} \n')


# Extracting data from individual movie container
for container in movie_containers:
    if container.find('div', class_='ratings-metascore') is not None:
        # Append names
        name = container.h3.a.text
        movie_names.append(name)

        # Append years
        year = container.h3.find(
            'span', class_='lister-item-year text-muted unbold').text
        years.append(year)

        # Append imdb
        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)

        # Append metascore
        m_score = (container.find('span', class_='metascore')).text
        metascore.append(m_score)

        # Append Vote
        vote = int(container.find('span', attrs={'name': 'nv'})['data-value'])
        votes.append(vote)

movies_df = pd.DataFrame({'movie': movie_names,
                          'year': years,
                          'imdb': imdb_ratings,
                          'metascore': metascore,
                          'Vote': votes})


# print(movies_df)
magic_number = randint(1, 40)
Selected_movie = movies_df.iloc[magic_number]

print("\nWohoo! Here's a top movie to watch this weekend \n ")
print(Selected_movie)
# print(f'{Selected_movie = }\n')
