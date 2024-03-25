import csv

from bs4 import BeautifulSoup
import requests
from Home import Home


def create(homes2):
    with open('home.csv', 'w', encoding='UTF-8', newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow(['header_name', 'price', 'price_for_m2'])
        for i in range(len(homes2)):
            writer.writerow([homes2[i].header_name, homes2[i].price, homes2[i].price_for_m2])


url = 'https://www.otodom.pl/pl/wyniki/sprzedaz/mieszkanie/pomorskie/gdynia/gdynia/gdynia?priceMax=600000&viewType=listing'
page = requests.get(url, headers={'User-Agent': 'Mozilla/5'})

soup = BeautifulSoup(page.content, 'html.parser')
listATags = soup.find_all('section')  # lista ogłoszeń
listBTags = soup.find_all('div', attrs={'data-testid': 'listing-item-header'})  # lista div gdzie są ceny
listCTags = soup.find_all('p', attrs={'data-cy': 'listing-item-title'})  # lista akapitów z nazwą
price = listBTags[0].find('span').get_text()
pricesList = []  # tu będzie cana i cena za m2
for x in range(0, len(listBTags)):
    pricesList.append(listBTags[x].find('span').get_text())  # złapanie spanów(tam gdzie jest cena i cana za m2)

pricesList2 = []
prices = []  # ceny
pricesM = []  # ceny za m2
for x in range(0, len(pricesList)):
    pricesList2 = (pricesList[x].rsplit('zł'))  # rodzielenie ceny od ceny za m2 i reszty
    if len(pricesList2) != 1:  # sprawdzedznie czy nie ma "sprawdz cene"
        pricesList2[0] = pricesList2[0].replace(u'\xa0', u'')
        prices.append(pricesList2[0])  # złapanie ceny
        pricesList2[1] = pricesList2[1].replace(u'\xa0', u'')
        pricesM.append(pricesList2[1])  # złapanie ceny za m2
    else:
        del listCTags[x]  # jeżeli jest zapytaj o cenę to usuwamy z listy nazw nazwe tego ogłoszenia

homes = []

for x in range(0, len(prices)):
    home = Home(listCTags[x].get_text(), prices[x], pricesM[x])
    homes.append(home)

slownik: dict = {}
for x in range(0, len(homes)):
    slownik[x] = [homes[x].header_name, homes[x].price, homes[x].price_for_m2]

create(homes)
