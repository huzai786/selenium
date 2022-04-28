# SELENIUM ELECTRICITY PRICE DETECTER!
import sys
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service


service = Service('/home/notme/Desktop/chromedriver')
driver = webdriver.Chrome(service=service)
print('opening the webpage')
driver.get('https://selvbetjening.energi.seas-nve.dk/')

actions = ActionChains(driver) 
driver.implicitly_wait(3)

btn = driver.find_element_by_xpath("//button[. = 'Accepter alle']").click()

driver.implicitly_wait(3)

login_user = driver.find_element_by_xpath('//*[@id="root"]/main/div/div/form/div[1]/input')

login_pass = driver.find_element_by_xpath('//*[@id="root"]/main/div/div/form/div[2]/input')

login_user.send_keys('zeeshan.ali2@yahoo.com')
login_pass.send_keys('nrm4d3x2')
login_btn = driver.find_element_by_xpath('//*[@id="root"]/main/div/div/form/div[3]/button')

login_btn.click()
driver.implicitly_wait(10)
time.sleep(4)

see_data_btn = driver.find_element_by_xpath('//*[@id="root"]/main/div/div[1]/div[2]/a')
time.sleep(3)
driver.implicitly_wait(10)

see_data_btn.click()

driver.implicitly_wait(10)

timer_btn = driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div/div[2]/ul/li[1]')

timer_btn.click()

driver.implicitly_wait(10)


timer_toggle = driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div/div[1]/div[2]/div[2]/div[2]/label[1]')

time.sleep(4)

timer_toggle.click()

driver.implicitly_wait(3)
time.sleep(3)


# load_btn = driver.find_element_by_class_name('button.m-navigate.m-left.css-1rmrtd0')

load_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "button.m-navigate.m-left.css-1rmrtd0")))

text = driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div/div[1]/div[2]/div[1]/p[1]/strong').text


actions.move_to_element(load_btn)

driver.implicitly_wait(3)

actions.click_and_hold(load_btn)
actions.click_and_hold(load_btn)
print(text)

actions.move_by_offset(xoffset=20, yoffset=-50)
if text == 'Kl. 08-09 torsdag den 21. april brugte du':
    actions.release(load_btn)
    print(text)
    print('releasing')

actions.perform()














































# i = 0
# while i < 1:
#     try:
#         load_old_data = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'button m-navigate m-left css-1rmrtd0')))
#         print('Clicking to see old data!')
#         load_old_data.click()
#         time.sleep(1)
#     except:
#         i = 1
# for i in range(20):
    # print("clicking")
    # old_data_btn.click()
    # time.sleep(4)

# driver.implicitly_wait(3)

# action_chains.move_by_offset(200, 200).context_click().perform()

