from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.chrome.options import Options
wd = webdriver.Chrome()

wd.get('https://buff.163.com/goods/759401')
sleep(5)
price = wd.find_element(By.XPATH, '//span[contains(@class,"c_price")]')[0]
