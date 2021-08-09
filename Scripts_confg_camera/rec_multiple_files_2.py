from picamera import PiCamera
import os 

FOLDER = 'Video_Teste'
SECOUND_FOLDER = 'Multiple_Files'
name_image = 'teste%d.mjpeg'
PATH = os.path.join(FOLDER, SECOUND_FOLDER, name_image)


'''
Este método serve para dividir uma gravação em vários arquivos  
'''

camera = PiCamera(resolution=(640, 480))
for file in camera.record_sequence(
    PATH % i for i in range(1, 11)):
    camera.wait_recording(5)