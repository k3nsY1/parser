from dis import Instruction
from bs4 import BeautifulSoup
import requests

# url = "https://mirprivoda.ru/katalog/zubchatye-shesterni/"


# req = requests.get(url)
# src = req.text
# with open("index1.html", "w") as file:
#     file.write(src)

with open("index1.html") as file:
    src = file.read()


soup = BeautifulSoup(src, "lxml")
# count = 0
# def main():
#     get_names("active")

# instructions= soup.find("span", itemprop="name")
# try:
#     method = str.replace(instructions.get_text(strip=True),". ",".")
#     method = str.replace(method, ". ", ".")
#     method = (str.replace(method, ".",".\n"))
# except AttributeError:
#     print(instructions)

# all_products=soup.find_all(class_ ="active")
# for item in all_products:
#     print(item.text)
# def get_names(a):
all_targets = soup.find(class_= "profuct_top_line").find("a").find_all("th")
for names in all_targets:
    print(names.text)
#         name = soup.find(class_ = "")
    # print(names.href)
    # for name in names:
    #     all_names = soup.find_all(class_ = "name")
    #     print(all_names.text)
# for item in all_names:
#     item_text = item.text
#     print(f"{item_text}")
    # for ref in item:
    #     href = ref.get("href")
    # print(item.text)
    # count = count +1
    # print(item)
    # item_href = item.get("href")
    # print(item.text)

