import requests
import random
from bs4 import BeautifulSoup as bs

proxies = []


def GetProxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = bs(requests.get(url).content, "html.parser")
    table = soup.find(
        "table", attrs={"class": "table table-striped table-bordered"})
    table = table.find('tbody')
    for row in table.find_all("tr"):
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return True


def GetProxy():
    proxy = random.choice(proxies)
    proxy = {"http": 'http://'+proxy}
    return proxy