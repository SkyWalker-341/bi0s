import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/product/495"
request = requests.get(url)
print(request.status_code)
soup = BeautifulSoup(request.text,"html")
#print(soup)
product_name = soup.findAll("h4",class_="card-title title")
print(product_name.text)

