from array import array
from asyncio import tasks
import base64
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
catalogUrl = 'https://rusdorznak.ru/uslugi'
signs = []
inner_data= {}
# inner_data= []
# data.append({
#         'Название':'name,
#         'Описание':'Тест полный словарь',
#         'Чертеж': 'image in encoded to binary',
#         'Категория': 'Знак',
#         'Категория 2': 'Тест полный словарь',
#         'Поставщик': 'https://base64.guru/converter/encode/image',
#         'Цена': '1234567',
#         'Атрибуты': {
#             'Название атрибута':'Значение'
#         })     
def main():
    # Категории
    
    req = requests.get(catalogUrl)
    soup = BeautifulSoup(req.text, "lxml")
    catalog_items = soup.find_all("a", class_ = "production__item")
    for catalog_item in catalog_items:
        name = catalog_item.text.strip()
        inner_data.update({
            'Категория':'Дорожные знаки',
            'Категория 2': name})
        # print(name)
        GetCards(baseUrl + catalog_item.attrs["href"].strip(), inner_data)
        signs.append(inner_data)
        GetSubCategory(baseUrl + catalog_item.attrs["href"].strip(), inner_data)
        signs.append(inner_data)
        
    

# Подкатегории
def GetSubCategory(url, inner_data):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    try:
        page_catalog = soup.find_all("a", class_ = "production__item")
        for catalog_item in (page_catalog):
            sub_cat_name = catalog_item.text.strip()
            # print(sub_cat_name)
            inner_data.update({'Категория 3': sub_cat_name})
            # print(baseUrl + catalog_item.attrs["href"].strip())
            GetSignPages(baseUrl + catalog_item.attrs["href"].strip(), inner_data)
            # return inner_data
    except:
        # inner_data.update({'Категория 3': ''})
        # return inner_data
        pass
        


# Знаки и ссылки
def GetSignsInAllPages(page, url, inner_data):
    req = requests.get(url + '?page={0}#category_product-list'.format(page))
    soup = BeautifulSoup(req.text, "lxml")
    signs_catalog = soup.find_all("a", class_ = "card-block__top")
    for signs_name in signs_catalog:
        sign_name = signs_name.text.strip()
        sign_href = baseUrl + signs_name.attrs["href"].strip()
        inner_data.update({
            'Название': sign_name,
            'Поставщик': sign_href
            })
        # print(sign_name)
        # print(sign_href)
        inner_data = GetSignInfo(sign_href, inner_data)
        return inner_data

def GetSignWithoutPages(url, inner_data):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    signs_catalog = soup.find_all("a", class_ = "card-block__top")
    for signs_name in signs_catalog:
        sign_name = signs_name.text.strip()
        sign_href = baseUrl + signs_name.attrs["href"].strip()
        inner_data.append({
            'Название': sign_name,
            'Поставщик': sign_href
            })
        # print(sign_name)
        # print(sign_href)
        GetSignInfo(sign_href, inner_data)
        

# Получаем страницы знаков
def GetSignPages(url, inner_data):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    pages = soup.find('ul', class_ = 'pagination justify-content-center')
    if pages == None:
        
        GetSignWithoutPages(url, inner_data)
        
        # signs_catalog = soup.find_all("a", class_ = "card-block__top")
        # for signs in signs_catalog:
        #     sign_name = signs.text.strip()
            # print(sign_name)
    else:
        all_pages = int(pages.find_all('li')[-2].text)
        for page in range(1, all_pages):
            GetSignsInAllPages(page, url, inner_data)
            

# Знаки без подкатегории
def GetCards(url, inner_data):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    cards_catalog = soup.find('div', class_='wrapper').find_all("div", class_= "product-list__card-content")
    for card_names in cards_catalog:
        name = card_names.find('a', class_='product-list__description-title').text.strip()
        # print(name)
        card_url = baseUrl + card_names.find('a', class_='product-list__description-title').attrs['href'].strip()
        inner_data.update({
            'Название': name,
            'Поставщик': card_url
            })
        # print(card_url)
        GetCardsInfo(card_url, inner_data)
        

def GetCardsInfo(url, inner_data):
    # driver = selenium.driver()
    # driver.get(url)
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    try:
        list_name_attrs = soup.find('div', class_ ='card-block__left').find_all('div', class_= 'card-block__choices')
        for attr in list_name_attrs:
            #  Название типов
            attr_name = ListToString(attr.find('label', class_= "card-block__right-label card-label").text.split())
            # print(attr_name)
            inner_data.update({'Атрибуты':{
                attr_name: ''
            }})
            try:
                # Всплывающийся список
                list_attr_dropdown = attr.find_all('li', class_= 'c-dropdown__item')
                for attr_dropdown in list_attr_dropdown:
                    name_attr_dropdown = ListToString(attr_dropdown.text.split())
                    inner_data['Атрибуты'][attr_name] += ' ' + name
            except:
                pass
            try:
                # Обычный список
                list_attr = attr.find_all('div', class_ = 'card-block__choice')
                for attr_name in list_attr:
                    name = ListToString(attr_name.find('span', class_ = 'as_form__check').text.split())
                    # print(name)
                    inner_data['Атрибуты'][attr_name] += ' ' + name
                    
            except:
                inner_data['Атрибуты'][attr_name] += ' '
                
                pass         
    except:
        inner_data.update({'Атрибуты':''})
        
        pass
    try:
        # Цена
        product_prices = soup.find('div', class_='product-prices').find_all('div',class_='card-block__radio')[-1].find('p', class_ = 'card-block__right-price').text.strip()
        # print(product_prices)
        inner_data.update({'Цена': product_prices})
    except:
        inner_data.update({'Цена': ''})
        pass
    try:
        # Описание
        sign_description = ListToString(soup.find('div', class_ = 'tabs_category__container container').find('p').text.split())
        inner_data.update({'Описание': sign_description})
        # print(sign_description)
    except:
        inner_data.update({'Описание': ''})
        pass
    signs.append(inner_data)
    


# Инофрмация о знаке
def GetSignInfo(url, inner_data):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    attrs=[]
    values=[]
    try:
        prices_block = soup.find('p', class_= 'card-block__right-price').text.split()
        # Цена
        price = ListToString(prices_block)
        # data.append({'Цена': price})
        # print(price)
        inner_data.update({'Цена': price})
    except:
        inner_data.update({'Цена': ''})
        pass
    size_type = soup.find('div', class_= 'card-block__left')
    try:
        sign_description = soup.find('div', class_ = 'tabs_category__container container')
        # Описание
        descript = ListToString(sign_description.find('p').text.split())
        # print(descript)
        inner_data.update({'Описание': descript})
        # data.append({'Описание': descript})
    except:
        inner_data.update({'Описание': ''})
        pass
    try:
        img_href = soup.find('section', class_='tabs_category').find('img', class_='lazy').get('src')
        inner_data.update({'Чертеж': img_href})
        # print(baseUrl + img_href)
        # image = (base64.b64encode(requests.get((baseUrl + src[3:]).strip()).content).replace(b'\n', b'')).decode("utf-8")
        # print(image)
    except:
        inner_data.update({'Чертеж': ''})
        pass  
    try:
        list_name_attrs = soup.find('div', class_ ='card-block__left').find_all('div', class_= 'card-block__choices')
        for attr in list_name_attrs:
            #  Название типов
            attr_name = ListToString(attr.find('label', class_= "card-block__right-label card-label").text.split())
            # print(attr_name)
            attrs.append(attr_name)
            # inner_data.update({'Атрибуты':{
            #     attr_name: ''
            # }})
            try:
                # Всплывающийся список
                list_attr_dropdown = attr.find_all('li', class_= 'c-dropdown__item')
                for attr_dropdown in list_attr_dropdown:
                    name_attr_dropdown = ListToString(attr_dropdown.text.split())
                    # print(name_attr_dropdown)
                    values.append(name_attr_dropdown)
                    # print(name_attr_dropdown)
                    # inner_data['Атрибуты'][attr_name] += ' ' + name_attr_dropdown
                # 
                # 'атрибуты' : 
                # названи типа : значение1, значение2...

            except:
                pass
            try:
                # Обычный список
                list_attr = attr.find_all('div', class_ = 'card-block__choice')
                for attr_name in list_attr:
                    name = ListToString(attr_name.find('span', class_ = 'as_form__check').text.split())
                    # print(name)
                    # print(name)
                    values.append(name)
                    # inner_data['Атрибуты'][attr_name] += ' ' + name
            except:
                pass         
    except:
        pass
    signs.append(inner_data)    
    # print("inner_data", inner_data)
    # print(dict(zip(attrs,values)))
    
    # print("signs", signs)
    

def ListToString(s):
    str1 = " " 
    return (str1.join(s))

if __name__ == "__main__":
    main()
    # print(signs)
    # my_file = open('znaki.json', 'w')
    # my_file.write(str(signs))
    # my_file.close()