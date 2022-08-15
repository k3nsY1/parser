import requests
from bs4 import BeautifulSoup
url='https://rusdorznak.ru/znaki-vertikalnoj-razmetki/znak-vertikalnaya-razmetka-23'
req = requests.get(url)
soup = BeautifulSoup(req.text, "lxml")
card_block = soup.find('div', class_= 'card-block__left').find_all('div', class_= 'card-block__choices')
print(card_block)