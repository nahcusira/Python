from bs4 import BeautifulSoup
import requests
import csv


url = 'https://www.us-cert.gov/ncas/alerts/2022'

r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")

links = []

for link in soup.find_all('a'):
    a = link.get('href')
    if a != None:
        if a.startswith('/ncas/alerts/aa22'):
            links.append(a)
with open('new.csv','w') as file:
    for link in links:
        file.write(link)
        





