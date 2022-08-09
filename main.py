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

baseUrl = 'https://rusdorznak.ru'
uslugiUrl = 'https://rusdorznak.ru/uslugi'
# cat_dict = {}   

category_urls= []
def main():
    req = requests.get(uslugiUrl)
    
    
    soup = BeautifulSoup(req.text, "lxml")
    catalog_items = soup.find_all("a", class_ = "production__item")
    for catalog_item in catalog_items:
        name = catalog_item.text.strip()
        url = baseUrl + catalog_item.attrs["href"].strip()
        # print(name)
        # print(baseUrl + catalog_item.attrs["href"].strip())
        # category_urls.append(url)
        # ParsePage(baseUrl + catalog_item.attrs["href"].strip())
        # print(baseUrl + catalog_item.attrs["href"].strip())
        ParseCards(baseUrl + catalog_item.attrs["href"].strip())
        # for category_url in category_urls:

      
            


# sub_cat_dict = []
def ParsePage(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    page_catalog = soup.find_all("a", class_ = "production__item")
    for catalog_item in (page_catalog):
        sub_cat_name = catalog_item.text.strip()
        sub_cat_url = url + catalog_item.attrs["href"].strip()
        # sub_cat_dict[sub_cat_name] = sub_cat_url
        # print(sub_cat_name)
        # print(url + catalog_item.attrs["href"].strip())
        ParseSigns(baseUrl + catalog_item.attrs["href"].strip())

# sign_dict= {}
def ParseSigns(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    signs_catalog = soup.find_all("a", class_ = "card-block__top")
    for signs_name in signs_catalog:
        sign_name = signs_name.text.strip()
        sign_href = baseUrl + signs_name.attrs["href"].strip()
        # print(baseUrl + signs_name.attrs["href"].strip())
        GetSignInfo(sign_href)
        # print(baseUrl + sign_name.attrs["href"].strip())
        # sign_url = sign_name.
        # print(signs_name.text.strip())

def ParseCards(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    cards_catalog = soup.find('div', class_='wrapper').find_all("form", class_= "product-list__card")
    for card_names in cards_catalog:
        name = card_names.find('a', class_='product-list__description-title').text.strip()
        # card_url = baseUrl + card_names.attrs['href'].strip()
        print(card_names.attrs['href'].strip())
        # GetSignInfo(card_url)
        # print('---------------')
        # count += 1
        # print(name)

def GetSignInfo(url):
    # print(url)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    sign_info = soup.find('ul', class_= 'c-dropdown__list')
    if sign_info == None:
        pass  
    else:
        attributes = sign_info.find_all('li', class_ = 'c-dropdown__item')
        for attribute_name in attributes:
            print(attribute_name.text)  

if __name__ == "__main__":
    main()

# print(category_urls)