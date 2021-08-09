import os 
from time import sleep
from picamera import PiCamera, Color
import datetime as dt 

FOLDER = 'Video_Teste'
name_image = 'annotate_video.mjpg'
PATH = os.path.join(FOLDER, name_image)

'''
Este método permite que uma data e hora na foto assim que foi capiturada
'''

camera = PiCamera(resolution=(640, 480), framerate=24)
camera.start_preview()
camera.annotate_background = Color('black')
camera.annotate_text = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
camera.start_recording(PATH)
start = dt.datetime.now()

while (dt.datetime.now() - start).seconds < 30:
    camera.annotate_text  = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    camera.wait_recording(0.2)
camera.stop_recording()