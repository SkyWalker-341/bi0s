import requests
from bs4 import BeautifulSoup
#import pandas as pd

for num in range(1,11):
    url = "https://www.flipkart.com/search?q=mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_1_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_1_na_na_na&as-pos=2&as-type=RECENT&suggestionId=mobile%7CMobiles&requestId=c0c11bbf-ced1-4402-82cd-d76e9863f878&as-backfill=on&page="+str(num)
    #print(url)
    request = requests.get(url)
    print(request.status_code)

    soup  = BeautifulSoup(request.text,"lxml")
    #print(soup)

    table = soup.find("div",class_ = "_1YokD2 _3Mn1Gg")

    #print(table)
    name = table.find_all("div",class_ = "_4rR01T")
    price = table.find_all("div",class_="_30jeq3 _1_WHN1")
    despction = table.find_all("div",class_ ="fMghEO")
    rating = table.find_all("div",class_ = "gUuXy-")
    name_s = [i.text for i in name]
    price_s = [i.text for i in price]
    despction_s = [i.text for i in despction]
    rating_s = [i.text for i in rating]
    for i,j,k,l in zip(name_s,price_s,despction_s,rating_s):
        product_d = {"name":i,"price":j,"despction":k,"rating":l}
        print(product_d)
    #print(rating)
    #print(despction)
    #print(price)
    #print(name)

