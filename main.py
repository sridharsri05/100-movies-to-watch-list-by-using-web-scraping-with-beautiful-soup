import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
response_data = response.text

soup = BeautifulSoup(response_data, "html.parser")

all_movies = soup.find_all("h3", "title")
movie_titles = [movie.getText() for movie in all_movies]
movies = movie_titles[::-1]

with open("movie_name_list", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
