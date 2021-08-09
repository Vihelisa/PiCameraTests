import os 
from time import sleep
from fractions import Fraction
from picamera import PiCamera

'''
Este método apresenta forma de controlar a luz da câmera para as capturas de imagem

OBS: Pode-se pegar como base o 6000, abaxo dele o preto começa a predominar e a cima dele o branco
'''

FOLDER = 'Imagens_Teste'
name_image = 'low_light3.jpg'
PATH = os.path.join(FOLDER, name_image)


camera = PiCamera(
    resolution=(1280, 720),
    framerate=Fraction(1, 6), #retorna a taxa em que as portas de vídeo e visualização da câmera funcionarão como uma instância 
    sensor_mode=3
)
camera.shutter_speed = 600000 #Muda a iluminação, quanto maior mais claro
camera.iso = 800  #retorna a configuração ISO da câmera, um valor que representa a sensibilidade da câmera à luz. 
sleep(10)
camera.exposure_mode ='off'
camera.capture(PATH)

