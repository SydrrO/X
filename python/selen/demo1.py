from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
wd = webdriver.Chrome(options=chrome_options)




wd.get('https://dhh.wtf/#/login')

email = wd.find_element(By.XPATH, "//input[@type='text']")
email.clear() # 清除输入框已有的字符串
email.send_keys('2562312527@qq.com') # 输入新字符串



password = wd.find_element(By.XPATH, "//input[@type='password']")
password.clear()
password.send_keys('D200610211842.')

enter = wd.find_element(By.XPATH,"//button").click()
sleep(3)
information = wd.find_element(By.XPATH, '//div[@class="mb-0"]/p/span')

print(information.text)