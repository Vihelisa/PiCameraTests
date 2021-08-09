import os
import picamera

'''
Faz a gravação de um video no formato arquivo e cok tempo determinado.

wait_recording => Espere no codificador de vídeo por segundos de intervalo. Recomenda-se que 
este método seja chamado durante a gravação para verificar se há exceções. Se ocorrer um erro 
durante a gravação (por exemplo, fora do espaço do disco), a gravação será parada
'''

FOLDER = 'Video_Teste'
name_image = 'testevideo.mjpeg'
PATH = os.path.join(FOLDER, name_image)


camera = picamera.PiCamera()
camera.resolution = (640, 480) #Resolução do vídeo
camera.start_recording(PATH) #Comece a gravar vídeo da câmera, armazenando-o na saída.
camera.wait_recording(60)   
camera.stop_recording() #Pare de gravar vídeo da câmera.