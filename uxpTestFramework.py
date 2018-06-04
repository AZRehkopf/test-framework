from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pywinauto import keyboard
from time import sleep

####################################
#        Device Connection         #
####################################

def connect(ip):
	driver.get("http://" + ip)
	
def login():
	elem = driver.find_element_by_name("user")
	elem.clear()
	elem.send_keys("admin")

	elem = driver.find_element_by_id("password")
	elem.clear()
	elem.send_keys("PV1admin")
	elem.send_keys(Keys.RETURN)

def endTest():
	driver.close()

####################################
#              Header              #
####################################

### Device Status Menu ###

def openDeviceStatus():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "device-status"))).click()
	sleep(1)

def closeDeviceStatus():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-status-close"))).click()
	sleep(1)

def reboot():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-status-restart"))).click()
	sleep(1)

def cancelReboot():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "reboot-cancel"))).click()
	sleep(1)

def confirmReboot():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "reboot-ok"))).click()
	sleep(1)

def factoryReset():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.ID, "factory-reset"))).click()
	sleep(1)

def cancelFactoryReset():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "reboot-cancel"))).click()
	sleep(1)

def confirmFactoryReset():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.ID, "factory-reset-ok"))).click()
	sleep(1)

### Options Menu ###

def openOptions():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "options"))).click()
	sleep(1)

def toggleAutoAccept():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "auto-accept-toggle-handle"))).click()
	sleep(1)

def toggleChime():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "play-chime-toggle-handle"))).click()
	sleep(1)

def saveOptions():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-option-save"))).click()
	sleep(1)

def cancelOptions():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-option-cancel"))).click()
	sleep(1)

### WebEasy ###

def openAdvanced():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.ID, "advanced"))).click()
	sleep(1)

### Update Profile ###

def updateProfile():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.ID, "update"))).click()
	sleep(1)

### Logout Dialogue ###

def logout():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "logoutUrl"))).click()
	sleep(1)

def confirmLogout():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "logout-ok"))).click()
	sleep(1)

def cancelLogout():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "logout-cancel"))).click()
	sleep(1)

### Picture Dialogue ###

def openPictureDialogue():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "device-image"))).click()
	sleep(1)

def selectPicture(filepath):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "device-image-btn-browse"))).click()
	sleep(2)
	keyboard.SendKeys(filepath)
	keyboard.SendKeys('{ENTER}')
	sleep(1)

def cancelPictureChange():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-device-image-cancel"))).click()
	sleep(1)

def confirmPictureChange():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-device-image-replace"))).click()
	sleep(1)	

####################################
#             Profile              #
####################################

def changeProfile(element, delay):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.ID, element))).click()
	sleep(delay)

def openGenericProfiles():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "generic-btn-txt"))).click()
	sleep(1)

def openApplicationProfiles():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "application-btn-txt"))).click()
	sleep(1)

####################################
#            Favourites            #
####################################

def startSession(element):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.ID, element))).click()
	sleep(1)	

def endSession():
	wait = WebDriverWait(driver, 10)
	element =  wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "close-btn"))).click()
	element =  wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-ok"))).click()
	sleep(1)

def createGroup():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.ID, "createGroup"))).click()
	sleep(1)

def toggleFavourite(element):
	wait = WebDriverWait(driver, 10)
	elem = wait.until(EC.element_to_be_clickable((By.ID, element)))
	action = ActionChains(driver)
	action.move_to_element_with_offset(elem, 0,0).perform()
	action.click().perform()

def removeFavourite(element):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.ID, element)))
	action = ActionChains(driver)
	action.move_to_element(element).perform()
	
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "hover-fav-delete"))).click()
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "hover-fav-delete-btn"))).click()
	sleep(1)

def addToGroup(elem, grp):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.ID, elem)))
	group =  wait.until(EC.element_to_be_clickable((By.ID, grp)))
	action = ActionChains(driver)
	action.drag_and_drop(element, group).perform()

def openSearch():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-box"))).click()
	sleep(1)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-all"))).click()
	sleep(1)

def closeSearch():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-close"))).click()
	sleep(1)

def search(query):
	wait = WebDriverWait(driver, 10)
	elem = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-box"))).click()
	elem = driver.find_element_by_class_name("searchInput")
	elem.clear()
	for i in query:
		sleep(0.2)
		elem.send_keys(i)

####################################
#           Room Control           #
####################################

def openRoomControl():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "room-control-image"))).click()
	sleep(1)

def openProfileSources():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "room-control-profile"))).click()
	sleep(1)

def toggleSwapDisplay():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.ID, "swapDisplay"))).click()
	sleep(1)

def openCameraControls(element):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.ID, element))).click()
	sleep(1)

####################################
#         Camera  Control          #
####################################

### Directional Buttons ###

def moveCameraRight(delay):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "right-btn-size")))
	action = ActionChains(driver)
	action.click_and_hold(element).perform()
	sleep(delay)
	action.release().perform()
	sleep(1)

def moveCameraLeft(delay):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "left-btn-size")))
	action = ActionChains(driver)
	action.click_and_hold(element).perform()
	sleep(delay)
	action.release().perform()
	sleep(1)

def moveCameraUp(delay):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "up-btn-size")))
	action = ActionChains(driver)
	action.click_and_hold(element).perform()
	sleep(delay)
	action.release().perform()
	sleep(1)

def moveCameraDown(delay):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "down-btn-size")))
	action = ActionChains(driver)
	action.click_and_hold(element).perform()
	sleep(delay)
	action.release().perform()
	sleep(1)

### Modifiers ###

def togglePrecision():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "precision-btn-size"))).click()
	sleep(1)

def toggleReverse():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "reverse-btn-size"))).click()
	sleep(1)

### Zoom Control ###

def zoomInSlow(delay):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "local-slow-in-btn")))
	action = ActionChains(driver)
	action.click_and_hold(element).perform()
	sleep(delay)
	action.release().perform()
	sleep(1)

def zoomOutSlow(delay):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "local-slow-out-btn")))
	action = ActionChains(driver)
	action.click_and_hold(element).perform()
	sleep(delay)
	action.release().perform()
	sleep(1)

def zoomInFast(delay):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "local-fast-in-btn")))
	action = ActionChains(driver)
	action.click_and_hold(element).perform()
	sleep(delay)
	action.release().perform()
	sleep(1)

def zoomOutFast(delay):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "local-fast-out-btn")))
	action = ActionChains(driver)
	action.click_and_hold(element).perform()
	sleep(delay)
	action.release().perform()
	sleep(1)

### Presets ###

def selectPreset(preset):
	element = {
		1: "local-preset-btn-one",
		2: "local-preset-button-two",
		3: "local-preset-button-three",
		4: "local-preset-button-four",
		5: "local-preset-button-five"
	}[preset]

	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, element))).click()
	sleep(1)

### Remote Control Control ###

def toggleRemoteControl():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "local-remote-access-toggle-btn"))).click()
	sleep(1)

### Mirror Toggle ###
def toggleMirror():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "local-mirror-btn"))).click()
	sleep(1)

### Focus Control ###

def manualNearFocus(delay):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "local-near-btn")))
	action = ActionChains(driver)
	action.click_and_hold(element).perform()
	sleep(delay)
	action.release().perform()
	sleep(1)

def manualFarFocus(delay):
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "local-far-btn")))
	action = ActionChains(driver)
	action.click_and_hold(element).perform()
	sleep(delay)
	action.release().perform()
	sleep(1)

def toggleAutoFocus():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "local-auto-btn"))).click()
	sleep(1)

### Close Camera Dialogue ###

def closeCameraControl():
	wait = WebDriverWait(driver, 10)
	element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "local-remote-dialog-close"))).click()
	sleep(1)

####################################
#               Main               #
####################################

def main():
	connect("172.17.137.23")
	login()
	sleep(2)
	startSession("group-div-1")
	sleep(4)
	endTest()

if __name__ == "__main__":
	driver = webdriver.Chrome()
	main()