from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
import aiohttp
import gc
import custom_utils.driver as ud
import custom_utils.user_agent as ragent
import custom_utils.proxy as rproxy
from bs4 import BeautifulSoup
import time
import asyncio

from models.attrs import GetItemsUrl


pagesUrls = []


async def GetCategoryPages(url, webdriver=None):
    
    i = 1
    while True:
        hdr = {'User-Agent': ragent.GetRandom()}
        async with aiohttp.ClientSession(headers=hdr) as session:
            print(url)
            async with session.get(url) as response:
                page_count = range(1)
                soup = BeautifulSoup(await response.text(), 'lxml')
                h1 = soup.find('div', class_ = 'main-header').find('h1')
                if h1.text != 'Страница не найдена':
                    i += 1
                    print(url + '&page=' + str(i))
                else:
                    break



async def Gather(categories):
    driver = ud.create_driver
    tasks = []
    counter = 0
    for category in categories:
        if counter == 15:
            await asyncio.gather(*tasks)
            tasks.clear()
            counter = 0
        task = asyncio.create_task(GetCategoryPages(category, driver))
        tasks.append(task)
        counter += 1
    await asyncio.gather(*tasks)
    tasks.clear()
    gc.collect
