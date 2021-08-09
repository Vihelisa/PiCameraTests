import os 
from time import sleep
from picamera import PiCamera 


FOLDER = 'Imagens_Teste'
name_image = 'annotate.jpg'
PATH = os.path.join(FOLDER, name_image)

'''
Permite que uma frase seja adicionada assim que a imagem for capturada.
'''

camera = PiCamera(resolution=(640, 480))
camera.framerate = 24
camera.start_preview()
camera.annotate_text = 'Hello World'
sleep(2)
camera.capture(PATH)
