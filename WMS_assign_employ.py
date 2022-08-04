import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
#s=Service("C:\Driver\chromedriver")
s=Service(r"D:\Users\shara\Downloads\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get('https://emiza-wms-dev.s3.ap-south-1.amazonaws.com/wms-dev/docs/EmizaWMS.html')
time.sleep(1)
driver.find_element("xpath", "//*[@id='10']/div[1]").click()
time.sleep(1)
driver.find_element("xpath", "//*[@id='110105']/div[1]").click()
time.sleep(1)
driver.find_element("xpath", "//*[@id='B|110105|WH01-CUST01-20220802-1108']/div[2]").click()
time.sleep(1)
element=driver.find_element("name","AssignTo")
Dropdown=Select(element)
Dropdown.select_by_visible_text('Executive - 1')
time.sleep(1)
driver.find_element("xpath", "//*[@id='AX-01']").click()
time.sleep(1)
driver.close()
#this is a new change
#this is another change
#this is another another change
