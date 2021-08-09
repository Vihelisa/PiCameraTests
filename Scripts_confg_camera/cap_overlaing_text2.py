import os 
from time import sleep
from picamera import PiCamera 


FOLDER = 'Imagens_Teste'
name_image = 'annotate_image.jpg'
PATH = os.path.join(FOLDER, name_image)

'''
Este método permite que seja permitido  adicionar, após a imagem ser capiturada, um texto formatado
'''

DICA = str('''
            JCAJCOISCJOIJC
            JCNSCNSKLSCSLC
            NCJNKNAKLAS
            NXCLNKXCASJXK
''')


camera = PiCamera(resolution=(640, 480))
camera.framerate = 24
camera.start_preview()
camera.annotate_text = DICA
sleep(2)
camera.capture(PATH)
