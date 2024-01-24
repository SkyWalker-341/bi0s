from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
chrome_path = "C:/Users/all-in-one/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
service = Service(chrome_path)
browers = webdriver.Chrome(service=service)
browers.get("https://www.tutorialsfreak.com/")
time.sleep(5)
browers.find_element_by_xpath("""/html/body/div/div[2]/div[1]/section[1]/div/div[1]/div/div/div/div[2]/button""").click()
time.sleep(5)
browers.find_element_by_xpath("""/html/body/div/div[2]/div[1]/section/div/div[2]/div[1]/div/ul/li[7]/a""").click()
