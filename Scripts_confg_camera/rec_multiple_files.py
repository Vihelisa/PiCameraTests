from picamera import PiCamera
import os 

FOLDER = 'Video_Teste'
SECOUND_FOLDER = 'Multiple_Files'
name_image = '%d.mjpeg'
PATH = os.path.join(FOLDER, SECOUND_FOLDER, name_image)

'''
Este método serve para dividir uma gravação em vários arquivos  
'''

camera = PiCamera(resolution=(640, 480))
camera.start_recording(PATH)
camera.wait_recording(5)
for i in range(1, 11):
    camera.split_recording(PATH % i)
    camera.wait_recording(5)
camera.stop_recording()