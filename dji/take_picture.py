import android, time, os

droid = android.Android()

def titleAlert():
	title = 'Android Timelapse'
	message = 'Please enter interval and storage directory'
	
def chooseInterval():
	#default value
	timer = 5 
	return timer

def chooseFolder():
	#default folder
	myFolder = '/sdcard/DCIM/Camera/pyphotos'
	return myFolder

def takePictures(picFolder, intervalVal):
	maxPhotos = 10
	photoCounter = 0

	while photoCounter <= maxPhotos:
		captureTime = time.strftime("%Y%m%d_%H%M%S", time.localtime())
		captureLocation = picFolder + "/IMG_" +str(captureTime)+'.jpg'
		#false - for the autofocus
		droid.cameraCapturePicture(captureLocation, False)
		time.sleep(intervalVal)
		photoCounter += 1
	
def main():

	intervalVal = chooseInterval()
	picFolder = chooseFolder()
	takePictures(picFolder, intervalVal)
	
if __name__ == "__main__":
    main()