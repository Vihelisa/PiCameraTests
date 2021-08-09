import serial 
import RPi.GPIO as GPIO 
from time import sleep

ser = serial.Serial("/dev/ttyACM0", 9600)
ser.flush()


while True:
    #Forma automatizada:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)
        num = input('Digite aqui: ')
        ser.write(num.decode())
        sleep(2)
        print(line)