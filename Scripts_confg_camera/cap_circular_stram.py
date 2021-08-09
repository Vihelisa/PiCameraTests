import io
import os 
import random 
import picamera 

def motion_detected():
    return random.randint(0, 10) == 0


camera = picamera.PiCamera()
stream = picamera.PiCameraCircularIO(camera, seconds=20)
camera.start_recording(stream, format='h264')
try:
    while True:
        camera.wait_recording(1)
        if motion_detected():
            camera.wait_recording(2)
            stream.copy_to('teste')
finally:
    camera.stop_recording()