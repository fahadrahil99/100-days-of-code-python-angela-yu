import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
data = response.text

soup = BeautifulSoup(data,"html.parser")
soup.encode('utf-8')
movies_list_elements = soup.find_all(name="h3",class_ = "title")
movies_list=[movies.getText() for movies in movies_list_elements]


ordered_list = movies_list[::-1]
print(ordered_list)
for movies in ordered_list:
    with open("ordered_list.txt","a",encoding="utf-8") as file:
        file.write(movies + "\n")
