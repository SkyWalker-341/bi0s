from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
chrome_path = "C:/Users/all-in-one/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(chrome_path)
email = input("enter the email name :")
password = input("enter the  password : ")
website = webdriver.Chrome(service=service)
website.get("https://www.w3schools.com/")
time.sleep(4)
website.find_element_by_xpath("""/html/body/div[2]/div[1]/div[3]/a[1]""").click()
#website.get("https://profile.w3schools.com/log-in?redirect_url=https%3A%2F%2Fmy-learning.w3schools.com")
time.sleep(4)
input1 = website.find_element_by_xpath('''/html/body/div[1]/div/div/div[4]/div[1]/div/div[2]/form/div[1]/div[2]/input''')
input1.send_keys(email+"@gmail.com")
time.sleep(4)
input2 = website.find_element_by_xpath("""/html/body/div[1]/div/div/div[4]/div[1]/div/div[2]/form/div[2]/div[2]/input""")
input2.send_keys(password)
time.sleep(3)
website.find_element_by_xpath("""/html/body/div[1]/div/div/div[4]/div[1]/div/div[4]/div[1]/button""").click()
