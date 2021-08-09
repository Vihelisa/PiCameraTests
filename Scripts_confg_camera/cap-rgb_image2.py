import time
import picamera
import picamera.array
import numpy as np

#um erro ocorreu, ver depois o que é 

with picamera.PiCamera() as camera:
    camera.resolution = (100, 100)
    time.sleep(2)
    image = np.empty((128, 112, 3), dtype=np.uint8)
    camera.capture(image, 'rgb')
    image = image[:100, :100]