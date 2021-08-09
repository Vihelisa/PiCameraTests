from time import sleep
from picamera import PiCamera
from datetime import datetime, timedelta

'''
Capitura imagens e salva com o tempo entre as capturas de acordo com a hora da máquina local
salvando o nome dos arquivos com a data em que foram tiradas as fotos.
'''
#Não deu certo nos testes, ver o que é

def wait():
    # Calculate the delay to the start of the next hour
    next_hour = (datetime.now() + timedelta(hour=1)).replace(
        minute=0, second=0, microsecond=0)
    delay = (next_hour - datetime.now()).seconds
    sleep(delay)


camera = PiCamera()
camera.start_preview()
wait()
for filename in camera.capture_continuous('img{timestamp:%Y-%m-%d-%H-%M}.jpg'):
    print('Captured %s' % filename)
    wait()