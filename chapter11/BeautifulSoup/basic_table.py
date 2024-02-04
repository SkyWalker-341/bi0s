import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
request = requests.get(url)
print(request.status_code)

soup = BeautifulSoup(request.text,"html")
print(soup)