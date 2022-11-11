import requests
from bs4 import BeautifulSoup

proxies = {
    'http': 'http://proxy.itm.bfw:3128',
#    'https': 'https://proxy.itm.bfw:3128',
  }

# proxies = {
# 'http': 'http://192.168.10.221:3128',
# 'https': 'https://192.168.10.221:3128',
# }

url = 'https://fr.wiktionary.org/wiki/manger'

response = requests.get(url, proxies=proxies)
print(f'Status Code: {response.status_code}')


# soup = BeautifulSoup(r.content)
# findMe =soup.find_all("div", class_="API")
# print("findMe")
# print(findMe)
