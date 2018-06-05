import sys, os, datetime
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)
from selenium import webdriver
from time import sleep
from random import randint as rand
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
	with open("ltr_log.txt", "w") as log:
		log.write("##################################### Test Begin #####################################\n\n")
		log.write("Test beginning at " + start + "\n\n")

def log(fav, delay, status):
	global connections
	time = datetime.datetime.now().strftime("[%H:%M:%S]: ")
	init = ""
	if status:
		init = "Starting "
		end = ". Aniticiapted duration: " + str(delay) + " minutes.\n"
	else:
		init = "Closing "
		end = ".\n"
		connections += 1
	message = time + init + "connection with favourite " + str(fav) + end
	with open("ltr_log.txt", "a") as log:
		log.write(message)

def runtime():
	time_expired = False
	while not time_expired:
		sleep(10)
		fav = rand(0,4)
		time = rand(1,61)
		log(fav,time,True)
		uxp.startSession(favourites[fav])
		sleep(time)
		uxp.endSession()
		log(fav,time,False)
		if (datetime.datetime.now() > datetime.datetime(2018,6,5,16,35,0)):
			time_expired = True

def shutdown():
	end = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	with open("ltr_log.txt", "a") as log:
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