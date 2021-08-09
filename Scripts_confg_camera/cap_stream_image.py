import os 
from io import BytesIO
from time import sleep
from picamera import PiCamera 

'''
Capitura de imagem abrindo um arquivo ante da captura e após a execução da captura da imagem
fechar esse arquivo antes aberto.
'''

FOLDER = 'Imagens_Teste'
name_image = 'TESTE.jpg'
PATH = os.path.join(FOLDER, name_image)


my_file = open(PATH, 'wb') #Abrindo arquivo para escrita em binário
camera = PiCamera()
camera.start_preview()
sleep(2)
camera.capture(my_file) #Captura da imagem e armazená-la no arquivo antes aberto

my_file.close() #Fechar o arquivo


