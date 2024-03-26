from bs4 import BeautifulSoup
import requests

url = 'https://nonsa.pl/wiki/Tiger_Bonzo'
page = requests.get(url)

# print(page.content)
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify())
listATags = soup.find_all('a', href=True)
#print(listATags)

linklist = []

for x in range(0, len(listATags)):
    #print(listATags[x].get('href'))
    linklist.append(listATags[x].get('href'))

print(linklist)
