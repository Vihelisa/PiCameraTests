import serial
import time

'''
Neste teste o raspberry escreve uma mensagem na serial e o arduíno devolve uma outra frase 
e desta forma as duas são printadas no terminal.
'''

ser = serial.Serial("/dev/ttyACM0", 9600, timeout=1)
ser.flush()

while True:
    ser.write(b"Hello from raspberry!\n")
    line = ser.readline().decode('utf-8').rstrip()
    print(line)
    time.sleep(1)