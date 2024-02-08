import requests
from bs4 import BeautifulSoup
import pandas  as pd

url = "https://www.forbesindia.com/article/explainers/top-10-largest-economies-in-the-world/86159/1"
request = requests.get(url)
print(request.status_code)

soup = BeautifulSoup(request.text,"lxml")
#print(soup)
table =  soup.find("table",style = "border-collapse: collapse;")
#print(table)
header = table.find_all("th",style = "border: 1px solid black; padding: 8px;")
#print(header_S)
header_S = [i.text for i in header]
data_r = table.find_all("tr")
row = []
for i in data_r[1:]:
    name = i.find_all("td",style ="border: 1px solid black; padding: 8px;")
    name_S = [i.text for i in name]
    #print(name_S)
    row.append(name_S)
df =pd.DataFrame(row,columns=header_S,)
print(df)