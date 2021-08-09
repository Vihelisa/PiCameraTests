#Importação
import os 
from time import sleep
from picamera import PiCamera 

'''
    Capturando uma imagem através da câmera do raspberry e salvando numa pasra
    no diretório.
'''
FOLDER = 'Imagens_Teste'
name_image = 'nome_qualquer.jpg'
PATH = os.path.join(FOLDER, name_image)

camera = PiCamera()
camera.resolution = (1024, 768) #Resolução da imagem que será salva
camera.start_preview() #Método que esconde a spbreposição de pré-visualização

sleep(2)
camera.capture(PATH)  #Captura da imagem, salvando direto no diretório especificado.