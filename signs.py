from urllib import request
from bs4 import BeautifulSoup
import requests


def ParseSigns(url, baseUrl):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    signs_catalog = soup.find_all("a", class_ = "card-block__top")
    for signs_name in signs_catalog:
        sign_name = signs_name.text.strip()
        sign_href = baseUrl + signs_name.attrs["href"].strip()
        
        GetSignInfo(sign_href)

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