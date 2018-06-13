import sys, os, datetime
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)
dir_path = dir_path[:len(dir_path) - 4]
from selenium import webdriver
from time import sleep
from random import randint as rand
from selenium.common.exceptions import TimeoutException
import uxpTestFramework as uxp

def startup():
	global favourites, driver, connections
	connections = 0
	driver = uxp.startTest()
	uxp.connect("172.17.137.25")
	uxp.login()
	sleep(5)
	favourites = uxp.getFavourites()
	start = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	with open(os.path.join(dir_path,"logs\\ltr_log.txt"), "w") as log:
		log.write("##################################### Test Begin #####################################\n\n")
		log.write("Test beginning at " + start + "\n\n")

def log(fav, delay, status):
	global connections
	time = datetime.datetime.now().strftime("[%H:%M:%S]: ")
	init = ""
	
	if status is "open":
		init = "Starting "
		end = ". Aniticiapted duration: " + str(delay) + " seconds.\n"
	elif status is "close":
		init = "Closing "
		end = ".\n"
		connections += 1
	elif status is "error":
		message = time + "Connection with favourite " + str(fav) + " failed.\n"

	if status is not "error":	
		message = time + init + "connection with favourite " + str(fav) + end
	
	with open(os.path.join(dir_path,"logs\\ltr_log.txt"), "a") as log:
		log.write(message)

def runtime():
	time_expired = False
	while not time_expired:
		sleep(10)
		fav = rand(0,len(favourites) - 1)
		time = rand(1,120)
		
		try: 
			uxp.startSession(favourites[fav])
			log(fav,time,"open")
		except TimeoutException: log(fav,time,"error")
		
		sleep(time)
		
		try: 
			uxp.endSession()
			log(fav,time,"close")
		except TimeoutException: log(fav,time,"error")
		
		if (datetime.datetime.now() > datetime.datetime(2018,6,14,8,0,0)):
			time_expired = True

def shutdown():
	end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	with open(os.path.join(dir_path,"logs\\ltr_log.txt"), "a") as log:
		log.write("\nTest ended at " + end + "\n")
		log.write("Total conenctions: " + str(connections) + "\n\n")
		log.write("#####################################  Test End  #####################################\n\n")
	uxp.endTest()

def main():
	startup()
	runtime()
	shutdown()
	
if __name__ == "__main__":	
	main()