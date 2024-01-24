from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
chrome_path = "C:/Users/all-in-one/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(chrome_path)
domain =  " house of Dragon " #input("enter the domain name : ")
website = webdriver.Chrome(service=service)
website.get("https://www.google.com/")
time.sleep(3)
input1 = website.find_element_by_xpath("""/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/div/textarea""")
input1.send_keys(domain)
time.sleep(2)
input1.send_keys(Keys.ENTER)
time.sleep(2)
website.find_element_by_xpath("""/html/body/div[5]/div/div[10]/div[3]/div[1]/div[2]/div/div/div/div/div/div/div/div/div[1]/div/div/div[1]/div/div[3]/div[5]/div/div/div/div/div/div[1]/div/div/span/a""").click()
time.sleep(3)
heigth = website.execute_script("return document.body.scrollHeight")
#print(heigth)
time.sleep(2)
while True:
    website.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    website.save_screenshot("E:/bi0s/web_scraping/selenium/dragon.png")
    