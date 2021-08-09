from picamera import PiCamera
from io import BytesIO
from time import sleep
from PIL import Image 

'''
Este método depende da bibliotecal PIL a qual ainda precisa ser 
intalada no raspberry para que o teste possa ser concluido
'''

stream = BytesIO()
camera = PiCamera()
camera.start_preview()
sleep(2)
camera.capture(stream, format='jpeg')

stream.seek(0)
image = Image.open(stream)