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

def main():
    # Категории
    req = requests.get(uslugiUrl)
    soup = BeautifulSoup(req.text, "lxml")
    catalog_items = soup.find_all("a", class_ = "production__item")
    for catalog_item in catalog_items:
        name = catalog_item.text.strip()
        print(name)
        GetSubCategory(baseUrl + catalog_item.attrs["href"].strip())

# Подкатегории
def GetSubCategory(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    page_catalog = soup.find_all("a", class_ = "production__item")
    for catalog_item in (page_catalog):
        sub_cat_name = catalog_item.text.strip()
        print(sub_cat_name)
        GetSignPages(baseUrl + catalog_item.attrs["href"].strip())

# Знаки и ссылки
def GetSignsInAllPages(page, url):
    req = requests.get(url + '?page={0}#category_product-list'.format(page))
    soup = BeautifulSoup(req.text, "lxml")
    signs_catalog = soup.find_all("a", class_ = "card-block__top")
    for signs_name in signs_catalog:
        sign_name = signs_name.text.strip()
        sign_href = baseUrl + signs_name.attrs["href"].strip()
        print(sign_name)
        print(sign_href)
        GetSignInfo(sign_href)


# Получаем страницы знаков
def GetSignPages(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    pages = soup.find('ul', class_ = 'pagination justify-content-center')
    if pages == None:
        signs_catalog = soup.find_all("a", class_ = "card-block__top")
        for signs in signs_catalog:
            sign_name = signs.text.strip()
            print(sign_name)
            pass
    else:
        all_pages = int(pages.find_all('li')[-2].text)
        for page in range(1, all_pages):
            GetSignsInAllPages(page, url)

# Знаки без подкатегории
def GetCards(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    cards_catalog = soup.find('div', class_='wrapper').find_all("form", class_= "product-list__card")
    for card_names in cards_catalog:
        name = card_names.find('a', class_='product-list__description-title').text.strip()
        # card_url = baseUrl + card_names.attrs['href'].strip()
        # print(card_names.attrs['href'].strip())
        # GetSignInfo(card_url)
        # print('---------------')
        # count += 1
        print(name)

# Инофрмация о знаке
def GetSignInfo(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    
    size_type = soup.find('div', class_= 'card-block__left')
    if size_type == None:
        pass  
    else:
        sizes = size_type.find_all('li', class_ = 'c-dropdown__item')
        for size_name in sizes:
            print(size_name.text)
        types = size_type.find_all('div', class_ = 'card-block__choice')
        for type_name in types:
            print(type_name.text.strip())    

if __name__ == "__main__":
    main()

