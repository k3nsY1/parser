import requests
from bs4 import BeautifulSoup
from main import ParseSigns


def GetSubCategory(url, baseUrl):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    page_catalog = soup.find_all("a", class_ = "production__item")
    for catalog_item in (page_catalog):
        sub_cat_name = catalog_item.text.strip()
        sub_cat_url = url + catalog_item.attrs["href"].strip()
       
        ParseSigns(baseUrl + catalog_item.attrs["href"].strip())