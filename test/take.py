import time
import picamera
import uuid

with picamera.PiCamera() as camera:
	directory = "white"
	camera.resolution = (640, 480)
	camera.framerate = 30
	time.sleep(2)
	camera.shutter_speed = camera.exposure_speed
	camera.exposure_mode = 'off'
	g = camera.awb_gains
	camera.awb_mode = 'off'
	camera.awb_gains = g
	camera.capture(directory + "/" + str(uuid.uuid4()) + ".jpg")
