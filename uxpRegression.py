import sys, datetime
sys.path.append('C:\\Users\\arehkopf\\Documents\\GitHub\\test-framework')
from selenium import webdriver
from time import sleep
import uxpTestFramework as uxp
import unittest

def startLogging():
	start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	with open("log.txt", "w") as log:
		log.write("##################################### Test Begin #####################################\n\n")
		log.write("Regression beginning at " + start + "\n")

def loginTest(ip):
	uxp.connect(ip)
	
	time = datetime.datetime.now().strftime("[%H:%M:%S]: Login Test at ")
	time = time + ip + " ... "
	
	with open("log.txt", "a") as log:
		log.write(time)
		try:
			assert "Evertz" in driver.title
			log.write("OK\n")
		except AssertionError:
			log.write("FAIL\n")
	
	uxp.login()

def endPointDirectoryTest():
	uxp.openSearch()
	devices = uxp.getSearchResults()
	time = datetime.datetime.now().strftime("[%H:%M:%S]: " + str(len(devices)) + " of 6 devices detected in endpoint directory ... ")

	with open("log.txt", "a") as log:
		log.write(time)
		try:
			assert len(devices) is 6
			log.write("OK\n")
		except AssertionError:
			log.write("FAIL\n")
	uxp.closeSearch()

### Add logic to check if favs are already added
def addRemoveFavouritesTest():
	uxp.openSearch()
	search = uxp.getFavouriteAddToggles()
	for s in search:
		uxp.toggleFavourite(s)
		sleep(0.1)
	uxp.closeSearch()
	favs = uxp.getFavourites()
	time = datetime.datetime.now().strftime("[%H:%M:%S]: Add favourites test ... ")

	with open("log.txt", "a") as log:
		log.write(time)
		try:
			assert len(favs) is 6
			log.write("OK\n")
		except AssertionError:
			log.write("FAIL\n")

	uxp.openSearch()
	search = uxp.getFavouriteRemoveToggles()
	for s in search:
		uxp.toggleFavourite(s)
		sleep(0.1)
	uxp.closeSearch()
	favs = uxp.getFavourites()
	time = datetime.datetime.now().strftime("[%H:%M:%S]: Remove favourites test ... ")

	with open("log.txt", "a") as log:
		log.write(time)
		try:
			assert len(favs) is 0
			log.write("OK\n")
		except AssertionError:
			log.write("FAIL\n")

#Add assertions
def initiateSessionTest():
	uxp.openSearch()
	search = uxp.getFavouriteAddToggles()
	for s in search:
		uxp.toggleFavourite(s)
		sleep(0.1)
	uxp.closeSearch()

	favs = uxp.getFavourites()
	for f in favs:
		uxp.startSession(f)
		sleep(2)
		uxp.endSession()
	time = datetime.datetime.now().strftime("[%H:%M:%S]: Initiate session test with auto answer off ... OK")

####################################
#               Main               #
####################################

def main():
	startLogging()
	loginTest("172.17.137.23")
	sleep(2)
	endPointDirectoryTest()
	addRemoveFavouritesTest()
	initiateSessionTest()
	uxp.endTest()

if __name__ == "__main__":
	driver = uxp.startTest()
	main()

'''
	openRoomControl()
	time.sleep(1)

	openCameraControls("local-camera0")
	time.sleep(1)

	selectPreset(1)
	time.sleep(1)
	
	moveCameraRight(1)
	moveCameraLeft(1)
	moveCameraUp(1)
	moveCameraDown(1)
	
	time.sleep(1)
	closeCameraControl()

	openPictureDialogue()
	sleep(1)
	selectPicture('C:\\Users\\arehkopf\\Desktop\\rkt.png')
	sleep(1)
	confirmPictureChange()
	sleep(5)

'''