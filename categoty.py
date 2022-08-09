import requests
from bs4 import BeautifulSoup

def GetCategory(url, baseUrl):
    req = requests.get(url)
    
    
    soup = BeautifulSoup(req.text, "lxml")
    catalog_items = soup.find_all("a", class_ = "production__item")
    for catalog_item in catalog_items:
        name = catalog_item.text.strip()
        url = baseUrl + catalog_item.attrs["href"].strip()
        # ParsePage(baseUrl + catalog_item.attrs["href"].strip())
        print(name)
        print(baseUrl + catalog_item.attrs["href"].strip())
        
        # ParseCards(baseUrl + catalog_item.attrs["href"].strip())