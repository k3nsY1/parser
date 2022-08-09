from array import array
from asyncio import tasks
from cgitb import text
from queue import Empty
import string
from unicodedata import category
from webbrowser import get
from bs4 import BeautifulSoup
import asyncio
import aiohttp
import http 
import requests

from categoty import GetCategory

baseUrl = 'https://rusdorznak.ru'
uslugiUrl = 'https://rusdorznak.ru/uslugi'
# cat_dict = {}   

category_urls= []
def main():
    GetCategory(uslugiUrl, baseUrl)
        

      
            





# sign_dict= {}


def ParseCards(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    card_info = soup.find('div', class_= 'product-list__description')
    # print(card_info.text)
    # cards_catalog = soup.find('div', class_='wrapper').find_all("form", class_= "product-list__card")
    # for card_names in cards_catalog:
    #     card_name = card_names.find('a', class_='product-list__description-title').text.strip()
    # cards_hrefs = soup.find('section', class_= 'container product-list').find_all('href')
    # for cards_href in cards_hrefs:
    #     # card_href = card_names.find('href', class_ = 'product-list__description').text.strip()
        # print(cards_href.text)
        # card_url = baseUrl + card_names.attrs['href'].strip()
        
        # GetSignInfo(card_url)

        # print(name)



if __name__ == "__main__":
    main()

# print(category_urls)