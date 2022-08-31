from cgitb import text
import gc
import asyncio
# from types import NoneType
import aiohttp
import custom_utils.driver as ud
from bs4 import BeautifulSoup
import custom_utils.user_agent as ragent

# Items urls
items_urls = {}

async def ParsePages(url):
    hdr = {'User-Agent': ragent.GetRandom()}
    async with aiohttp.ClientSession(headers=hdr) as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            try:
                items = soup.find('div', class_ = 'items-column').find_all('div', class_ = 'item')
                for item in items:
                    item_href = item.find('div', class_ = 'item__name').find('a').attrs['href']
                    print(item_href)
            except:
                print("EXCEPTION")
                pass
            # products_container = soup.find(
            #     'div', class_='products-container')
            # products = products_container.find_all(
            #     'div', class_='product-thumb')
            # for product in products:
            #     name_container = product.find(
            #         'div', class_='name').find('a')
            #     items_urls[name_container.text] = name_container.attrs['href']

async def GetItemsUrl(pages):
    tasks = []
    for page in pages:
        task = asyncio.create_task(ParsePages(page))
        tasks.append(task)
    await asyncio.gather(*tasks)
    gc.collect()

# Items
items = []


async def ParseItemPage(url):
    hdr = {'User-Agent': ragent.GetRandom()}
    async with aiohttp.ClientSession(headers=hdr) as session:
        try:
            async with session.get(url) as response:
                soup = BeautifulSoup(await response.text(), 'lxml')
                info_block = soup.find('div', class_= 'product_content-w')
                descriptions = info_block.find('p').text
                print(descriptions)
                # fields = info_block.find_all('br').text
                # for field in fields:
                #     print(field)    
        except Exception as ex:
            print(response.status)
            print(ex)
            # try:
            #     table = soup.find('div', class_= 'showhide').find_all('tr')
            #     for field in table:
            #         print(field.text)
            # except:
            #     pass




# WORK METHOD
# import requests
# import json
# import time
# from selenium import webdriver
# from bs4 import BeautifulSoup
# from selenium.webdriver.common.by import By
# import custom_utils.driver as ud

# items = []

# Getting urls of items
# def GetItemsUrls(url):
#     req = requests.get(url)
#     soup = BeautifulSoup(req.text, "lxml")
#     item_names = soup.find_all('div', class_= 'item__name')
#     for name in item_names:
#         GetInfo('https://www.chipdip.ru' + name.find('a').attrs['href'])


# Creating dict and write all info about item 
# def GetInfo(url):
#     item = {}
#     driver = ud.create_driver()  #Chrome(executable_path="/home/adok/pyt/chipdipru/chromedriver/chromedriver")
#     try:
#         driver.get(url)
#         time.sleep(1)
#         price = driver.find_element(By.CLASS_NAME, 'ordering__value').text
#         name = driver.find_element(By.CLASS_NAME, 'main-header').find_element(By.TAG_NAME, 'h1').text
#         category = driver.find_element(By.ID, 'breadcrumbs_items').find_elements(By.TAG_NAME, 'a')[-2].text
#         attr_names = []
#         list_attrs = driver.find_element(By.CLASS_NAME, 'product_content-w').find_elements(By.CLASS_NAME, 'product__param-name')
#         for attr_name in list_attrs:
#             attr_names.append(attr_name.text)
#         attributes = []
#         list_values = driver.find_element(By.CLASS_NAME, 'product_content-w').find_elements(By.CLASS_NAME, 'product__param-value')
#         for attr_value in list_values:
#             attributes.append(attr_value.text)
#         item = {
#         'Название': name,
#         'Категория 1': 'Реле',
#         'Категория 2': category,
#         'Ссылка': url,
#         'Цена': price,
#         'Атрибуты': dict(zip(attr_names,attributes))}
#         items.append(item)
#     except Exception as _ex:
#         print(_ex)
#     finally:
#         driver.close()
#         driver.quit()