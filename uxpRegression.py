import sys, datetime, os, webbrowser
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)
from selenium import webdriver
from time import sleep
import uxpTestFramework as uxp
import smTestFramework as sm

def start_logging():
	global driver, devices
	driver = uxp.startTest()
	start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	with open("reg_log.txt", "w") as log:
		log.write("##################################### Test Begin #####################################\n\n")
		log.write("Regression beginning at " + start + "\n\n")
	devices = sm.getDeviceDatabase()

def stop_logging():
	end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	with open("reg_log.txt", "a") as log:
		log.write("\nRegression ended at " + end + "\n\n")
		log.write("#####################################  Test End  #####################################\n\n")
	uxp.endTest()
	webbrowser.open("reg_log.txt")	

def log(name, result):
	time = datetime.datetime.now().strftime("[%H:%M:%S]: ")
	message = time + "Running " + name + " ... "
	with open("reg_log.txt", "a") as log:
		log.write(message)
		if result:
			log.write("OK\n")
		else:
			log.write("FAIL\n")

def connection_test():
	result = True
	ip_adrs = sm.getAllRegisteredIPs(devices)
	for ip in ip_adrs:
		uxp.connect(ip)
		try:
			assert "Evertz" in driver.title
		except AssertionError:
			result = False
		sleep(0.5)
	log(connection_test.__name__, result)
	
def login_test(ip):
	result = True
	uxp.connect(ip)
	try:
		assert "Evertz" in driver.title		
	except AssertionError:
		result = False
	uxp.login()
	log(login_test.__name__, result)

def endpoint_directory_test():
	result = True
	uxp.openSearch()
	devices = uxp.getSearchResults()
	try:
		assert len(devices) is 6
	except AssertionError:
		result = False
	uxp.closeSearch()
	log(endpoint_directory_test.__name__, result)

### Add logic to check if favs are already added
def add_favourites_test():
	result = True
	uxp.openSearch()
	search = uxp.getFavouriteAddToggles()
	uxp.toggleAllFavourites(search)
	favs = uxp.getFavourites()
	try:
		assert len(favs) is 6
	except AssertionError:
		result = False
	log(add_favourites_test.__name__, result)

### Add logic to check if favs are already added
def remove_favourites_test():
	result = True
	uxp.openSearch()
	search = uxp.getFavouriteRemoveToggles()
	uxp.toggleAllFavourites(search)
	favs = uxp.getFavourites()
	try:
		assert len(favs) is 0
	except AssertionError:
		result = False
	log(remove_favourites_test.__name__, result)

### Add assertions
def initiate_session_test_auto_anwser_on():
	uxp.openSearch()
	search = uxp.getFavouriteAddToggles()
	uxp.toggleAllFavourites(search)	
	
	favs = uxp.getFavourites()
	for f in favs:
		uxp.startSession(f)
		sleep(2)
		uxp.endSession()
	log(initiate_session_test_auto_anwser_on.__name__, True)	

### Add assertions
def initiate_session_test_auto_anwser_off():
	caller = uxp.getCurrentDeviceName()
	callee = uxp.getFavouriteNames()
	callee_ip = devices[sm.findDevice(devices, callee[0])].ip
	caller_ip = devices[sm.findDevice(devices, caller)].ip
	uxp.connect(callee_ip)
	uxp.login()
	uxp.openOptions()
	uxp.toggleAutoAccept()
	uxp.saveOptions()
	uxp.connect(caller_ip)
	sleep(10)
	uxp.startSessionByNum(0)
	uxp.connect(callee_ip)
	uxp.acceptSession()
	uxp.openOptions()
	uxp.toggleAutoAccept()
	uxp.saveOptions()
	uxp.endSession()
	uxp.connect(caller_ip)
	log(initiate_session_test_auto_anwser_off.__name__, True)
	sleep(5)

### Add assertions
def reject_session_test():
	caller = uxp.getCurrentDeviceName()
	callee = uxp.getFavouriteNames()
	callee_ip = devices[sm.findDevice(devices, callee[0])].ip
	caller_ip = devices[sm.findDevice(devices, caller)].ip
	uxp.connect(callee_ip)
	sleep(10)
	uxp.openOptions()
	uxp.toggleAutoAccept()
	uxp.saveOptions()
	uxp.connect(caller_ip)
	uxp.startSessionByNum(0)
	uxp.connect(callee_ip)
	uxp.rejectSession()
	uxp.openOptions()
	uxp.toggleAutoAccept()
	uxp.saveOptions()
	uxp.connect(caller_ip)
	log(reject_session_test.__name__, True)

def change_profiles_while_idle_test():
	result = True
	profiles = uxp.getProfiles()
	for p in profiles:
		uxp.changeProfile(p,5)
	try:
		assert len(profiles) is not 0
	except AssertionError:
		result = False
	log(change_profiles_while_idle_test.__name__, True)

def change_profiles_while_in_session_test():
	result = True
	uxp.startSessionByNum(0)

	profiles = uxp.getProfiles()
	for p in profiles:
		uxp.changeProfile(p,5)
	try:
		assert len(profiles) is not 0
	except AssertionError:
		result = False
	uxp.endSession()
	log(change_profiles_while_in_session_test.__name__, True)

def device_picture_test():
	uxp.openPictureDialogue()
	uxp.selectPicture(os.path.join(dir_path,"night.png"))
	uxp.confirmPictureChange()
	log(device_picture_test.__name__, True)
	sleep(5)

def mute_test():
	uxp.startSessionByNum(0)
	sources = uxp.getAllSources()
	for s in sources:
		uxp.toggleMute(s)
	sleep(5)
	for s in sources:
		uxp.toggleMute(s)
	uxp.endSession()
	log(mute_test.__name__, True)

def reboot_test():
	result = True
	uxp.openDeviceStatus()
	uxp.reboot()
	uxp.confirmReboot()
	sleep(120)
	uxp.login()
	try:
		assert "Your device is currently unavailable" not in driver.page_source
	except AssertionError:
		result = False
	log(reboot_test.__name__, result)
	sleep(10)

def sm_reboot_test():
	result = True
	device = uxp.getCurrentDeviceName()
	sm.restartDevice(devices, device)
	sleep(120)
	uxp.login()
	try:
		assert "Your device is currently unavailable" not in driver.page_source
	except AssertionError:
		result = False
	log(sm_reboot_test.__name__, result)
	sleep(10)

def we_logout_test():
	result = True
	uxp.openAdvanced()
	sleep(2)
	driver.switch_to_window(driver.window_handles[1])
	uxp.weLogout()
	driver.switch_to_window(driver.window_handles[0])
	driver.refresh()
	try:
		assert driver.current_url.endswith("login.php")
	except AssertionError:
		result = False
	log(we_logout_test.__name__, result)
	sleep(10)
	uxp.login()

def profile_reload_test():
	result = True
	before = uxp.getActiveProfile()
	driver.refresh()
	sleep(3)
	after = uxp.getActiveProfile()
	try:
		assert (before == after) is True
	except AssertionError:
		result = False
	log(profile_reload_test.__name__, result)

def profile_category_test():
	result = True
	uxp.openGenericProfiles()
	try:
		assert "2 Tx" in driver.page_source
	except AssertionError:
		result = False
	uxp.openApplicationProfiles()
	try:
		assert "Huddle Audience - Single Fiber" in driver.page_source
	except AssertionError:
		result = False
	log(profile_category_test.__name__, result)

def cancel_while_connecting_test():
		uxp.startSessionByNum(0)
		uxp.endSession()

def create_group_test():
	result = True
	uxp.createGroup()
	try:
		assert "Group 1" in driver.page_source
	except AssertionError:
		result = False
	log(create_group_test.__name__, result)

#Add Assertions
def add_fav_to_group_test():
	favs = uxp.getFavourites()
	for f in favs:
		uxp.addToGroup(f,"group-div-1")
	log(add_fav_to_group_test.__name__, True)

def remove_group_test():
	result = True
	uxp.removeGroup("group-div-1")
	sleep(1)
	try:
		assert "Group 1" not in driver.page_source
	except AssertionError:
		result = False
	log(remove_group_test.__name__, result)

def add_temp_fav_to_group_test():
	result = True
	uxp.openSearch()
	uxp.createSearchGroup()
	favs = uxp.getSearchResults()
	for f in favs:
		uxp.addToGroup(f,"groupSearch1")
	sleep(1)
	try:
		assert "Group 1" in driver.page_source
	except AssertionError:
		result = False
	log(add_temp_fav_to_group_test.__name__, result)
	uxp.closeSearch()
	sleep(1)

def remove_fav_from_group():
	for i in range(0,5):
		uxp.removeFromGroup("group-div-1")
	uxp.removeGroup("group-div-1")
	log(remove_fav_from_group.__name__, True)

####################################
#               Main               #
####################################

def main():
	start_logging()
	
	connection_test()
	login_test("172.17.137.23")
	endpoint_directory_test()
	add_favourites_test()
	remove_favourites_test()
	initiate_session_test_auto_anwser_on()
	initiate_session_test_auto_anwser_off()
	reject_session_test()
	change_profiles_while_idle_test()
	change_profiles_while_in_session_test()
	device_picture_test()
	mute_test()
	reboot_test()
	sm_reboot_test()
	we_logout_test()
	profile_reload_test()
	profile_category_test()
	cancel_while_connecting_test()
	create_group_test()
	add_fav_to_group_test()
	remove_group_test()
	add_temp_fav_to_group_test()
	remove_fav_from_group()
	
	stop_logging()

if __name__ == "__main__":	
	main()