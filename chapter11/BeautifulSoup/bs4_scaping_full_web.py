import requests
from bs4 import BeautifulSoup
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
request = requests.get(url)
print(request.status_code)

soup = BeautifulSoup(request.text,"html.parser")

name= soup.find_all("a",class_ = "title" )
prices = soup.find_all("h4",class_ = "float-end price card-title pull-right")
description = soup.find_all("p",class_ = "description card-text")
rating = soup.find_all("p",class_ = "float-end review-count")
name_p = [i.text for i in name]
prices_p = [i.text for i in prices]
description_p = [i.text for i in description]
rating_p = [i.text for i in rating]
for i,j,k,l in zip(name_p,prices_p,description_p,rating_p):
    total_d = {"Name":i,"prices" :j,"description":k,"Rating":l}
    print(total_d)    