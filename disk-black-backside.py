import time
import picamera
import uuid

with picamera.PiCamera() as camera:
    imgobject = "disk_black_backside"
    camera.resolution = (640, 480)
    camera.framerate = 30
    # Wait for the automatic gain control to settle
    time.sleep(2)
    # Now fix the values
    camera.shutter_speed = camera.exposure_speed
    camera.exposure_mode = 'off'
    g = camera.awb_gains
    camera.awb_mode = 'off'
    camera.awb_gains = g
    # Finally, take several photos with the fixed settings
    for i in range(17):
        name = 'pictures/' + imgobject + '/' + imgobject + '_' + str(i) + '_' +  str(uuid.uuid4()) + '.jpg'
        camera.capture(name)
    # camera.capture_sequence(['pictures/'+imgobject+'/'+imgobject+'_image%02d-' + str(uuid.uuid4()) + '.jpg' % i for i in range(17)])
