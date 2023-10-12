import requests
import pandas as pd
from bs4 import BeautifulSoup

response = requests.get("https://amazing-creature.blogspot.com/2012/08/funny-cats-part-9-52-pics.html")
# print(response)
soup = BeautifulSoup(response.content,'html.parser')
# print(soup)

names = soup.find_all('div',class_="main section")
print(names.get_text())
