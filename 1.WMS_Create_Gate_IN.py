import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
s=Service("C:\Driver\chromedriver")
driver=webdriver.Chrome(service=s)
driver.get('https://emiza-wms-dev.s3.ap-south-1.amazonaws.com/wms-dev/docs/GateInTxnList.html')
driver.maximize_window()
time.sleep(5)
driver.find_element("xpath","//*[@id='displayLayout']/section/div/div/div/div[2]/button").click()
time.sleep(3)
element=driver.find_element("class name","form-control")
Dropdown=Select(element)
Dropdown.select_by_visible_text('Swiss Military') #select client
time.sleep(1)
Type=driver.find_element("name","InwardTxnTypeID") #Inward Transaction Type
drp=Select(Type)
drp.select_by_visible_text('IP-Inward Packing Material-Emiza')
time.sleep(1)
driver.find_element("id","VehicleNumber").send_keys('7865MH9871') #vehical number
time.sleep(1)
dock=driver.find_element("name","DockStationID") #select dock station
drp=Select(dock)
drp.select_by_visible_text('dock-03')
time.sleep(1)
Vehicaltype=driver.find_element("name","VehicleTypeId") #select vehical type
drp=Select(Vehicaltype)
drp.select_by_visible_text('Truck 14FT - 250 Ton')
time.sleep(1)
driver.find_element("id","SealNo").send_keys('BF66') #seal number
time.sleep(1)
driver.find_element("id","DocketNumber").send_keys('4') #docket number
time.sleep(1)
driver.find_element("id","NoOfInvoices").send_keys('2') #number of invoices
time.sleep(1)
driver.find_element("id","TotalNoOfBoxes").send_keys('30') #number of boxes
time.sleep(1)
Finalresult=driver.find_element("name","ReasonID") # vehical final result
drp=Select(Finalresult)
drp.select_by_visible_text('Vehicle allowed')
time.sleep(1)
driver.find_element("xpath","//*[@id='actions']/button[1]/i").click() #Click to save button
time.sleep(1)
driver.find_element("xpath","//*[@id='AX-01']").click() #Gate_IN Complete button
driver.close()







