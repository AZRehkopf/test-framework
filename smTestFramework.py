from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pywinauto import keyboard
from time import sleep

sm_ip = "http://172.17.136.10"
devices = [] 

class device:
	def __init__(self, serial, model, name, ip):
		self.serial =  serial
		self.model = model
		self.name = name
		self.ip = ip

def startSession():
	global driver 
	driver = webdriver.Chrome()

	driver.get(sm_ip)
	elem = driver.find_element_by_id("username")
	elem.clear()
	elem.send_keys("admin")

	elem = driver.find_element_by_id("password")
	elem.clear()
	elem.send_keys("PV1nucleus")
	elem.send_keys(Keys.RETURN)
	sleep(2)

def endSession():
	driver.close()

def getVersionNumber():
	items = driver.find_elements_by_class_name("menu-details-label-text")
	return(items[1].text)

def clickMenuButton(text):
	items = driver.find_elements_by_class_name("menu-text-div")
	labels = []
	for i in items:
		labels.append(i.text)
	val = labels.index(text)
	items[val].click()

def createDeviceDatabase():
	items = driver.find_elements_by_xpath("//tr[@class='device-table-row']/*")
	text = []
	global devices
	for i in items:
		text.append(i.text)
	del text[0:11]
	num_of_devices = int(len(text)/11)
	for dev in range(num_of_devices):
		devices.append(device(text[(dev*11)+1],text[(dev*11)+2],text[(dev*11)+3],text[(dev*11)+4]))

def findDevice(name):
	for index, item in enumerate(devices):
		if item.name == name:
			break
	return index

def getAllRegisteredIPs():
	if len(devices) is 0:
		startSession()
		getVersionNumber()
		clickMenuButton("Devices")
		createDeviceDatabase()
		endSession()
	ips = []
	for d in devices:
		ips.append(d.ip)
	return(ips)

#getAllRegisteredIPs()
#print(devices[findDevice("TRS4K-2U")].ip)
#endSession()