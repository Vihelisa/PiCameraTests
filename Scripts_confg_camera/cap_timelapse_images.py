import os 
from time import sleep
from picamera import PiCamera

'''
Sequência de captura de imagens possuindo um tempo determinado entre as capturas.

capture_continuous => Capture imagens continuamente da câmera como um iterador infinito.
'''

FOLDER = 'Imagens_Teste'
SECOUND_FOLDER = 'Timelapse_Images_Test'
name_image = 'teste{counter:03d}.jpg' #colocar um método counter no nome para que seja salvo arquivos com nomes diferentes e em ordem numérica 
PATH = os.path.join(FOLDER, SECOUND_FOLDER , name_image)


camera = PiCamera()
camera.start_preview()
sleep(2)
for filename in camera.capture_continuous(PATH):
    print('Captured %s' % filename)
    sleep(120) # espera 1 minutes