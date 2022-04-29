# SELENIUM ELECTRICITY PRICE DETECTER!
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_argument("--enable-javascript")

# For linux
service = Service('/home/notme/Desktop/chromedriver')

# For Window
# service = Service('C:\Program Files (x86)\chromedriver.exe')


driver = webdriver.Chrome(service=service, chrome_options=chrome_options)
driver.maximize_window()
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
time.sleep(6)

see_data_btn = driver.find_element_by_xpath('//*[@id="root"]/main/div/div[1]/div[2]/a')
time.sleep(6)
driver.implicitly_wait(10)

see_data_btn.click()

driver.implicitly_wait(10)

timer_btn = driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div/div[2]/ul/li[1]')

timer_btn.click()

driver.implicitly_wait(10)


timer_toggle = driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div/div[1]/div[2]/div[2]/div[2]/label[1]')

time.sleep(3)

timer_toggle.click()

driver.implicitly_wait(3)
time.sleep(3)


# actions.click_and_hold(load_btn)

while True:
    time.sleep(2)
    load_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "button.m-navigate.m-left.css-1rmrtd0")))
# data_elem = driver.find_element_by_xpath('//*[@id="consumption-bar-chart"]/div[1]')
    # actions.move_to_element(load_btn)
    print('upper load btn code')
    driver.implicitly_wait(10)
    actions.click_and_hold(load_btn)
    print('clicking load button')
    actions.pause(1.3)
    # actions.click_and_hold(load_btn)
# actions.move_to_element(data_elem)
# actions.context_click(data_elem)
    print('releasing button')
    # actions.release(load_btn)
    actions.move_by_offset(xoffset=20, yoffset=-50)
    print('moving to offset _ _')
    # actions.click_and_hold(load_btn)
    text = driver.find_element_by_xpath('//*[@id="root"]/main/div[2]/div/div[1]/div[2]/div[1]/p[1]/strong').text
    print(text)
    actions.perform()
    print('moving to next iteration')


# if text == '':
#     actions.release(load_btn)
#     print('releasing')
#     actions.perform()



