from lib2to3.pgen2 import driver
import time
import numpy as np
import aiohttp
from bs4 import BeautifulSoup
from custom_utils.driver import create_driver


categoriesUrls = []
base_url = 'https://www.chipdip.ru'

async def GetCategories(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), "lxml")
            categories = soup.find_all('div', class_ = 'catalog__f_wrapper')
            for category in categories:
                category_href = base_url + category.find('a', class_= 'link').attrs['href']
                
                categoriesUrls.append(category_href)
                # categoriesUrls = np.concatenate(())
            # print(categoriesUrls)

