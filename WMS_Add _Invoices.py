import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
#s=Service("C:\Driver\chromedriver")
s=Service(r"D:\Users\shara\Downloads\chromedriver_win32\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get('https://emiza-wms-dev.s3.ap-south-1.amazonaws.com/wms-dev/docs/EmizaWMS.html') #Gate_IN URL
driver.implicitly_wait(5)
driver.find_element("xpath","//*[@id='20']/div[1]").click() #shipment arrival notice
time.sleep(1)
driver.find_element("xpath","//*[@id='120100']/div[1]").click() #caption invoice wise details
time.sleep(1)
driver.find_element("xpath","//*[@id='E|120100|WH01-CUST01-20220801-1517']/div[1]").click() #pending transactions (Swiss Military)
time.sleep(1)
driver.find_element("xpath","//*[@id='addInvoice']/button").click() #add invoices
time.sleep(1)
driver.find_element("xpath","//*[@id='R{Row-ID}']/td[1]/input").send_keys('INVOICE-10') #invoice number
time.sleep(1)
driver.find_element("xpath","//*[@id='R{Row-ID}']/td[2]/input").send_keys('5') #invoice box quantity
time.sleep(1)
driver.find_element("xpath","//*[@id='R{Row-ID}']/td[3]/input").send_keys('5') #Received Box
time.sleep(1)
driver.find_element("xpath","//*[@id='R{Row-ID}']/td[4]/input").send_keys('1') #Damaged Box
time.sleep(1)
driver.find_element("xpath","//*[@id='R{Row-ID}']/td[5]/input").send_keys('5') #Invoice Weight
time.sleep(1)
driver.find_element("xpath","//*[@id='R{Row-ID}']/td[6]/input").send_keys('7') #Length
time.sleep(1)
driver.find_element("xpath","//*[@id='R{Row-ID}']/td[7]/input").send_keys('5') #Breadth
time.sleep(1)
driver.find_element("xpath","//*[@id='R{Row-ID}']/td[8]/input").send_keys('9') #Height
time.sleep(1)
Executive=driver.find_element("name","ExecutiveAssigned") #Executive
drp=Select(Executive)
drp.select_by_visible_text('Executive - 2')
driver.find_element("xpath","//*[@id='R{Row-ID}']/td[10]/input").send_keys('3')  #Labours
driver.close()
#this is a comment


