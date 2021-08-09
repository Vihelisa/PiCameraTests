import os 
from time import sleep
from picamera import PiCamera

'''
Capitura de imagens consistentes, ou seja, várias imagens capituradas uma atrás da outras.

shutter_speed => Recupera ou define a velocidade do obturador da câmera em microsegundos.
exposure_speed => Recupera a velocidade atual do obturador da câmera.
exposure_mode => Recupera ou define o modo de exposição da câmera. retorna uma sequência 
representando a configuração de exposição da câmera.
awb_gains => Obtém ou define os ganhos de equilíbrio automático da câmera. retorna uma tupla 
de valores representando o equilíbrio (vermelho, azul) da câmera. 
awb_mode => Recupera ou define o modo de equilíbrio automático da câmera. retorna uma string 
representando a configuração de balanço de branco automático da câmera. 
'''


FOLDER = 'Imagens_Teste'
SECOUND_FOLDER = 'Consistent_image_test'
name_image = 'teste%02d.jpg'
PATH = os.path.join(FOLDER, SECOUND_FOLDER ,name_image)


camera = PiCamera(resolution=(1280, 720), framerate=30)
camera.iso = 100
sleep(2)
camera.shutter_speed = camera.exposure_speed 
camera.exposure_mode = 'off' #Fazer testes mudando as configurações 
g = camera.awb_gains
camera.awb_mode = 'off' #Fazer testes mudando as configurações 
camera.awb_gains = g 

camera.capture_sequence([PATH % i for i in range(10)]) #lista de 10 fotos a serem capturadas;