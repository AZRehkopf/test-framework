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
'''
'''
	for j in range(7,10):
		for i in range(1,6):
			callee = 'favimg' + str(i)
			startSession(callee)
			time.sleep(2)
			endSession()
		profile =  'profimg' + str(j)
		changeProfile(profile, 5)
	
	changeProfile('profimg6', 5)
'''	

'''
	openRoomControl()
	time.sleep(1)

	toggleSwapDisplay()
	time.sleep(1)

	openProfileSources()
	time.sleep(1)
'''
'''
	openPictureDialogue()
	sleep(1)
	selectPicture('C:\\Users\\arehkopf\\Desktop\\rkt.png')
	sleep(1)
	confirmPictureChange()
	sleep(5)
'''
'''
	sleep(2)
	openSearch()
	toggleFavourite("favimg3000")
	sleep(1)
	closeSearch()
'''