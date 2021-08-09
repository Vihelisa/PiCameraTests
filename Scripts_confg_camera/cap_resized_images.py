import os 
from time import sleep
from picamera import PiCamera

'''
Às vezes, particularmente em scripts que realizarão algum tipo de análise ou
processamento em imagens, você pode querer capturar imagens menores do que a 
resolução atual da câmera. Embora tal redimensionamento possa ser realizado usando 
bibliotecas como PIL ou OpenCV, é consideravelmente mais eficiente fazer com que a 
GPU do Pi realize o redimensionamento ao capturar a imagem. Isso pode ser feito com 
o parâmetro de redimensionar dos métodos de captura.

O parâmetro de redimensionar também pode ser especificado ao gravar vídeo com o método 
start_recording().
'''


FOLDER = 'Imagens_Teste'
name_image = 'teste3.jpg'
PATH = os.path.join(FOLDER, name_image)


camera = PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

sleep(2)
camera.capture(PATH, resize=(320, 240))