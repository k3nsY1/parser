import asyncio
from webbrowser import Chrome
import models.category as category
import models.pages as pages
import models.attrs as attrs
import custom_utils.proxy as rproxy


rproxy.GetProxies()

print('Getting categories')
asyncio.run(category.GetCategories('https://www.chipdip.ru/catalog/relay'))
print('Getting pages')
asyncio.run(pages.Gather(category.categoriesUrls))
# print('Parse Item')
# asyncio.run(attrs.ParseItemPage('https://www.chipdip.ru/product/tyco-1-1393154-2-pt570024'))