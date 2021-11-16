from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://vk.com/')
obj = BeautifulSoup(html.read())
print(str(obj.body.h1).strip('</h1>'))