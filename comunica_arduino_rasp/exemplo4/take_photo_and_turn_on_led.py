import os 
import  serial
from time import sleep
from picamera import PiCamera

FOLDER = 'Imagens_Teste'
num = 1

def cria_pasta():
    if os.path.exists(FOLDER): 
        pass
    else:
        os.mkdir(FOLDER)

ser = serial.Serial("/dev/ttyACM0", 9600)
ser.flush()

while True:
    cria_pasta()
    name_image = 'teste' + str(num) + '.jpg'
    PATH = os.path.join(FOLDER, name_image)
    num = num + 1
    ser.write(b'1\n')
    #line = ser.readline()
    print('LED LIGADO')
    camera = PiCamera()
    camera.resolution = (1024, 768) 
    camera.start_preview()
    sleep(2)
    camera.capture_continuous(PATH)
    print('Foto capiturada')
    sleep(2)
    ser.write(b'0\n')
    print('LED APAGADO')
    sleep(1)
    