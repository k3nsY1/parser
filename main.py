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


# all_products=soup.find_all(class_ ="active")
# for item in all_products:
#     print(item.text)
# def get_names(a):
all_targets = soup.find_all(class_ = "name")
for names in all_targets:
    print(names.text)
    print(names.href)
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

