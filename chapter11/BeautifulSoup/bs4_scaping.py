import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/product/495"
request = requests.get(url)
print(request.status_code)
soup = BeautifulSoup(request.text, "html.parser")

product_name = soup.find("h4", class_="card-title title")
price_tags = soup.find("h4", class_="float-end price pull-right")
description = soup.find("p", class_="description card-text")

product_name_S = product_name.text 
price_tags_S = price_tags.text 
description_S = description.text 

cartbox = dict(name=product_name_S, prices=price_tags_S, description=description_S)
print(cartbox)
