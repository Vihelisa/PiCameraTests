import os 
from io import BytesIO
from time import sleep
from picamera import PiCamera 

'''
Neste método o script roda, não indica nenhum erro mas a imagem captuda não aparece
no diretório indicado
'''

FOLDER = 'Imagens_Teste'
name_image = 'teste1'
PATH = os.path.join(FOLDER, name_image)

my_stream = BytesIO() #Tirar dúvida sobre esse método BytesIO 
camera = PiCamera()
camera.start_preview()

sleep(2)
camera.capture(my_stream, 'jpeg')