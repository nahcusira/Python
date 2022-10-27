from bs4 import BeautifulSoup
import requests


url = 'https://cataas.com/#/'

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
print([tag.name for tag in soup.find_all()])
# print([str(tag) for tag in soup.find_all()])